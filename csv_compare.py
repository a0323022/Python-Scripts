import csv
import sys #used for passing in the argument

#file_name = sys.argv[1] #filename is argument 1

input_file1 = input("Enter First File Name")
input_file2 = input("Enter Second File Name")
output_path = input("Enter output file, if any")




'''
with open('a_netdevtype_122220.csv','r') as apan01:

with open('b_netdevtype_122220.csv','r') as bpan01:

    b_list = bpan01.readlines()[1:]
    a_list = apan01.readlines()[1:]

    print(a_list[1][0])
    print(b_list[1][1])
'''
'''
     for Name in b_list:
        if Name in a_list:
            print(a_list[1], "Found in master file")
        else:
            print(a_list[0], "Not found in master file")
'''

'''
#opens File 1

with open('a_netdevtype_122220.csv', 'r') as f: 
    reader = csv.reader(f)
    for row in csv.reader(f, delimiter=','): #reads csv into a list of lists
        data_a = []
        print(data_a)

#print(data_a[1][0:3])

#opens File 2

with open('b_netdevtype_122220.csv', 'r') as f:
    reader = csv.reader(f)

    data_b = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

    #print(data_a[-1][0:3])

    for i in range(len(data_a)):
        for j in range(len(data_b)):
            if data_a[i]in data_b[j]:
                print(data_a[i], data_b[j], "found one!")
'''

'''

import csv

f = open('a_netdevtype_122220.csv', "r")

for x in f:
    print(f.readline())

f.close()

    spamreader = csv.reader(csvfile)
for row in spamreader:
    print(spamreader)

#csvfile.close()

a = open("a_netdevtype_122220.csv", "r")
b = open("b_netdevtype_122220.csv", "r")

a_list = []
b_list = []

for x in a:
    print(type(a))
    print(type(b))
    a = a.readline()
    b = b.readline()
    a_dict = {a}

    print(a)
    print(type(a_dict))
    print(a_dict)
    print(b)
    print(type(a))
    print(type(b))

a.close()
b.close()

'''