import os
from pathlib import Path

import Algorithmia


API_KEY = os.environ.get('ALGO_API_KEY')
DATA_DIR_BASE = os.environ.get('DATA_DIR')
ORIGINAL_DATA_DIR = DATA_DIR_BASE + 'original/'
TRANSFERD_DATA_DIR = DATA_DIR_BASE + 'transferd/'


def upload(client, fnames):
    for im in fnames:
        client.file(ORIGINAL_DATA_DIR + str(im.name)).put(im.read_bytes())


def download(client, folder):
    folder = Path(folder)
    transfered = client.dir(TRANSFERD_DATA_DIR)
    for im in transfered.files():
        (folder / Path(im.url).name).write_bytes(im.getBytes())


def style_transfer(fnames, out_folder, filter_name):
    client = Algorithmia.client(API_KEY)
    p = Path(in_folder)
    assert p.exists()

    ims = upload(client, p)
    inputs = {
        "images": [ORIGINAL_DATA_DIR + im for im in ims],
        "savePaths": [TRANSFERD_DATA_DIR + im for im in ims],
        "filterName": filter_name
    }

    algorithm_name = 'deeplearning/DeepFilter/0.6.0'
    algo = client.algo(algorithm_name)
    result = algo.pipe(inputs).result

    download(client, out_folder)
    return result
