import re
import os
import subprocess
from tqdm import tqdm


for d in tqdm(os.listdir('manga')):

    # Get list of jpgs in directory
    imgs = [os.path.join('manga', d, f) for f in os.listdir(os.path.join('manga', d))]

    # Sort list of jpgs to match page order
    imgs = sorted(imgs, key=lambda x: int(re.sub('[^0-9]+', '', x)))

    if not os.path.exists('pdfs'):
        os.makedirs('pdfs')

    cmd = ['img2pdf', *imgs, '-o', f'pdfs/{d}.pdf']
    subprocess.call(cmd)
