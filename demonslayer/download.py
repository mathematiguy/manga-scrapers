import os
import json
import subprocess


downloads = json.load(open('demonslayer.json'))

for d in downloads:
    folder_dir = os.path.join('manga', d['chapter'])
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)
    fp = os.path.join(folder_dir, d['url'].rsplit('/', 1)[-1])

    cmd = ['wget', d['url'], '-P', folder_dir]
    subprocess.call(cmd)
