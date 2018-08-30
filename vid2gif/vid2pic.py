from pathlib import Path

import skvideo.io
import skimage.transform


def to_pic(fname, to_folder, sample_rate=12):
    folder = Path(to_folder)
    folder.mkdir(parents=True, exist_ok=True)

    fname = Path(fname)
    assert fname.exists()

    vid = skvideo.io.vreader(str(fname))
    outfile_names = []
    for i, frame in enumerate(vid):
        if i % sample_rate == 0:
            frame = skimage.transform.rescale(frame, 1, mode='constant', preserve_range=True)
            outfile_name = str(folder / '%s-%s.png' % (fname.stem, i))
            skimage.io.imsave(outfile_name, frame)
            outfile_names.append(outfile_name)
        else:
            continue
    return outfile_names
