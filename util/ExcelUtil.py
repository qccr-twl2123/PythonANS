# -*- coding: utf-8 -*-
import xlrd
import csv
from os import sys
import pandas as pd
import random
import numpy as np


def csv_from_excel(excel_file):
    workbook = xlrd.open_workbook(excel_file)
    all_worksheets = workbook.sheet_names()
    for worksheet_name in all_worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        your_csv_file = open(''.join([worksheet_name,'.csv']), 'wb')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)


    for rownum in xrange(worksheet.nrows):
        wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])
        your_csv_file.close()


if __name__ == "__main__":
    # data_xls = pd.read_excel('2016012017255038120.xls', 'Sheet1', index_col=None)
    # data_xls.to_csv('2015.csv', encoding='utf-8')
    print np.random.choice(['JGood', 'is', 'a', 'handsome', 'boy'],size=10)

