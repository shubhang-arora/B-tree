import os
import random


def createfile(name, number):
    path = os.getcwd()
    inputFile = open(os.getcwd()+'/'+name+'.txt','w')
    for i in range(1, int(number)):
        inputFile.write(str(random.randint(100, 20000)))
        inputFile.write(",")
    inputFile.close()


if __name__ == '__main__':

    name = raw_input("Input name of the File you want to create")
    number = raw_input("Enter the number of objects you want to write in the file")
    createfile(name, number)
