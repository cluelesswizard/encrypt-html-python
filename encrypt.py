#!/bin/python3.9
#-*- coding: utf-8 -*-

import os, sys, requests, re
from bs4 import BeautifulSoup as bs

"""
Copyright (c) 2020 DestaGans

Author: DestaGans
Team: Black Coder Crush
Tools: Auto Encript Html Script
Source code: https://pastebin.com/wxaYEgAt

Target-Scrap: https://www.smartgb.com/free_encrypthtml.php

"""

# Ni Warna Bro #
bi = '\x1b[34;1m'
cy = '\x1b[36;1m'
i = '\x1b[32;1m'
ku = '\x1b[33;1m'
lbi = '\x1b[94;1m'
lcy = '\x1b[95;1m'
lpur = '\x1b[95;1m'
me = '\x1b[31;1m'
pu = '\x1b[37;1m'
pur = '\x1b[35;1m'
reset = '\x1b[0;1m'
bekrond = '\x1b[7m'
#--------------#

os.system('clear')
print('''{}
 _   _ _             _
| | | | |           | |      {}[ {}HTML ENCRIPTED {}]{}
| |_| | |_ _ __ ___ | |
|  _  | __| '_ ` _ \| | {}Author{}: {}DestaGans / Mr.Đ`HACK{}
| | | | |_| | | | | | |   {}Team{}: {}Black Coder Crush{}
\_| |_/\__|_| |_| |_|_|
'''.format(bi,me,pu,me,bi,cy,me,pu,bi,cy,me,pu,bi))

sc = input('{}[{}*{}] EnterHtmlScript{}: {}'.format(pu,i,pu,me,cy))
try:
        files = open(sc,'r').read()
except:
        time.sleep(1)
        print('{}[{}!{}] File Not Found{}!{}'.format(pu,me,pu,me,reset))
        sys.exit()

key = re.findall('<input type="hidden" name="ch" value="(.*?)">',requests.get('https://www.smartgb.com/free_encrypthtml.php').text)

data = {
        'h': files,
        's':'extented',
        'ch': key,
        'Skicka': 'Encrypt HTML'
}
try:
        res = requests.post('https://www.smartgb.com/free_encrypthtml.php?do=crypt',data=data).text
        b = bs(res, "html.parser")
        result = b.find('textarea').text
except:
        print('{}[{}!{}] Exception{}!'.format(pu,me,pu,me))
open(sc.replace('.html','_enc.html'),'w').write('<!-- EncryptedBy: DestaGans -->'+result)

print('{}[{}!{}] Result{}: {}'.format(pu,i,pu,me,cy)+sc.replace('.html','_enc.html'))
print(reset)

sys.exit()