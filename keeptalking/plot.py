import numpy as np
import matplotlib.pyplot as plt


def plot(filename: str, sample_rate: int, input_signal: np.ndarray, output_signal: np.ndarray, width: int = 5,
         height: int = 5):

    f = plt.figure()

    # f.subplots_adjust(left=0.1, right=0.9, top=2.9, hspace=0.6)
    f.set_figheight(height)
    f.set_figwidth(width)

    plt.suptitle(f'Analysis of "{filename}"', y=3.)

    xs = np.linspace(0, input_signal.size / sample_rate, input_signal.size, endpoint=False)
    ax_sig = f.add_subplot(411)
    ax_sig.margins(x=0)
    ax_sig.set_ylim(bottom=-1., top=1.)
    ax_sig.set_title('Input Signal')
    ax_sig.set_ylabel('Amplitude')
    ax_sig.set_xlabel('Time (s)')
    ax_sig.plot(xs, input_signal, color='#333333', linewidth=.1)

    ax_psd_spec = f.add_subplot(412)
    ax_psd_spec.margins(x=0)
    ax_psd_spec.set_title('Input Signal PSD Spectrum')
    ax_psd_spec.set_ylabel('Frequency (Hz)')
    ax_psd_spec.set_xlabel('Time (s)')
    ax_psd_spec.specgram(input_signal, NFFT=1024, Fs=sample_rate, window=np.bartlett(1024), noverlap=900, mode='psd',
                         cmap='nipy_spectral')

    ax_se = f.add_subplot(413)
    ax_se.margins(x=0)
    ax_se.set_ylim(bottom=-1., top=1.)
    ax_se.set_title('Output Signal')
    ax_se.set_ylabel('Amplitude')
    ax_se.set_xlabel('Time (s)')
    ax_se.plot(xs, output_signal, color='magenta', linewidth=.1)

    ax_psd_spec = f.add_subplot(414)
    ax_psd_spec.margins(x=0)
    ax_psd_spec.set_title('Output Signal PSD Spectrum')
    ax_psd_spec.set_ylabel('Frequency (Hz)')
    ax_psd_spec.set_xlabel('Time (s)')
    ax_psd_spec.specgram(output_signal, NFFT=1024, Fs=sample_rate, window=np.bartlett(1024), noverlap=900, mode='psd',
                         cmap='nipy_spectral')

    plt.show()

