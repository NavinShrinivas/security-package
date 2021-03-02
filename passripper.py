#tried serarching for password geenrating packages
#none meet the level of quality i need
#hence developing it

import random

ualpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lalpha="abcdefghijklmnopqrstuvwxyz"
specchar="!@#$%^&*()_+=-`~'<>.|/?"
number="1234567890"


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

print(generate())

#----------------fucntion called by custom password generator----------------

