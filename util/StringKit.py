#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import sys
reload(sys)

class StringKit(object):

    def __init__(self, param):
        self.param = param

    def underline_character_to_camel(self):
        """
        下划线字符转驼峰字符
        """
        camel_character = ""
        new_string = self.param.split("_")
        for i in range(len(new_string)):
            if(i > 0):
                camel_character += new_string[i].capitalize()
            else:
                camel_character = new_string[i]
        return camel_character

if __name__ == '__main__':
        stringKit = StringKit("bank_card_id")
        print  stringKit.underline_character_to_camel()
