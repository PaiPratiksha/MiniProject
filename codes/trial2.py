import csv;
import numpy as np;
import matplotlib.pyplot as plt;
import ast

# csv_file = csv.reader(open('LCR.powerspec.csv'), delimiter = ',')
csv_file = np.array(list(csv.reader(open("data.csv"), delimiter=",")))
# csv_file = np.loadtxt(open("LCR.powerspec.csv"), delimiter=",")
m, n = csv_file.shape;
# m_x , n_x = (-1, -1)
# for row in csv_file:
# 	m_x = m_x +1;
# 	for i in row:
# 		n_x = n_x + 1
# 		data[m_x][n_x] = float(i);
# 		if(n_x >= n):
# 			n_x = -1;


print(csv_file.dtype)
		# try:
		# 	i =  int(i)
		# except ValueError:
		# 	i =  float(i)


# my_data = np.array(csv_file);
# print(data.dtype)


# m, n = csv_file.shape;
# print(m, n)
# plt.plot(np.arange(m), csv_file.T[0])
# plt.show()



# import csv
# import numpy
# reader = csv.reader(open("test.csv", "rb"), delimiter=",")
# x = list(reader)
# result = numpy.array(x).astype("float")

# numpy.loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=1)

# result = numpy.array(list(csv.reader(open("LCR.powerspec.csv"), delimiter=","))).astype("float")

# def read_lines():
#     with open('testdata.csv', 'rU') as data:
#         reader = csv.reader(data)
#         for row in reader:
#             yield [ float(i) for i in row ]









# for i in read_lines():
#     print(i)

# # to get a list, instead of a generator, use
# xy = list(read_lines())




##this is the way to do the whole coding for wavelet transform 
"""
import pywt
import atplotlib.pyplot as plt
a = np.array([1, 2, 3 ,4 ,5 ])
(x, y) = pywt.dwt(a, 'db8')

plt.scatter(np.arange(np.size(x) , x))
plt.show()



"""

