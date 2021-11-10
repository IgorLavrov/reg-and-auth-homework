import random
pas_list=[]
log_list=[]
 
def login(l,p):
    print("Enter your login")
    log=input()
    number=l.count(log)
    if number==0:
        l.append(log)
        print(" /a-Automatic password, /r-Manual password ")
        r=input()
        if r.lower()=="a":
            print(auto_reg(l,p))
        elif r.lower()=="r":
            reg_t(l,p)
    if number>0:
        print("This Login is already existed")
        print("Would you like to authorize-yes or quit-no")
        vt=input
        if vt=="yes":
            authorisation(l,p)
        else:
            exit()
 
 
def reg_t(l,p):
    list1=[".",",",";","!","_","*","-","+","(",")","#","¤","%","&"]
    print("Enter your pasword")
    pass3= input()
    pas=list(pass3)
    correct=0
    a=0
    b=0
    c=0
    for n in range(len(pas)):
        if(pas[n].isupper()):
            print("Вы ввели заглавную букву ")
            a+=1
        if (pas[n].isdigit()):
            print("Вы ввели цифру ") 
            b+=1
        if pas[n] in list1:
           print("Вы ввели .,:;!_*-+()/#¤%& ")
           c+=1
    correct=a+b+c
    if correct >3 and a or b or c !=0 :
        print("password correct")
        p.append(pass3)
        print("added")
        print(pas_list,log_list)
    else:
        print ("wrong password")
        reg_t()
 

def authorisation(l,p):
    print("Enter your login")
    print(log_list,pas_list)
    log= input()
    print("Enter yout password")
    passw=input()
    
    if log in log_list:  
        if  passw==pas_list[log_list.index(log)]:
            print ("Log in Success")
        else:
            print("Wrong password")
    else:
        print("Wrong login")
 
def auto_reg(l,p):
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    pas = ''.join([random.choice(ls) for x in range(12)])
    p.append(pas)
    return pas

 
while 1:
    print("a-registreerimine,\ne autoriseerimine,\nr välja" )
    valik=input("Sinu valik:")
    if valik.lower()=="a":
       login(log_list,pas_list)
    elif valik.lower()=="e":
        authorisation(log_list,pas_list)
    elif valik.lower()=="r":
        break
