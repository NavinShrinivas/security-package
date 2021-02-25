import passripper

def dbcreate():
    dbname=input("Enter name of DB: ")
    f=open(dbname+".txt","w+")
    f.close()
    password=passripper.generate()
    print("PASSWORD FOR CREATED DB [PLEASE REMEMBER CAREFULLY][CAN NOT BE RESET]:")
    print("\t \t",password)
    waste=input("Press ENTER to go back to menu")