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