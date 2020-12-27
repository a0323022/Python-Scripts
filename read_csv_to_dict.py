import csv 
import sys #used for passing in the argument
#file_name = sys.argv[1] #filename is argument 1

input_file1 = "apan01.csv"
input_file2 = "bpan01.csv"
output_path = "out.csv"

'''
#this one works well for matching the entire list/line
with open(input_file1, 'r') as t1:
    fileone = set(t1)

with open(input_file2, 'r') as t2, open(output_path, 'w') as outFile:
    for line in t2:
        if line in fileone:
            print(type(line))
            #outFile.write(line)
'''
with open('bpan01.csv', 'r') as updates_fh:
    updates = {tuple(r[:2]): r for r in csv.reader(updates_fh)}

with open('apan01.csv', 'r') as infh, open('out.csv', 'w') as outfh:
    writer = csv.writer(outfh)
    writer.writerows((updates.get(tuple(r[:2]), r) for r in csv.reader(infh)))

#
# update indices, then search through lines of b or a.

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

#f.close() #close the csv





