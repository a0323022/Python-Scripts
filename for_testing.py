import csv

f_a = open('apan01.csv', "r")

f_b = open('bpan01.csv', "r")

list_a = list((csv.reader(f_a)))
list_b = list((csv.reader(f_b)))

for i in list_a:
    for j in list_b:
        if i[0] in j:
            print("found one match in B", i[0])

f_a.close()
f_b.close()
