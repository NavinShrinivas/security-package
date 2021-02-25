from os import system, name
import passripper
import dbmanager

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