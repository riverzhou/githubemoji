#!/usr/bin/env python3

import os
import json

jsonfilename = 'emojis.json'
testfilename = 'TEST.md'

with open(jsonfilename, 'r', encoding='utf-8') as rf:
    dictEmoji = json.load(rf)

output = '* Emoji TEST  \n\n---\n'
for name in dictEmoji:
    spam = '`:{}:` :{}: '.format(name,name)
    output += spam

with open(testfilename, 'w', encoding='utf-8') as wf:
    wf.write(output)
