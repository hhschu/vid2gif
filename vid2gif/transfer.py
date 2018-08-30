import os
from pathlib import Path

import Algorithmia


API_KEY = os.environ.get('ALGO_API_KEY')
DATA_DIR_BASE = os.environ.get('DATA_DIR')
ORIGINAL_DATA_DIR = DATA_DIR_BASE + 'original/'
TRANSFERD_DATA_DIR = DATA_DIR_BASE + 'transferd/'


def upload(client, fnames):
    for im in fnames:
        im = Path(im)
        client.file(ORIGINAL_DATA_DIR + str(im.name)).put(im.read_bytes())


def download(client, folder):
    folder = Path(folder)
    transfered = client.dir(TRANSFERD_DATA_DIR)
    for im in transfered.files():
        (folder / Path(im.url).name).write_bytes(im.getBytes())


def style_transfer(fnames, out_folder, filter_name):
    client = Algorithmia.client(API_KEY)
    client.dir(ORIGINAL_DATA_DIR).create()
    client.dir(TRANSFERD_DATA_DIR).create()

    upload(client, fnames)
    inputs = {
        "images": [ORIGINAL_DATA_DIR + Path(im).name for im in fnames],
        "savePaths": [TRANSFERD_DATA_DIR + Path(im).name  for im in fnames],
        "filterName": filter_name
    }

    algorithm_name = 'deeplearning/DeepFilter/0.6.0'
    algo = client.algo(algorithm_name)
    result = algo.pipe(inputs).result

    download(client, out_folder)
    return result
