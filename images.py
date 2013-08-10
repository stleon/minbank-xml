#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  images.py
#  
#  Copyright 2013 stleon <leonst998@gmail.com>
#  
#

import base64
import re
import sys

def find_replace(pat, text, ext):
        # если совпадений не будет, то выскачит ошибка
        match = re.search(pat, text)
        if match: 
                #print match.group(1)
                # match.group(1) - нужный нам айдишник фото. 
                try:
                        with open("img/"+match.group(1)+"."+ext, "rb") as image_file:
                                # открыли картинку, сделали магию
                                encoded_string = base64.b64encode(image_file.read()) 
                except IOError:
                        sys.exit('Photo '+match.group(1)+'.'+ext+' doesnt exist!!!')    
                # заменяем айдишник на строку
                text =  text.replace(match.group(1), encoded_string)
        return text

def main():
        source = raw_input('Source (without .xml): ')
        ext = raw_input('Extension (png, jfif...): ')
        # открываем файл для чтения и записи
        try:
                my_xml = open(source+'.xml', "r")
                my_new_xml = open(source+'_new.xml', "w")
        except IOError:
                sys.exit('File '+source+'.xml doesnt exist!!!')
        # ищем по файлу нужные нам строки
        for line in my_xml:
                new_text = find_replace('<PORTRAIT>(\d+)</PORTRAIT>', line, ext)
                # пишем каждую строчку в новый файл
                my_new_xml.write(new_text)
        # закрываем файл
        my_xml.close()
        my_new_xml.close()

if __name__=='__main__':
        main()
