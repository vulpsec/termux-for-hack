#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

import os
import time
import sys

Mor = '\033[95m'
Cyan = '\033[96m'
KoyuMavi = '\033[1;34m'
Mavi = '\033[94m'
Yeşil = '\033[92m'
Sarı = '\033[93m'
Kırmızı = '\033[91m'
Kalın = '\033[1m'
AltıÇizili = '\033[4m'
Bitir = '\033[0m'
Beyaz ='\033[1;37m'

import os
import time

print('ROOT OLARAK ÇALIŞTIRINIZ!')
time.sleep(2)

def yükle():
    os.system('''termux-setup-storage;apt update && apt upgrade;pkg update && pkg upgrade;pkg install git ;pkg install python ;pkg install python2 ;pkg install python3  ;pkg install wget ;pkg install curl ;pkg install ruby ;pkg install php ;pkg install pip ;pkg install pip2 ;pkg install perl ;pkg install nmap ;pkg;install openssh ;pkg install openssl  ;pip install colorama ;''')
    print(f'{Yeşil}İşlem Tamamlamdı.')
    int = input(f'{Beyaz}Bütün Python Kütüphanelerini İndirmek İster Misiniz Y/n: {Yeşil}')
    if int == 'Y' or int == 'y':
        os.system('git clone https://github.com/morbius-os/all-pip-installer') #düzenlenecek
        os.system('cd all-pip-installer')
        os.system('python3 all-pip.py')

yükle()