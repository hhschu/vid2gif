import os

import numpy as np
from moviepy.editor import ImageSequenceClip


def to_gif(filename, array, fps=12, scale=1.0):
    fname, _ = os.path.splitext(filename)
    filename = fname + '.gif'

    # copy into the color dimension if the images are black and white
    if array.ndim == 3:
        array = array[..., np.newaxis] * np.ones(3)

    # make the moviepy clip
    clip = ImageSequenceClip(list(array), fps=fps)
    clip.resize(scale)
    clip.write_gif(filename, fps=fps)
    return clip
