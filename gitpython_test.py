# -*- coding: utf-8 -*-
from git import *
import time
import re
import os
from datetime import date

one_day = 60 * 60 * 24

git_repo = "https://github.com/kazuhirosaji/make_release_mail_format.git"
local_path = "/Users/saji/release_reports/" + date.today().strftime("%y%m%d")
os.mkdir(local_path)

Repo.clone_from(git_repo, "/Users/saji/release_reports")


def is_deploy_log(message):
    if (message.find("into \'master\'") > 0):
        return True
    else:
        return False

def get_title(message):
    disp_msg = ""
    for msg in message.split("\n"):
        if (msg.find("RR") > 0):
            msg = msg.replace("[RR]", "")
            msg = re.sub("(\[*[0-9]*/*[0-9]*\])", "", msg)
            msg = msg.strip()
            disp_msg = msg
    return disp_msg

repo = Repo("/Users/saji/release_reports")
for item in repo.iter_commits('master', max_count=10):
    past_date = (int)(time.time() - item.committed_date) / one_day
    if (past_date < 10):
        if (is_deploy_log(item.message)):
            print(item.author)
            print(time.strftime("%Y %m %d", time.gmtime(item.committed_date)))
            print(get_title(item.message))
            print("\n")
    else:
        break




