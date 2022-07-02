import random
import csv
import string

def generate_pw():
    s=''
    for i in range(8):
        s += random.choice(list_of_characters)
    return s

f=open(r"C:\Users\User\Desktop\NF2\2nd sem\mentors_credentials.txt",'r')
r=next(csv.reader(f))
credentials_list=[]
for line in csv.reader(f):
    credentials_list.append(line)
f.close()
print(credentials_list)

list_of_characters=list(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
list_of_characters.remove(',')
random.shuffle(list_of_characters)

for i in range(len(credentials_list)):
    pw=generate_pw()
    credentials_list[i].append(pw)

f=open(r"C:\Users\User\Desktop\NF2\2nd sem\mentors_credentials1.txt","w+",newline="")
w=csv.writer(f,delimiter=",")
w.writerow(["Email-id","password"])
for i in credentials_list:
    w.writerow(i)
f.close()
