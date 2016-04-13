import sys
import csv
from svmutil import *
from collections import defaultdict
import numpy as np
import os

complete_csv = open("complete.csv","w")

# first file:
f = open("datatest1.csv","r")
for line in f:
    complete_csv.write(line)

# now the rest:
f = open("datatest2.csv","r")
f.next() # skip the header
for line in f:
    complete_csv.write(line)

f = open("datatest3.csv","r")
f.next() # skip the header
for line in f:
    complete_csv.write(line)
complete_csv.close()

def construct_line(label, line):
    new_line = []
    if float(label) == 0.0:
        label = "0"
    new_line.append(label)

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            item = -1.0
        new_item = "%s:%s" % (i + 1, item)
        new_line.append(new_item)
    new_line = " ".join(new_line)
    new_line += "\n"
    return new_line

def csv2libsvm(csvfile,libsvmfile,labels):
    label_index = labels #number of properties

    reader = csv.reader(csvfile)
    next(reader, None) #ignore headers

    for line in reader:
        if label_index == -1:
            label = '1'
        else:
            label = line.pop(label_index)

        new_line = construct_line(label, line)
        libsvmfile.write(new_line)


complete_csv = open("complete.csv","r")
complete_data = open("complete.data","w")

csv2libsvm(complete_csv,complete_data,5)

test_csv = open("test.csv","r")
test_data = open("test.data","w")

csv2libsvm(test_csv,test_data,-1)

y, x = svm_read_problem("complete.data")
j,i = svm_read_problem("test.data")

prob = svm_problem(y, x)
param = svm_parameter('-s 0 -t 2 -c 2') #find exact params for our problem
m = svm_train(prob, param)

p_labels, p_acc, p_vals = svm_predict(j, i, m)

(ACC, MSE, SCC) = evaluations(j, p_labels)

#print p_labels, ACC

print len(p_labels)

list = []

for i in p_labels:
    if i==1:
        list.append("present")
    else:
        list.append("absent")


result = open("result.csv","wb")
wr = csv.writer(result, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

for data in list:
    result.write(data+"\n")
