import csv

a = open("apan01.csv", "r")
b = open("bpan01.csv", "r")

for x in a:
    a_list = a.readlines()
    print(a_list[0])
    print(type(a_list))
    


a.close()
b.close()
