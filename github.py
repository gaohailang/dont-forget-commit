#-*-coding:utf-8-*-

import requests
from sh import git
import time
from datetime import datetime

# from github import Github
# g = Github('ghlndsl@126.com', '<password>')
# u = g.get_user()
# a = u.get_starred()

timestamp = time.time()*1000
url_tpl = 'https://github.com/users/gaohailang/contributions_calendar_data?_=%s'

def get_todaystr():
    i = datetime.now()
    return i.strftime('%Y/%m/%d %H:%M:%S')

def fake_commit():
    x = open('daily-fake-commits.txt','a')
    x.write(get_todaystr()+'\n')
    x.close()
    git('add','.')
    git('commit','-m','fake commit at '+get_todaystr())
    git('push')

def ask_today_commit():
    contributions_json = requests.get(url_tpl % timestamp).json()
    if contributions_json:
        if contributions_json[-1][1]:
            return True
            print 'today gaohailang has already commit!'
    return False

# 1 检查date range内是否有commit
has_contributed = ask_today_commit()

# 2 构建一个commit, 并且提交到github上
if not has_contributed:
    print 'i am going to fake commit'
    try:
        fake_commit()
    except Exception as e:
        print e
        # and email me
