class User():
    __count = 0
    def __init__(self,name,gender,salary):
        self.name = name                                  
        self.gender = gender
        self.salary = salary
        User.__count = User.__count+1
        self.__account = User.__count
    def showdetails(self):
        print(f"Name :{self.name}\nGender : {self.gender}\nSalary : {self.salary}")
        print("Account No :",self.__account)
class Bank():
    __balance = 0
    __bankname="DNS Bank".center(30)
    __usercount = 0
    def __init__(self,name,gender,salary,pin):
        self.name = name
        self.gender  = gender
        self.salary = salary
        self.__pin = pin
        Bank.__usercount +=1
        self.account = f"bnkaccno000{Bank.__usercount}"
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        print("Amount Deposited Successfully")
        print("Your Current Balance is :",self.__balance)
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient Balance")
            print("Your Current Balance is :",self.__balance)
        elif amount>=100 and amount<=self.__balance:
            self.__balance = self.__balance-amount
            print("Thank You For Visiting")
            print("Your Current Bank Amount is :",self.__balance)
        elif amount<100:
            print("You Cannot Withdraw Less Than 100")
            print("Your Current Balance is :",self.__balance)
    def viewbalance(self):
        print(f"Name : {self.name}\nGender : {self.gender}\nSalary : {self.salary}\nCurrent Balance :{self.__balance}")
    def transfer(self,amt,user):
        if amt>self.__balance:
            print("Insufficient Balance")
            print("Your Current Balance is :",self.__balance)
        elif amt>=1 and amt<=self.__balance:
            user.deposit(amt)
            self.__balance = self.__balance-amt
            print("Amount Transfer Successfully")
            print("Current Balance :",self.__balance)
        elif amt<1:
            print("You Cannot Transfer amount less than 1")
            print("Curent Balance :",self.__balance)
            
    def getusername(self):
        return self.name
    def getpin(self):
        return self.__pin
    def logindata(self):
        return [self.name, self.__pin]
    def __str__(self):
        return f"{self.name} {self.__pin}"
            
              
users = {}

while True:
    print("1. Create Account\n2. Login\n->Exit")
    choice = input("Enter your Selection : ")
    
    if choice == "1":
        while True:
            name = input("Enter your Name : ")
            if name.isalpha():
                break
            else:
                print("Invalid Name. Please enter only characters.")
                
        while True:
            gender = input("Enter your Gender (1 for Male, 2 for Female, etc.): ")
            if gender.isdigit():
                break
            else:
                print("Invalid Gender. Please enter only Number.")

        while True:
            salary = input("Enter your Salary: ")
            if salary.isdigit():
                salary = int(salary)
                break
            else:
                print("Invalid Salary. Please enter an Number.")

        while True:
            pin = (input("Set your Password (PIN) :"))
            if pin.isdigit():
                pin = int(pin)
                break
            else:
                print("Invalid pin. Please enter an Number.")
        
        users[name] = Bank(name, gender, salary, pin)


    elif choice == "2":
        name = input("Enter your Name : ")
        while True:
            pin_input = input("Enter your Password (PIN): ")
            if pin_input.isdigit():
                pin = int(pin_input)
                break
            else:
                print("Invalid PIN. Please enter an Number.")

        obj = users.get(name, 0)

        if obj == 0:
            print("No Match Found")
        elif obj.getpin() == pin:
            print("Access Granted")
            while True:
                print("1. Deposit\n2. Withdraw\n3. View Balance\n4. Transfer\n5. Logout")
                action = input("Choose an Action: ")
                if action == "1":
                    while True:
                        amount_input = input("Enter the deposit amount: ")
                        if amount_input.isdigit():
                            amount = int(amount_input)
                            break
                        else:
                            print("Invalid amount. Please enter an Number.")
                    obj.deposit(amount)
                elif action == "2":
                    while True:
                        amount_input = input("Enter the withdraw amount: ")
                        if amount_input.isdigit():
                            amount = int(amount_input)
                            break
                        else:
                            print("Invalid amount. Please enter an Number.")
                    obj.withdraw(amount)
                elif action == "3":
                    obj.viewbalance()
                elif action == "4":
                    accountant_name = input("Enter the Account User Name: ")
                    account = users.get(accountant_name, 0)
                    if account == 0:
                        print("Person Not Found")
                    else:
                        while True:
                            amount = input("Enter the transfer amount: ")
                            if amount.isdigit():
                                amount = int(amount)
                                break
                            else:
                                print("Invalid amount. Please enter an integer.")
                        obj.transfer(amount, account)
                elif action == "5":
                    print("Logging Out")
                    break
                else:
                    print("Invalid Operation, Try again")
            else:
                print("Access Denied")

    elif choice == "3":
        print("Exit")
        break
