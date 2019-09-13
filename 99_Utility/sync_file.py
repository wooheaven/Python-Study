import subprocess
import argparse
import hashlib
from collections import defaultdict
import shutil


def get_hash(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter Original file path")
    parser.add_argument('FILE_PATH', type=str)
    args = parser.parse_args()
    file_path = args.FILE_PATH
    file_name = file_path[len(file_path) - file_path[::-1].index('/'):]
    file_md5 = get_hash(file_path)

    cmd = 'find `pwd` -type f -name ' + str(file_name) + ' -exec echo {} \;'
    path_str = subprocess.check_output(cmd, shell=True)
    path_str = path_str.decode("utf-8")

    path_list = path_str.split('\n')
    path_list = list(filter(lambda x: len(x) > 0, path_list))
    path_list.sort()

    md5_dict = defaultdict()
    for idx, key in enumerate(path_list):
        if file_path in key:
            print(idx, 'original-file-path', key, sep='\t')
        else:
            print(idx, ' compare-file-path', key, sep='\t')
            md5_dict[key] = get_hash(key)
    for idx, key in enumerate(md5_dict):
        if file_md5 == md5_dict.get(key):
            print(idx, '     same md5', key, sep='\t')
        else:
            print(idx, 'different md5', key, sep='\t')
            shutil.copy(file_path, key)
            print(idx, 'copy', sep='\t')
