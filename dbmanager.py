import time
import csv
import pandas as pd
from pandas import DataFrame
import passripper
import random

def dbcreate():
    dbname=input("Enter name of DB: ")
    f=open(dbname+".csv","w+")
    f.close()
    password=passripper.generate()
    C={'USERNAME':[],
        'PASSWORD':[]}
    df = DataFrame(C, columns= ["USERNAME","PASSWORD"])
    df.to_csv(dbname+'.csv',index = None, header=True)
    print("PASSWORD FOR CREATED DB [PLEASE REMEMBER CAREFULLY][CAN NOT BE RESET]:")
    print("\t \t",password)
    waste=input("Press ENTER to go back to menu")

def ceasernum(password):
    specchar=""
    specflag=True
    num=""
    numflag=True
    ampha=""
    alpha_count=0
    speclist=['!','@','#','$','%','^','&','*','(',')','_','+','=','-','`','~',"'",'<','>','.',',','|','/','?']
    for i in range(0,len(password)):
        if(password[i] in speclist and specflag):
            specchar=password[i]
            specflag=False
        if(password[i].isnumeric() and numflag):
            num=password[i]
            numflag=False
        if(password[i].isalpha() and alpha_count!=2):
            alpha_count+=1
        if(password[i].isalpha() and alpha_count==2):
            alpha=password[i]
            alpha_count+=1
    random.seed(specchar+num+alpha)
    finalval=random.randint(0,24)
    return(finalval)
        

def encrypt(dbname,ceasernum):
    f=open(dbname+".csv","r")
    data=f.readline().rstrip('\n')
    result=""
    for i in range(len(data)):
        char=data[i]
        result+=chr(ord(char)+ceasernum)
    f.close()
    f=open(dbname+".csv","w")
    f.write(result)

encrypt("csdf",-24)