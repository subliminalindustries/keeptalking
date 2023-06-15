#!/usr/bin/env python
# coding: utf-8

import os
import sys

import audiofile
import numpy as np

from scipy.fft import rfft, irfft
from sklearn.preprocessing import minmax_scale

from plot import plot


def load_audio_file(filename: str):
    fp = os.path.realpath(filename)
    if not os.path.isfile(fp):
        raise FileNotFoundError(f'file {fp} not found.')

    data, sample_rate = audiofile.read(fp)

    # TODO: mix stereo to mono or process both channels
    if data.ndim == 2 and data.shape[0] == 2:
        data = data[0]

    fp, ext = os.path.splitext(fp)

    # TODO: figure out whether file is signed or unsigned
    return minmax_scale(data, (-1., 1.)), sample_rate, fp, ext


def interpolate(data: np.ndarray, to_size: int):
    return np.interp(np.linspace(0, data.size - 1, num=to_size), np.arange(data.size), data)


def spectral_entropy(data: np.ndarray, bit_rate: int = 24):
    if data.size < 2:
        return 0.

    data = data[data.nonzero()]
    probability = data / np.sum(data)

    return -np.sum(probability * np.log2(probability)) / np.log2(bit_rate)


def spectral_entropy_voice_recovery(data: np.ndarray, nfft: int = 512):
    print(f'- data contains {data.shape[0]} samples')

    fft_blocks = []
    for block in range(0, data.size - 1, nfft):
        block_size = min(data.size - 1, nfft)
        fft_blocks.append(rfft(data[block:block+block_size], n=nfft)[1:])

    fft_blocks = np.array(fft_blocks).T
    freqs, steps = fft_blocks.shape

    h_entropy = np.ndarray(shape=fft_blocks.shape)  # horizontal spectral entropy
    # v_entropy = np.ndarray(shape=sxx.shape)  # vertical spectral entropy

    print("- calculating spectral entropy for each FFT frequency bin..")
    for freq in range(0, freqs - 1):
        entropy = np.ndarray(shape=(steps,))
        entropy.fill(spectral_entropy(fft_blocks[freq, :]).real)
        h_entropy[freq, :] = entropy

    # print(f'- calculating vertical spectral entropy..')
    # for step in range(0, t-1):
    #     entropy = np.ndarray(shape=(f,))
    #     entropy.fill(spectral_entropy(sxx[:, step]).real)
    #     v_entropy[:, step] = entropy

    # E = minmax_scale(H * V, (0., 1.))
    # E = minmax_scale(V, (0., 1.))
    sxx_entropy = minmax_scale(h_entropy, (0., 1.))

    float_sm = np.finfo(np.float64).tiny

    print('- calculating differential spectral entropy for each FFT bin..')
    freqs_entropy = np.copy(sxx_entropy)
    for freq in range(0, freqs - 1):
        for current_freq in range(0, freqs - 1):
            if current_freq == freq:
                freqs_entropy[current_freq, :] = sxx_entropy[current_freq, :]
                continue

            base_freq_entropy = np.nan_to_num(sxx_entropy[freq, :], nan=float_sm, posinf=1.-float_sm,
                                              neginf=0.+float_sm)

            current_freq_entropy = np.nan_to_num(sxx_entropy[current_freq, :], nan=float_sm, posinf=1.-float_sm,
                                                 neginf=0.+float_sm)

            diff = np.square(np.sqrt(base_freq_entropy) - np.sqrt(current_freq_entropy))
            freqs_entropy[current_freq, :] = np.abs(diff)

        fft_blocks[freq] = fft_blocks[freq] * minmax_scale(freqs_entropy, (0., 1.))[freq]

    print('- applying inverse FFT..')
    output = []
    for step in range(0, steps - 1):
        output.append(irfft(fft_blocks[:, step], n=nfft))

    print('- normalizing output..')
    output = minmax_scale(interpolate(np.block(output), data.shape[0]), (-1., 1.))

    return output


signal, fs, file, extension = load_audio_file(sys.argv[1])

nfft = 1024
if len(sys.argv) == 3:
    nfft = int(sys.argv[2])

print(f'- processing "{file}{extension}"..')
output_signal = spectral_entropy_voice_recovery(signal, nfft=nfft)

if len(sys.argv) == 4 and sys.argv[3] == '--plot':
    plot(filename=f'{file}{extension}', sample_rate=fs, input_signal=signal, output_signal=output_signal, width=7,
         height=7)

output_filename = f'{file}-entropy{extension}'
print(f'- writing "{output_filename}"..')

if os.path.isfile(f'{file}-entropy.wav'):
    os.remove(f'{file}-entropy.wav')

audiofile.write(f'{file}-entropy.wav', output_signal, fs, bit_depth=24, normalize=True)
