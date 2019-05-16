import glob
import os


def modify_idx(size, idx):
    idx_str = str(idx + 1)
    while size > len(idx_str):
        idx_str = '0' + idx_str
    return idx_str


pwd_folder_list = glob.glob('*/')

for idx, folder in enumerate(pwd_folder_list):
    tmp_folder = folder[folder.index('_') + 1:-1]
    pwd_folder_list[idx] = [folder, tmp_folder]

pwd_folder_list.sort(key=lambda x: (x[1].lower(), x[0].lower()))

size = len(str(len(pwd_folder_list)))
if size == 1:
    size = size + 1

for idx, sub_list in enumerate(pwd_folder_list):
    new_folder = modify_idx(size, idx) + '_' + sub_list[1]
    pwd_folder_list[idx] = [sub_list[0], sub_list[1], new_folder]

with open('git-move.sh', 'w') as f:
    for sub_list in pwd_folder_list:
        pre_str = 'git mv '
        if sub_list[0][:-1] == sub_list[2]:
            pre_str = "# " + pre_str
        f.writelines(pre_str + sub_list[0] + ' ' + sub_list[2] + '\n')

os.chmod('git-move.sh', 0o755)
