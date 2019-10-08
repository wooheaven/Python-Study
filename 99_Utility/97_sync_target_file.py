import argparse
import os
from collections import defaultdict
import json
import subprocess


class Sync():
    def __init__(self, parent, path):
        self.parent = parent
        self.path = path

    def do(self):
        # check file
        self.check_parent_file(self.parent, self.path)

        # path_dict
        path_dict = self.get_path_dict(self.parent, self.path)

        # find with md5sum
        self.find_with_md5sum(path_dict)

        # find with rsync
        self.find_with_rsync(path_dict)

        # find with md5sum
        self.find_with_md5sum(path_dict)

    def check_parent_file(self, parent, path):
        if not os.path.exists(parent):
            raise FileNotFoundError('Folder is not existed : ', parent)
        if not os.path.isdir(parent):
            raise NameError('Path is not a folder : ', parent)
        if not os.path.exists(path):
            raise FileNotFoundError('File is not existed : ', path)
        if not os.path.isfile(path):
            raise NameError('Path is not a file : ', path)

    def get_path_dict(self, parent, path):
        path_dict = defaultdict(str)
        path_dict['parent'] = os.path.abspath(self.parent)
        path_dict['path'] = os.path.abspath(self.path)
        path_dict['file'] = os.path.basename(self.path)
        print(json.dumps(path_dict, indent=4))
        return path_dict

    def find_with_md5sum(self, path_dict):
        cmd = 'find ' + path_dict['parent']
        cmd += ' -type f'
        cmd += ' -name ' + path_dict['file']
        cmd += ' -exec md5sum {} \\;'
        print('\n' + cmd)
        md5sum_list = subprocess.check_output(
            args=[cmd],
            universal_newlines=True, shell=True)
        print(md5sum_list)

    def find_with_rsync(self, path_dict):
        cmd = 'find ' + path_dict['parent']
        cmd += ' -type f'
        cmd += ' -name ' + path_dict['file']
        cmd += ' ! -path ' + path_dict['path']
        cmd += ' -exec rsync ' + path_dict['path'] + ' {} \\;'
        print(cmd)
        subprocess.call(
            args=[cmd],
            universal_newlines=True, shell=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser('Path')
    p.add_argument('PARENT', type=str, metavar='Parent Path of Target File')
    p.add_argument('PATH', type=str, metavar='Path of Target File')
    args = p.parse_args()

    s = Sync(args.PARENT, args.PATH)
    s.do()