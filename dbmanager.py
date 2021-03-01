import time
import csv
import pandas as pd
from pandas import DataFrame
import passripper
import random
import time
from os import system, name
from prettytable import from_csv
import csv 

def clearer():
    if(name=="nt"): #checks for windows device
        _ = system('cls')
    else: #linux and mac
        _ =system("clear")

# C={'WEBSITE':[],
#     'USERNAME':[],
#     'PASSWORD':[]}
# df=DataFrame(C)



def dbcreate():
    fields=[['WEBSITE','USERNAME','PASSWORD']]
    dbname=input("Enter name of DB: ")
    f=open(dbname+".csv","w+")
    f.close()
    password=passripper.generate()
    with open(dbname+".csv",'a',newline='\n') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(fields)
    print("PASSWORD FOR CREATED DB [PLEASE REMEMBER CAREFULLY][CAN NOT BE RESET]:")
    print("\t \t",password,"\n \n")
    print("INITIAL ENCRYPTION:")
    csvfile.close()
    encrypt(dbname,ceasernum(password))
    print("Encryption taking place!Please wait,It is a time consuming process.")
    time.sleep(6)
    print("\n Encryption over! Your data is now safe.")
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
    finalval=random.randint(0,23)
    return(finalval)
        

def encrypt(dbname,ceasernum):
    f=open(dbname+".csv","r")
    data=f.read()
    result=""
    for i in range(len(data)):
        char=data[i]
        result+=chr(ord(char)+ceasernum)
    f.close()
    f=open(dbname+".csv","w")
    f.write(result)
    f.close()

def decrypt(dbname,ceasernum):
    f=open(dbname+".csv","r")
    data=f.read()
    result=""
    for i in range(len(data)):
        char=data[i]
        result+=chr(ord(char)-ceasernum)
    f.close()
    f=open(dbname+".csv","w")
    f.write(result)
    f.close()

def create_entry(dbname):
    website=input("Enter name of website this credentials will be used for :")
    username=input("Enter username :")
    pass_flag=True
    passneed=input("Is a new password needed [DEFAULT:Y /N] :")
    entrypass=""    
    if(passneed=='N'):
        pass_flag=False
    else:
        pass_flag=True


    if(pass_flag==True):
        entrypass+=passripper.generate()
    else:
        temp=input("Enter pre-decided password :")
        entrypass+=temp
    f=open(dbname+".csv",'a')
    f.write(website+','+username+','+entrypass+'\n')
    f.close()


def livedb(dbname,password):
    decrypt(dbname,ceasernum(password))
    f=open(dbname+".csv","r")
    data=f.readline().rstrip('\n')
    if data[0]!='W':
        encrypt(dbname,ceasernum(password))
        f.close()
        print("PASSWORD ENTERED IS WRONG!")
        waste=input("Press ENTER to go back to menu")
    else:
        print("Decryption taking place!Please wait,It is a time consuming process.")
        time.sleep(6)
        print("\n Decryption over! Your data is now readable.")
        waste=input("Press ENTER to continue")
        flag=True
        while flag:
            clearer()
            with open(dbname+".csv", "r") as fp: 
                x = from_csv(fp)
            fp.close()
            print(x)
            print("1.New entry \t \t 2.Exit")
            choice=int(input("Choice:"))
            if(choice==1):
                clearer()
                create_entry(dbname)
                clearer()
            if(choice==2):
                encrypt(dbname,ceasernum(password))
                print("Encryption taking place!Please wait,It is a time consuming process.")
                time.sleep(6)
                print("\n Encryption over! Your data is now safe.")
                waste=input("Press ENTER to go back to menu")
                return


#present bookmarks for work