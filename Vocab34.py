import random
import os
#Uptil Pg20
f=open("vocab_words.txt","r+")
p=str(f.read())
k=p.replace(","," ").split()
for i in range(len(k)):
    store1=random.choice(k)
    print(store1,end="")
    os.system('cls')
    input("")
    k.remove(store1)
    

