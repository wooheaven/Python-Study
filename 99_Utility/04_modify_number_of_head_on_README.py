import os
import glob
import re
import argparse


class Rename():
    def __init__(self, field_num, start_num, end_num):
        self.field_num = field_num
        self.field_size = 1
        self.start_num = start_num
        self.end_num = end_num

    def do(self):
        cwd = os.getcwd()
        if cwd.endswith('99_Utility'):
            readme_path = glob.glob(cwd + '/../README.md')
        elif cwd.endswith('-Study'):
            readme_path = glob.glob(cwd + '/README.md')
            print(readme_path)
        else:
            raise NotImplementedError

        if len(readme_path) == 1:
            head_list = []
            skip_old = False
            lines = []
            with open(file=readme_path[0], mode='r') as fr:
                lines = fr.read().splitlines()
                for i, line in enumerate(lines):
                    if skip_old:
                        break
                    line = re.sub(r'╠', '', line)
                    line = re.sub(r'═', '', line)
                    line = re.sub(r'║ ', '', line)
                    line = re.sub(r'╚', '', line)
                    line = re.sub(r'- ', '', line)
                    line = re.sub(r'&nbsp; ', '', line)
                    line = re.sub(r'[a-zA-Z]', '', line)
                    line = re.sub(r'[_]', '', line)
                    line = re.sub(r'\s{1,}$', '', line)
                    if len(line.split(' ')) < 2 or i >= self.end_num:
                        skip_old = True
                        continue
                    full_head = line.split(' ')[0]
                    short_head = line.split(' ')[1]
                    head_list.append([full_head, short_head])
                    print('  read head', i+1, 'full_head', full_head, 'short_head', short_head, line, sep='\t')
                for i, head in enumerate(head_list):
                    if self.start_num <= i+1 <= self.end_num:
                        for j, tmp in enumerate(head[0].split('.')):
                            if j+1 == self.field_num and len(str(int(tmp)+1)) > self.field_size:
                                self.field_size += 1
                for i, line in enumerate(lines):
                    if self.start_num <= i+1 <= self.end_num:
                        full_head = head_list[i][0]
                        new_full_head = ''
                        for j, tmp in enumerate(full_head.split('.')):
                            if j+1 == self.field_num:
                                tmp = self.string_with_prefix(str(int(tmp)+1))
                            new_full_head += tmp + '.'
                        new_full_head = new_full_head[:-1]

                        short_head = head_list[i][1]
                        new_short_head = ''
                        for k, tmp in enumerate(short_head.split('.')):
                            if k+1 == self.field_num:
                                tmp = str(int(tmp) + 1)
                            new_short_head += tmp + '.'
                        new_short_head = new_short_head[:-1]

                        line = re.sub(full_head, new_full_head, line, count=1)
                        line = re.sub(short_head, new_short_head, line, count=1)
                        lines[i] = line
                        print('change head', i+1, line, sep='\t')
            with open(file=readme_path[0], mode='w') as fw:
                for line in lines:
                    fw.write("%s\n" % line)
        else:
            print(cwd, readme_path)
            raise NotImplementedError

    def string_with_prefix(self, tmp):
        while len(tmp) < self.field_size:
            tmp = '0' + tmp
        return tmp


if __name__ == "__main__":
    p = argparse.ArgumentParser("modify number of head on READMD.md")
    p.add_argument('FILED_NUM', type=int, metavar='Field Number')
    p.add_argument('START_NUM', type=int, metavar='Start Number')
    p.add_argument('END_NUM', type=int, metavar='End Number')
    args = p.parse_args()
    filed_num = args.FILED_NUM
    start_num = args.START_NUM
    end_num = args.END_NUM
    r = Rename(filed_num, start_num, end_num)
    r.do()

