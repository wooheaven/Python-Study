import os
import glob
import argparse
from collections import defaultdict
import re
import hashlib
import shutil


class PySync():
    def __init__(self, path_a, path_b, mode):
        self.path_a = path_a
        self.path_b = path_b

        self.check_path()
        # Find files recursively
        self.dict_a = self.get_files_dict(self.path_a)
        self.dict_b = self.get_files_dict(self.path_b)
        # get md5
        self.update_files_with_md5(self.dict_a)
        self.update_files_with_md5(self.dict_b)

        if mode == 'sync':
            self.sync_a_from_b()
        elif mode == 'delete':
            self.delete_a_from_b()

    def sync_a_from_b(self):
        for key, dict in self.dict_b.items():
            src = dict['Parent_Path'] + key
            dst = self.path_a + key
            if key in self.dict_a.keys():
                if os.path.isfile(src):
                    md5_a = dict['md5']
                    md5_b = self.dict_a.get(key)['md5']
                    if md5_a != md5_b:
                        self.copy_file(src, dst)
            else:
                if os.path.isfile(src):
                    self.copy_file(src, dst)
                elif os.path.isdir(src):
                    os.mkdir(dst)

    def delete_a_from_b(self):
        for key, dict in self.dict_b.items():
            src = dict['Parent_Path'] + key
            if key in self.dict_a.keys():
                if os.path.isfile(src):
                    md5_a = dict['md5']
                    md5_b = self.dict_a.get(key)['md5']
                    if md5_a == md5_b:
                        os.remove(self.path_a + key)

    def check_path(self):
        # check path
        if not os.path.exists(self.path_a):
            raise NameError("Path_A is not existed")
        if not os.path.exists(self.path_b):
            raise NameError("Path_B is not existed")
        if not os.path.isdir(self.path_a):
            raise NameError("Path_A is not directory")
        if not os.path.isdir(self.path_b):
            raise NameError("Path_B is not directory")
        # path to abspath
        self.path_a = os.path.abspath(self.path_a)
        self.path_b = os.path.abspath(self.path_b)
        # add / to path
        self.path_a = self.add_slash(self.path_a)
        self.path_b = self.add_slash(self.path_b)

    def add_slash(self, path_str):
        if not path_str[-1][0] == '/':
            path_str += '/'
        return path_str

    def get_files_dict(self, path):
        files_dict = defaultdict(lambda: defaultdict(str))
        for file_path in glob.glob(path + '**', recursive=True):
            if len(file_path) - len(path) > 0:
                tmp_dict = defaultdict()
                tmp_dict['Parent_Path'] = path
                files_dict[re.sub(path, '', file_path, count=1)] = tmp_dict
        return files_dict

    def get_md5(self, path, blocksize=65536):
        afile = open(path, 'rb')
        hasher = hashlib.md5()
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        afile.close()
        return hasher.hexdigest()

    def update_files_with_md5(self, files_dict):
        for key, dict in files_dict.items():
            if os.path.isfile(dict['Parent_Path']+key):
                dict['md5'] = self.get_md5(dict['Parent_Path'] + key)

    def copy_file(self, src, dst):
        shutil.copy(src, dst)


if __name__ == "__main__":
    p = argparse.ArgumentParser("Sync A from B")
    p.add_argument('PATH_A', type=str, metavar='Path_A')
    p.add_argument('PATH_B', type=str, metavar='Path_B')
    p.add_argument('MODE', type=str, metavar='Mode')

    args = p.parse_args()
    path_a = args.PATH_A
    path_b = args.PATH_B
    mode =  args.MODE

    r = PySync(path_a, path_b, mode)