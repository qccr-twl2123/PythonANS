#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import sys
reload(sys)


class FileUtil(object):

      def __init__(self,fileName):
          self.__fileName= fileName

      def convertFileToDict(self):
          file = open(self.__fileName)
          key_list = []
          values_list = []
          for  line in  file.readlines():
              key_list.append(self.underline_character_to_camel(line.split()[0].split("_")))
              values_list.append(line.split()[1])

          key_value = dict(zip(key_list,values_list))
          return key_value

      def underline_character_to_camel(self,character):
            """
            下划线字符转驼峰字符
            """
            camel_character =""
            for i in range(len(character)):
                if(i > 0):
                    camel_character += character[i].capitalize()
                else:
                    camel_character= character[i]
            return camel_character

if __name__ == '__main__':
       fileUtil =  FileUtil("demo.text")
       print fileUtil.convertFileToDict()
