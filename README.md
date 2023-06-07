# Keep Talking

A forensic audio analysis tool focused on voice identification and enhancement in low signal-to-noise ratio material.

![Screenshot](https://raw.githubusercontent.com/subliminalindustries/keeptalking/934a8f9c863e00531103b9a3ef8275e325362234/.github/keeptalking.png "keeptalking")

## Methodology

This tool uses variance of spectral entropy and its rate of change together with the instantaneous frequency from the Hilbert transform to enhance vocal information.

## To-Do

- Run the algorithm on frequency bins instead of the entire frequency spectrum of the input file;
- Enhance both tracks of stereo files instead of using only one channel.
