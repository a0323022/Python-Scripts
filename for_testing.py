'''
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
'''

'''
import csv

f_a = open('apan01.csv', "r")
f_b = open('bpan01.csv', "r")

list_a = list((csv.reader(f_a)))
list_b = list((csv.reader(f_b)))

match = 0
missing_in_B = 0
missing = []
count = 0

for i in list_a:
    #count = count + 1
    #if count >= 3:
    #    break
    for j in list_b:
    #    if i[0] in j[0]:
         if i[0] in j:
            #print(i)
            match = match + 1
            print('a ', i[0:2], 'b ', j[0:2])
            print('Matched ' + str(match))
        #elif i[0] not in j[0]:
         #   missing_in_B = missing_in_B + 1
          #  missing.append(i[0])
           # print("Match", match, "Missing", missing, "Missing in B", missing_in_B)

f_a.close()
f_b.close()

'''
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %i and %s" %(dictionary_tk["age"], dictionary_tk["nationality"])) # And by the way I'm Brazilian