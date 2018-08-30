import numpy as np
import skvideo.io
import skimage.transform


def to_pic(fname, sample_rate=12):
    vid = skvideo.io.vreader(fname)
    frames = [skimage.transform.rescale(frame, 1, mode='constant', preserve_range=True)
              for i, frame in enumerate(vid) if i % sample_rate == 0]
    frames = np.array(frames).astype(np.uint8)
    return frames
