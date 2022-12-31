# coco
Colour-Colour (CoCo) Image Analyser launches an interactive window where you may load an image, plot its pixels in a
channel-channel (e.g., red-green, red-blue, green-blue) space, giving you an idea of how much content of each channel has
each colour in the image. Useful for teaching about image segmentation algorithms such as k-means.


Steps for analysing the colour distribution of an image:
1. Put all the images you want to analyse into the same folder as the Python script
2. Launch the script. This should open an interactive window.
3. Write the name of a file (e.g., "chamiza.jpg") into the text entry box, then click load.
4. Double click on the button that indicates which channels (r, g,or b) you'd want to use as x-y axes for the colour analysis.
    Depending on the image, checking different channel combinations might provide different info.
5. Click the "analyse" button. This will take a while since the code maps every pixel into a different plot. The program may even
    crash if there's not enough memory. Just relaunch it if that's the case. If the error persists, the code is probably needing more
    memory than your machine is providing.
6. Once the analysis plot is shown to the right of the original image, you may either double click at a different colour combination
    button and re-analyse, or hit the "Save" button. This will save "<filename>_analysis_<axes>.png" to your local
    directory, where <filename> is the name of the file loaded (e.g., chamiza), and <axes> is the colour-colour combination in the axes.
7. At any given moment, you may rewrite the image name and hit "Load" again to load a different image.
