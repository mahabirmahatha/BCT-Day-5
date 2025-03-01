from prettytable import PrettyTable
L=[]
class Signupinterface:
    
    def __init__(self,e,p):
         self.email=e
         self.password=p
         self.table=PrettyTable()
    def signup(self):
        if(self.email.endswith("gmail.com")):
            a={"Email:":self.email,"Password:":self.password}
            L.append(a)
            print("SignUp successful.")
            return
        else:
            print("Email format is not valid. Please enter correct email.")
            return

    def check(self):
        for i in range(len(L)):
            if(self.email.endswith("gmail.com")):
                if(L[i]['Email:']==self.email):
                    if(L[i]['Password:']==self.password):
                        print("Login successful.")
                        return
                    else:
                        print("Incorrect password.")
                        return
            else:
                print("Email format is not valid. Please enter correct email.")
                return
        print("Email is not registered, please SignUp first.")
        return

    def show(self):
        self.table.field_names = ["Email", "Password"]
        for i in range(len(L)):
            e=L[i]['Email:']
            p=L[i]['Password:']
            self.table.add_row([self.email,self.password])
        print(self.table)
        self.table.clear()

c=str(input("Do you want to SignUp? (Yes/No):"))
if(c.lower()=="yes"):
    email=input("Enter your email:")
    password=input("Enter your password:")
    t1=Signupinterface(email,password)
    t1.signup()
d=str(input("Do you want to SignIn? (Yes/No):"))
if(d.lower()=="yes"):
    email1=input("Enter your email:")
    password1=input("Enter your password:")
    t2=Signupinterface(email1,password1)
    t2.check()
e=str(input("Do you want to see database? (Yes/No):"))
if(e.lower()=="yes"):
    for i in range(len(L)):
      t3=Signupinterface(L[i]['Email:'],L[i]['Password:'])
      t3.show()