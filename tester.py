from dbmanager import decrypt,encrypt,ceasernum
#----------query wrapped arounf encryption and decryption----------
def query(dbname,password,q):
    decrypt(dbname,ceasernum(password))
    f=open(dbname+".csv","r")
    data=f.readline().rstrip('\n')
    if data[0]!='E':
        encrypt(dbname,ceasernum(password))
        f.close()
        print("PASSWORD ENTERED IS WRONG!")
        waste=input("Press ENTER to go back to menu")
    else:
        presentflag=0
        rdln=f.readline()
        ans=""
        process=[]
        while rdln:
            process=[]
            ans=""
            ans+=rdln
            process=ans.split(',')
            print(process[1])
            if process[1]==q:
                presentflag=1
                break
            rdln=f.readline()
        # if presentflag==1:
        #     print("Entry number : ",process[0])
        #     print("Website Name: ",process[1])
        #     print("Username : ",process[2])
        #     print("Passwords : ",process[3])
        #     waste=input("Press ENTER to go back to menu")
        # else:
        #     print("Record not found!")
        #     waste=input("Press ENTER to go back to menu")
        encrypt(dbname,ceasernum(password))

query("test4","ppur7lj|9Px","adsfs")