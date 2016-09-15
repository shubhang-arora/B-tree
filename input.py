import os
import random
path = os.getcwd()
print(path)
helloFile = open(os.getcwd()+'/hello.txt','w')
for i in range(1,200000):
    helloFile.write(str(random.randint(1,20000)))
    helloFile.write(",")

helloFile.close()
