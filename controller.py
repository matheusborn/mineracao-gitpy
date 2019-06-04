import os
import sys
import operator
from git import Repo
from git import diff
from functools import reduce
import json

reload(sys)
sys.setdefaultencoding('utf-8')

PATH = './linux'

repo = Repo(PATH)
assert not repo.bare
commits = list(repo.iter_commits('HEAD'))


def run():

    for index in range(len(commits)-1):
        diff_index = commits[index+1].diff(commits[index].hexsha, create_patch=True,
                                           ignore_blank_lines=True, ignore_space_at_eol=True, diff_filter='cr')
        count = 0
        count2 = 0
        try:
            df = str(reduce(lambda x, y: str(x)+str(y), diff_index))
            df_lines = df.splitlines()
            for line in df_lines:
                try:
                    if line[0] == '+':
                        count += 1
                    if line[0] == '-' and line[1] != '-':
                        count -= 1
                except:
                    pass

            if count == 0:
                for line in df_lines:
                    if 'lhs:' in line:
                        #print('count = ' + str(count))
                        #print('count2 = ' + str(count2))

                        if count > count2:
                            print('aumentou complexidade')
                            print(index)
                        elif count2 > count:
                            print('diminuiu complexidade')
                            pass
                        else:
                            #print('manteve complexidade')
                            pass
                        count = 0
                        count2 = 0
                    try:
                        if line[0] == '+' and '{' in line:
                            count += 1
                        elif line[0] == '-' and line[1] != '-' and '{' in line:
                            count2 += 1
                    except:
                        pass

                #print('count = ' + str(count))
                #print('count2 = ' + str(count2))

                if count > count2:
                    print('aumentou complexidade')
                    print(index)
                elif count2 > count:
                    #print('diminuiu complexidade')
                    pass
                else:
                    #print('manteve complexidade')
                    pass
            else:
                pass
        except:
            pass
