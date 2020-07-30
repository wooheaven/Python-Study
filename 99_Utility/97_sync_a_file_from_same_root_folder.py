import argparse
import os
from collections import defaultdict
import json
import subprocess


class Sync():
    def __init__(self, p1, p2):
        self.common_root_folder = p1
        self.reference_file = p2

    def do(self):
        # check file
        self.check_parent_file(self.common_root_folder, self.reference_file)

        # path_dict
        path_dict = self.get_path_dict(self.common_root_folder, self.reference_file)

        # find with md5sum
        self.find_with_md5sum(path_dict)

        # find with rsync
        self.find_with_rsync(path_dict)

        # find with md5sum
        self.find_with_md5sum(path_dict)

    def check_parent_file(self, p1, p2):
        if not os.path.exists(p1):
            raise FileNotFoundError('Folder is not existed : ', p1)
        if not os.path.isdir(p1):
            raise NameError('Path is not a folder : ', p1)
        if not os.path.exists(p2):
            raise FileNotFoundError('File is not existed : ', p2)
        if not os.path.isfile(p2):
            raise NameError('Path is not a file : ', p2)

    def get_path_dict(self, p1, p2):
        path_dict = defaultdict(str)
        path_dict['common_root_folder'] = os.path.abspath(self.common_root_folder)
        path_dict['reference_path'] = os.path.abspath(self.reference_file)
        path_dict['reference_file'] = os.path.basename(self.reference_file)
        print(json.dumps(path_dict, indent=4))
        return path_dict

    def find_with_md5sum(self, path_dict):
        cmd = 'find ' + path_dict['common_root_folder']
        cmd += ' -type d ! -perm -g+r,u+r,o+r -prune -o'
        cmd += ' -type f -name ' + path_dict['reference_file']
        cmd += ' -exec md5sum {} \\;'
        print('\n' + cmd)
        md5sum_list = subprocess.check_output(
            args=[cmd],
            universal_newlines=True, shell=True)
        print(md5sum_list)

    def find_with_rsync(self, path_dict):
        cmd = 'find ' + path_dict['common_root_folder']
        cmd += ' -type d ! -perm -g+r,u+r,o+r -prune -o'
        cmd += ' -type f -name ' + path_dict['reference_file']
        cmd += ' ! -path ' + path_dict['reference_path']
        cmd += ' -exec rsync ' + path_dict['reference_path'] + ' {} \\;'
        print(cmd)
        subprocess.call(
            args=[cmd],
            universal_newlines=True, shell=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser('Path')
    p.add_argument('COMMON_ROOT_FOLDER', type=str, metavar='Common Root Folder')
    p.add_argument('REFERENCE_FILE', type=str, metavar='Reference File')
    args = p.parse_args()

    s = Sync(args.COMMON_ROOT_FOLDER, args.REFERENCE_FILE)
    s.do()