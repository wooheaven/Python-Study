import glob
from collections import defaultdict


def modify_idx(size, idx):
    idx_str = str(idx + 1)
    while size > len(idx_str):
        idx_str = '0' + idx_str
    return idx_str


pwd_folder_list = glob.glob('./*/')
pwd_folder_dict = defaultdict(lambda: defaultdict(str))

for idx, sub_folder in enumerate(pwd_folder_list):
    tmp_folder = sub_folder[sub_folder.index('_')+1:-1]
    pwd_folder_dict[tmp_folder]['old'] = sub_folder
    pwd_folder_list[idx] = tmp_folder

pwd_folder_list.sort()
size = int(len(pwd_folder_list) / 10) + 1

for idx, tmp_folder in enumerate(pwd_folder_list):
    pwd_folder_dict[tmp_folder]['new'] = modify_idx(size, idx) + '_' + tmp_folder

with open('git-move.sh', 'w') as f:
    for key in pwd_folder_dict.keys():
        f.writelines('git mv ' + pwd_folder_dict[key]['old'] + ' ' + pwd_folder_dict[key]['new'] + '\n')
