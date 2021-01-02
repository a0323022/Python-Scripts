import csv 
import sys #used for passing in the argument
#file_name = sys.argv[1] #filename is argument 1
'''
input_file1 = "apan01.csv"
input_file2 = "bpan01.csv"
output_path = "out.csv"
'''
file_a = open("apan01.csv","r")
file_b = open("bpan01.csv","r")
'''

dict_a = {}
dict_b = {}

for line in file_a:
    line.strip()
    dict_a[(line.split(","))[0]] = line
    print(dict_a[]
file_a.close()
for line in file_b:
    line.strip()
    if 
'''

#opens File 1
reader = csv.reader(file_a)
data_a = csv.reader(file_a, delimiter=',') #reads csv into a list of lists
for line in file_a:
    list_a = 
print(data_a)

'''
#opens File 2
with open('bpan01.csv', 'r') as f:
    reader = csv.reader(f)
    data_b = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists
    #print(data_a[-1][0:3])

    for i in range(len(data_a)):
        for j in range(len(data_b)):
            if data_a[i]in data_b[j]:
                print(data_a[i], data_b[j], "found one!")
'''
'''
with open('apan01.csv', newline='') as csvfile:
   list = csv.reader(csvfile, delimiter=',')
   for row in list:
      print(', '.join(row))
      

for i in range(len(data)):
    print data[i][0] #this alone will print all the computer names
    for j in range(len(data[i])) #Trying to run another for loop to print the usernames
        print data[i][j]
'''
# update indices, then search through lines of b or a.



#f.close() #close the csv



