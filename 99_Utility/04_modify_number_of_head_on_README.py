import os
import glob
import re
import argparse


class Rename():
    def __init__(self, start_num, end_num, diff_num):
        self.start_num = start_num
        self.end_num = end_num
        self.diff_num = diff_num

    def do(self):
        # find READMD.md
        cwd = os.getcwd()
        if cwd.endswith('99_Utility'):
            readme_path = glob.glob(cwd + '/../README.md')
        elif cwd.endswith('-Study'):
            readme_path = glob.glob(cwd + '/README.md')
            print(readme_path)
        else:
            raise NameError("Can't find README.md")

        # read lines
        with open(file=readme_path[0], mode='r') as f_in:
            lines = f_in.read().splitlines()

        # read head_numbers
        head_numbers = {}
        for i, line in enumerate(lines):
            if i+1 < self.start_num:
                continue
            if self.end_num <= i:
                continue
            tmp = re.sub(r'░', '', line)
            tmp = re.sub(r'╠', '', tmp)
            tmp = re.sub(r'═', '', tmp)
            tmp = re.sub(r'║ ', '', tmp)
            tmp = re.sub(r'║', '', tmp)
            tmp = re.sub(r'╚', '', tmp)
            tmp = re.sub(r'- ', '', tmp)
            tmp = re.sub(r'&nbsp; ', '', tmp)
            tmp = re.sub(r'[a-zA-Z]', '', tmp)
            tmp = re.sub(r'[_]', '', tmp)
            tmp = re.sub(r'\s{1,}$', '', tmp)
            tmp = tmp.split(' ')[0]
            head_numbers[i] = int(tmp)
            print('line number = ' + str(i+1), 'head_number = ' + tmp, 'original line = ' + line, sep='\t')

        # edit lines
        for key, value in head_numbers.items():
            old_line = lines[key]
            new_line = re.sub(str(value), str(value+self.diff_num), old_line, count=1)
            lines[key] = new_line
            print('\nline number = ' + str(key+1), 'old_line = ' + old_line, sep='\t')
            print('line number = ' + str(key+1), 'new_line = ' + new_line, sep='\t')

        # save lines
        with open(file=readme_path[0], mode='w') as fw:
            for line in lines:
                fw.write("%s\n" % line)


if __name__ == "__main__":
    p = argparse.ArgumentParser("modify number of head on READMD.md")
    p.add_argument('START_NUM', type=int, metavar='Start_Number')
    p.add_argument('END_NUM', type=int, metavar='End_Number')
    p.add_argument('DIFF_NUM', type=int, metavar='Diff_Number')

    args = p.parse_args()
    start_num = args.START_NUM
    end_num = args.END_NUM
    diff_num = args.DIFF_NUM

    r = Rename(start_num, end_num, diff_num)
    r.do()

