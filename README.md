# Keep Talking

<div style="border-style: solid; border-width: thin; border-color: lightgrey;" align="center" width="100%">
    <img width="33%" src=".github/icon.png">
    <h3>A forensic audio analysis tool</h3>
    <h3>focused on voice identification and enhancement in low signal-to-noise ratio material.</h3>
</div>

## Methodology

This tool uses variance of spectral entropy to enhance vocal information.

<p  style="border-style: solid; border-width: thin; border-color: lightgrey;" align="center" width="100%">
    <img width="100%" src=".github/screenshot.png"> 
</p>

### Example

The audio files below are an example of recordings of the audio component of the Microwave Auditory Effect. You can hear that the algorithm enhances the amplitude envelope of speech patterns, enhancing the intelligibility of the material.

**noisy file:** ![noisy.mp4](https://raw.githubusercontent.com/subliminalindustries/keeptalking/main/.github/noisy.mp4)

**processed file:** ![noisy-processed.mp4](https://raw.githubusercontent.com/subliminalindustries/keeptalking/main/.github/noisy-processed.mp4)

The audio was captured using the paid version of the Hear-Boost app ([Apple App Store](https://apps.apple.com/en/app/hear-boost-recording-ear-aid/id1437159134), [Google Play Store](https://play.google.com/store/apps/details?id=com.audiofix.hearboost)) which is excellent at recording the audio spectrum components of the Microwave Auditory Effect. The settings used in Hear-Boost were: Volume Boost: 200x, Device Mic: On, Voice Filter: Off. While recording using this app sure to turn your phone volume down 100% to prevent runaway microphone feedback.

NOTE: For now the algorithm processes the entire spectrum at once instead of processing frequency bins separately. Also there is some fine-tuning left to do to take out the jitter in amplitude.

## To-Do

- Run the algorithm on frequency bins instead of the entire frequency spectrum of the input file;
- Fine-tune smoothing parameters to reduce amplitude jitter;
- Enhance both tracks of stereo files instead of using only one channel.
