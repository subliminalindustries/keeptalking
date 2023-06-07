# Keep Talking

<p style="border-style: solid; border-width: thin; border-color: lightgrey;" align="center" width="100%">
    <img width="66%" src=".github/icon.png"> 
</p>

A forensic audio analysis tool focused on voice identification and enhancement in low signal-to-noise ratio material.

## Methodology

This tool uses variance of spectral entropy and its rate of change together with the instantaneous frequency from the Hilbert transform to enhance vocal information.

<p  style="border-style: solid; border-width: thin; border-color: lightgrey;" align="center" width="100%">
    <img width="100%" src=".github/screenshot.png"> 
</p>

### Example

Below is an example where you can see that the algorithm enhances the contours of speech patterns enhancing the intelligibility of the material.

**noisy file:**
<p style="border-style: solid; border-width: thin; border-color: lightgrey;" align="center" width="100%">
	<video controls>
	  <source src=".github/noisy.mp4" type="video/mp4">
	</video>
</p>

**processed file:**
<p style="border-style: solid; border-width: thin; border-color: lightgrey;" align="center" width="100%">
	<video controls>
	  <source src=".github/noisy-processed.mp4" type="video/mp4">
	</video>
</p>

NOTE: For now the algoritm processes the entire spectrum at once instead of processing frequency bins separately. Also there is some fine-tuning left to do to take out the jitter in amplitude.

## To-Do

- Run the algorithm on frequency bins instead of the entire frequency spectrum of the input file;
- Fine-tune smoothing parameters to reduce amplitude jitter;
- Enhance both tracks of stereo files instead of using only one channel.
