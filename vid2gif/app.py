import argparse
import shutil
import tempfile

import vid2pic
import transfer

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='Input video file')
parser.add_argument('--output', type=str, help='Location to store output files')
parser.add_argument('--filter_name', type=str, default='alien_goggles', help='Name of the style filter')


if __name__ == '__main__':
    opts = args = parser.parse_args()
    temp_dir = tempfile.gettempdir()
    ims = vid2pic.to_pic(fname=opts.input, to_folder=temp_dir)
    transfer.style_transfer(fnames=ims, out_folder=opts.output, filter_name=opts.filter_name)
    shutil.rmtree(temp_dir)
