import os
import sys
import operator
from git import Repo
from git import diff
from functools import reduce
import json

reload(sys)
sys.setdefaultencoding('utf-8')

PATH = './EventBus'

repo = Repo(PATH)
assert not repo.bare
commits = list(repo.iter_commits('HEAD'))


def run():

    for index in range(len(commits)-1):
        commit = commits[index]
        diff_index = commits[index+1].diff(commits[index].hexsha, create_patch=True,
                                           ignore_blank_lines=True, ignore_space_at_eol=True, diff_filter='cr')
        try:
            df = str(reduce(lambda x, y: str(x)+str(y), diff_index))
            df_lines = df.splitlines()
            count = 0
            for line in df_lines:
            # print(line)
                try:
                    if line[0] == '+' and line[1] != '-':
                        count += 1
                    if line[0] == '-' and line[1] != '-':
                        count -= 1
                except:
                    pass
            if count == 0:
                print('foi ' + str(commit.hexsha))
            else:
                pass
        except:
            pass