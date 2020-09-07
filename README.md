

# Deep Image Video Analogy
the following Google Colab notebook installs the libraries required to run our code and runs our code (make sure that notebook uses a GPU runtime):

https://colab.research.google.com/drive/1pbEvVPZIFs1wERpxrbF66dFX1oE6pAOI?usp=sharing

This is a fork of the linux branch of the original Deep Image Analogy paper's repository which can be found in:
https://github.com/msracver/Deep-Image-Analogy/tree/linux

##our project
In (Liao, et al. 2017), the authors proposed a new technique, Deep Image Analogy, for visual attribute transfer across images of similar semantic content, but which may vary significantly in terms of appearance (e.g. color, tone, texture and style.) Deep Image Analogy allows to transfer such attributes by creating two analogy images, each with the spatial structure of one and the visual attributes of the other.
The technique described in (Liao, et al. 2017) achieves this goal by finding mappings between the deep feature maps of the two images, and gradually translating that mapping to a spatial mapping between the original images. These mappings, which map pixels corresponding to the same semantic location, can be used to create the analogy by warping (and slightly smoothing) each input image to fit the spatial structure of the other, thus getting new images with the visual content of one input image and the spatial structure of the other.
In this work we aim to extend this method to visual attribute transfer between images and video. To do so we propose Deep Image Video Analogy (DIVA), which gets an image and a video with similar semantic content (e.g. depicting a similar scene, object or animal,) and produces a new video with the spatial structure of the original video and the visual appearance of the image.

##example
<b>Input video:</b>

<img src="https://imgflip.com/gif/4e56p9" width="300" height="500" title="hover text">
<b>Input image:</b>

<img src="https://ibb.co/RjFRDSz" width="300" height="500" title="hover text">
<b>Outout:</b>

<img src="https://imgflip.com/gif/4e56r6" width="300" height="500" title="hover text">
