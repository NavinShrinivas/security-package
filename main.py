from os import system, name
import passripper
import dbmanager
import getpass

def clearer():
    if(name=="nt"): #checks for windows device
        _ = system('cls')
    else: #linux and mac
        _ =system("clear")


    
clearer()
flag=True
while flag:
    print("==========PASSWORD MANAGER==========")
    print("1.new DB")
    print("2.existing DB")
    print("3.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        clearer()
        dbmanager.dbcreate()
        clearer()
    if choice==2:
        clearer()
        dbname=input("Enter DB name:")
        p=getpass.getpass(prompt='Enter password of DB:') 
        dbmanager.livedb(dbname,p)
        clearer()
    if choice==3:
        flag=False
        exit()