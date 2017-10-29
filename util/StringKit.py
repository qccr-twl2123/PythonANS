#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import sys
reload(sys)

class StringKit(object):

    def __init__(self, str):
        self.__str = str

    def underline_character_to_camel(str):
        """
        下划线字符转驼峰字符
        """
        camel_character = ""
        for i in range(len(str)):
            if(i > 0):
                camel_character += str[i].capitalize()
            else:
                camel_character = str[i]
        return camel_character

if __name__ == '__main__':
        stringKit = StringKit("bank_card_id")
        print  stringKit.underline_character_to_camel()
