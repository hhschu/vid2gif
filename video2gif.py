import numpy as np
import skvideo
import skvideo.io
import skimage.transform
import skvideo.datasets
import skvideo.utils
import os
from moviepy.editor import ImageSequenceClip

#'Polar_orbit.ogv.360p.mkv'
def get_video(file_name):
    vid = skvideo.io.vreader(file_name)

    downsample_factor = 12

    frames = []
    for frameIdx, frame in enumerate(vid):
        if frameIdx % downsample_factor == 0:
            frame = skimage.transform.rescale(frame, 1, mode='constant', preserve_range=True).astype(np.uint8)
            frames.append(frame)
        else:
            continue

    frames = np.array(frames).astype(np.uint8)
    print(frames.shape)
    return frames

def get_gif(filename, array, fps=12, scale=1.0):
    """Creates a gif given a stack of images using moviepy
    Notes
    -----
    works with current Github version of moviepy (not the pip version)
    https://github.com/Zulko/moviepy/commit/d4c9c37bc88261d8ed8b5d9b7c317d13b2cdf62e
    Usage
    -----
    >>> X = randn(100, 64, 64)
    >>> gif('test.gif', X)
    Parameters
    ----------
    filename : string
        The filename of the gif to write to
    array : array_like
        A numpy array that contains a sequence of images
    fps : int
        frames per second (default: 10)
    scale : float
        how much to rescale each image by (default: 1.0)
    """

    # ensure that the file has the .gif extension
    fname, _ = os.path.splitext(filename)
    filename = fname + '.gif'

    # copy into the color dimension if the images are black and white
    if array.ndim == 3:
        array = array[..., np.newaxis] * np.ones(3)

    # make the moviepy clip
    clip = ImageSequenceClip(list(array), fps=fps).resize(scale)
    clip.write_gif(filename, fps=fps)
    return clip
