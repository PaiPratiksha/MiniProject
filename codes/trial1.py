import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mp  
import csv 
import pandas as pd 
from pandas import ExcelWriter as ew;
from pandas import ExcelFile as ef;
import math

a = np.array(pd.read_excel('data.xlsx'))
# b = np.array(a)
m, n = np.shape(a)
print(a.dtype)
print(m, n)

# plt.plot(np.arange(0, m), a.T[0], 'ro')
# # plt.axis([0, m+1, ])
# # plt.show()
# a = a[~np.isnan(a)]
a = np.nan_to_num(a)
print(a[0])
print('\n')
print(a[1])
print(max(a[0]))

plt.plot(np.arange(0, m), a.T[1], linewidth = 0.5 )
# plt.axis([0, m+1, ])
plt.show()




# plt.scatter(np.arange(0, m), a.T[1])
# plt.show()




# from openpyxl import load_workbook
# import numpy as np
 
# #read  from excel file
# wb = load_workbook('python_excel_read.xlsx')
# sheet_1 = wb.get_sheet_by_name('Sheet1')
 
# x = np.zeros(sheet_1.max_row)
# y = np.zeros(sheet_1.max_row)
 
# for i in range(0,sheet_1.max_row):
#     x[i]=sheet_1.cell(row=i+1, column=1).value
#     y[i]=sheet_1.cell(row=i+1, column=2).value
 
# print x
# print y