from os import system, name
from passripper import generate

def clearer():
    if(name=="nt"): #checks for windows device
        _ = system('cls')
    else: #linux and mac
        _ =system("clear")

def dbcreate():
    dbname=input("Enter name of DB: ")
    f=open(dbname+".txt","w+")
    f.close()
    password=generate()
    print("PASSWORD FOR CREATED DB [PLEASE REMEMBER CAREFULLY][CAN NOT BE RESET]:")
    print("\t \t",password)
    waste=input("Press ENTER to go back to menu")
    


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
        dbcreate()
        clearer()