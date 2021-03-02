#tried serarching for password geenrating packages
#none meet the level of quality i need
#hence developing it
from os import system, name
import random

ualpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lalpha="abcdefghijklmnopqrstuvwxyz"
specchar="!@#$%^&*()_+=-`~'<>.|/?"
number="1234567890"

#----------------fucntion to clear cli quiclky when needed----------------
def clearer():
    if(name=="nt"): #checks for windows device
        _ = system('cls')
    else: #linux and mac
        _ =system("clear")

#----------------generate function called by db fucntions----------------
def generate():
    #default vals
    def_alpha=8
    def_ualpha=1
    def_specchar=1
    def_number=2
    password=""
    

    for i in range(def_ualpha):
        rand=random.randint(0,23)
        password=password+ualpha[rand]
    for i in range(def_alpha-def_ualpha):
        rand=random.randint(0,23)
        password=password+lalpha[rand]
    for i in range(def_specchar):
        rand=random.randint(0,len(specchar)-1)
        password=password+specchar[rand]
    for i in range(def_number):
        rand=random.randint(0,9)
        password=password+number[rand]

    finalpass=''.join(random.sample(password, len(password)))

    return finalpass

#----------------fucntion called by custom password generator----------------

def custom_gen():
    print("-------OPTIONS-------")
    print("1.SMALL PASSWORD[length=5]")
    print("2.MEDIUM PASSWORD[length=8]")
    print("3.LARGE PASSWORD[length=12]")
    print("4.CUSTOM PASSWORD[length=custom]")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        def_alpha=3
        def_ualpha=1
        def_specchar=0
        def_number=1
        customgenerator(def_alpha,def_ualpha,def_specchar,def_number)
    if(choice==2):
        def_alpha=5
        def_ualpha=1
        def_specchar=1
        def_number=1
        customgenerator(def_alpha,def_ualpha,def_specchar,def_number)
    if(choice==3):
        def_alpha=8
        def_ualpha=1
        def_specchar=1
        def_number=2
        customgenerator(def_alpha,def_ualpha,def_specchar,def_number)
    if(choice==4):
        clearer()
        def_alpha=int(input("Input number of lower case :"))
        def_ualpha=int(input("Input number of upper case :"))
        def_specchar=int(input("Input number of special charecters :"))
        def_number=int(input("Input number of number :"))
        total=def_alpha+def_number+def_specchar+def_ualpha
        print("Total password length as per given parameters :",total)
        customgenerator(def_alpha,def_ualpha,def_specchar,def_number)

#custom passweord generator accepting number of arguments
def customgenerator(def_alpha,def_ualpha,def_specchar,def_number):
    password=""
    for i in range(def_ualpha):
        rand=random.randint(0,23)
        password=password+ualpha[rand]
    for i in range(def_alpha-def_ualpha):
        rand=random.randint(0,23)
        password=password+lalpha[rand]
    for i in range(def_specchar):
        rand=random.randint(0,len(specchar)-1)
        password=password+specchar[rand]
    for i in range(def_number):
        rand=random.randint(0,9)
        password=password+number[rand]

    finalpass=''.join(random.sample(password, len(password)))

    print("PASSWORD GENERATED:",finalpass)
    waste=input("Press ENTER to go back to menu")

