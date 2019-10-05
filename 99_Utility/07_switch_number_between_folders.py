import argparse
import os
from collections import defaultdict
import re
import shutil


class Rename():
    def __init__(self, path_a, path_b):
        self.path_a = path_a[0:-1] if path_a.endswith('/') else path_a
        self.path_b = path_b[0:-1] if path_b.endswith('/') else path_b
        self.path_dict = defaultdict()

    def do(self):
        # check path
        for path in [self.path_a, self.path_b]:
            if not os.path.exists(path):
                raise NameError("Path is not existed : ", path)
            if not os.path.isdir(path):
                raise NotADirectoryError("Path is existed but not a directory : ", path)
            regex = re.compile(r'\d\d\_')
            match_obj = re.search(regex, path[0:3])
            if len(match_obj.group()) != 3:
                raise NameError("Path is not started by number : ", path)

        # create path_dict
        self.path_dict['path_a'] = {'old_path': self.path_a, 'new_path': ''}
        self.path_dict['path_b'] = {'old_path': self.path_b, 'new_path': ''}

        # new_path
        self.update_new_path('path_a', 'path_b')
        self.update_new_path('path_b', 'path_a')

        # move
        for key in self.path_dict.keys():
            tmp_dict = self.path_dict.get(key)
            tmp_old_path = tmp_dict.get('old_path')
            tmp_new_path = tmp_dict.get('new_path')
            shutil.move(tmp_old_path, tmp_new_path)

    def update_new_path(self, path_target, path_reference):
        tmp_path = self.path_dict[path_reference]['old_path'][0:3] + self.path_dict[path_target]['old_path'][3:]
        if os.path.exists(tmp_path):
            raise NameError('new_path is already existed : ', tmp_path)
        self.path_dict[path_target]['new_path'] = tmp_path


if __name__ == "__main__":
    p = argparse.ArgumentParser("1st_path, 2nd_path")
    p.add_argument('path_1st', type=str, metavar='1st_folder_path')
    p.add_argument('path_2nd', type=str, metavar='2nd_folder_path')

    args = p.parse_args()
    path_1st = args.path_1st
    path_2nd = args.path_2nd

    r = Rename(path_1st, path_2nd)
    r.do()