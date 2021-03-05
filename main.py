from os import system, name
import passripper
import dbmanager
import getpass
import customceaser

#----------------fucntion to clear cli quiclky when needed----------------
def clearer():
    if(name=="nt"): #checks for windows device
        _ = system('cls')
    else: #linux and mac
        _ =system("clear")


#----------------main driver code INITIAL LANDING PAGE----------------
clearer()
flag=True
while flag:
    print("==========PASSWORD MANAGER==========")
    print("1.new DB")
    print("2.existing DB")
    print("3.Custom password generator")
    print("4.Ceaser cipher")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        clearer()
        dbmanager.dbcreate()
        clearer()
    if choice==2:
        clearer()
        dbname=input("Enter DB name:")
        try:
            f=open(dbname+".csv","r")
        except IOError:
            print("File not found!Please make a database if not created.")
            waste=input("Press ENTER to go back to menu")
        else:
            p=getpass.getpass(prompt='Enter password of DB:') 
            dbmanager.livedb(dbname,p)
        clearer()
    if(choice==3):
        clearer()
        passripper.custom_gen()
        clearer()
    if choice==4:
        clearer()
        print("Enter file name with extension[.txt,.csv] or type text directly :\n")
        data=input("INPUT:")
        typ=customceaser.classifier(data)
    if choice==5:
        flag=False
        exit()
    else:
        print("Enter a valid choice!!")