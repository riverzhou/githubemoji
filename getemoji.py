#!/usr/bin/env python3

import os
import json
import requests
from time import sleep

jsonfilename = 'emojis.json'
prefix = 'https://github.githubassets.com/images/icons/'

listurl = []

with open('emojis.json', 'r', encoding='utf-8') as rf:
    dictEmoji = json.load(rf)

for name in dictEmoji:
    listurl.append(dictEmoji[name])

listurl.reverse()

while True:
    if len(listurl) == 0:
        break
    url = listurl.pop()
    path = url[len(prefix):].split('?')[0]
    dirname, filename = path.rsplit('/', 1)
    print(url)
    # print(path)
    # print(dirname)
    # print(filename)
    try:
        c = requests.get(url).content
    except Exception as err:
        print(err)
        listurl.insert(0,url)
        sleep(1)
        continue

    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(path, 'wb') as wf:
        wf.write(c)
