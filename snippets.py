'''
import csv
with open('apan01.csv', newline='') as csvfile:
   list = csv.reader(csvfile, delimiter=',')
   for row in list:
      print(', '.join(row))
      
'''

'''
for i in range(len(data)):
    print data[i][0] #this alone will print all the computer names
    for j in range(len(data[i])) #Trying to run another for loop to print the usernames
        print data[i][j]
'''

'''
#opens File 1
with open('apan01.csv', 'r') as f:  
    reader = csv.reader(f)
    data_a = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

#opens File 2
with open('bpan01.csv', 'r') as f:
    reader = csv.reader(f)
    data_b = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

if data_a[1][0] in data_b:
    print(data_a[1][0], data_b, "found one!")
'''

'''
for i in range(len(data_a)):
   #if data_a
   #print(data_a[i])
   print(data_a[i][0])
'''
'''
for i in range(len(data_b)):
   print(data_b[i]))
'''   
'''
for i in (data_a):
    #print data[i][0] #this alone will print all the computer names
    for j in (data_b): #Trying to run another for loop to print the usernames
        if data_a[0] or data_a[1] == data_b[0] or data_b[1]:
            print(data_a)
'''
'''
#this one works well for matching the entire list/line
with open(input_file1, 'r') as t1:
    fileone = set(t1)

with open(input_file2, 'r') as t2, open(output_path, 'w') as outFile:
    for line in t2:
        if line in fileone:
            print(line)
            #outFile.write(line)

'''

file_a = open("apan01.csv","r")
file_b = open("bpan01.csv","r")

'''
dict_a = {}
dict_b = {}

for line_a in file_a:
    line_a.strip()
    dict_a[(line_a.split(","))[0]] = line_a
    for line_b in file_b:
        line_b.strip()
        dict_b[(line_b.split(","))[0]] = line_b

        print(dict_a[dict.keys])
        if dict_a.keys in dict_b:
            print(line_a, "Found one!", line_b)
'''


file_a.close()
file_b.close()