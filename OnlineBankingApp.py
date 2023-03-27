import math
print("Welcome to the online banking application")
def sign_in():
    global name # username
    global pin # password
    global cb # current balance
    name = str(input("Please create your username"))
    pin = str(input("Please create your 6 digits pin"))
    if len(pin) == 6:
        pin = pin
    else:
        print("The pin has to be in 6 digits")
        new_pin = str(input("Please create your 6 digits pin"))
        if len(new_pin) != 6:
            print("The pin has to be in 6 digits")
            sign_in()
        else:
            pin = new_pin
    print("Thanks for creating your bank account")

def forgot_pin():
    recover_pin = str(input("Please create your new 6 digits pin"))
    if len(recover_pin) != 6:
        print("The pin has to be in 6 digits")
        forgot_pin()
    else:
        print("the new pin has been stored, please log in")
        pin = recover_pin
        login()

def deposit_interest(p,r,t):
    # A = Pe^(rt) which is the formula for calculating the compound interest
    p = float(p)
    r = float(r)
    t = float(t)
    rt = r * t
    e = math.exp(rt)
    # Calculation
    a = p * e # Future value of your investment
    return a

def login():
    # make1 represents username
    # pin1 represents user's pin
    name1 = str(input("Please enter your username"))
    pin1 = str(input("Please enter your pin"))
    # Check if the name and pin matched
    if name1 == name and pin1 == pin:
        print("welcome to the online banking application" + " " + name)
        print("Please choose the menu down here")
        list_menu = ["1-Deposit","2-Withdraw","3-Transfer","4-Check Balance","5-Deposit interest rate","6-Calculate compound interest"]
        for b in list_menu:
            print(b)
        choose = int(input("Please enter the number of your chose"))
        d = 0 # d represents deposit
        w = 0 # w represents withdraw
        cb = 0 # cb represents current balance
        if choose == 1:
            d = int(input("Enter the amount of your deposit"))
            cb = d
            print("Your current balance is" +" "+ str(cb))
        elif choose == 2:
            w = int(input("Enter the amount of money that you want to withdraw"))
            if w > cb:
                print("Your current balance is not sufficient for this transaction")
                login()
            else:
                cb = d-w
                print(str(w) +" "+ "has been withdrawn from your account" +" "+ " and your current balance is" + " " + str(cb))
        elif choose == 3:
            dest = str(input("Please enter the account number of your destination in 8 digits"))
            if len(dest) == 8:
                amount = int(input("Please enter the amount of money that you want to transfer"))
                if amount > cb:
                    print("Your current balance is not sufficient for this transaction")
                    login()
                else:
                    cb = d - amount
                    print("The transaction of" + " " + str(amount) + " " + "has been transferred to" + " " + str(dest) + " " + " your current balance is" + str(cb))
            else:
                print("The transaction has been rejected since the destination account number is invalid")
                login()        
        elif choose == 4:
            print("Your current balance is" +" " + str(cb))
        elif choose == 5:
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate = 2
            else:
                rate = 1.5
            print("Your current deposit interest rate is" +" "+ str(rate) + " %")
        elif choose == 6:
            list_option = ["1-Calculate your deposit compound interest based on your CB","2-Calculate your deposit compound interest based on your deposit input"]
            for n in list_option:
                print(n)
            choice = int(input("Please enter your choice from the options above"))
            if choice == 1:
                timing = str(input("How many years you want to invest your money"))
                if d > 50000:
                    rate_x = 3/100
                elif d > 30000:
                    rate_x = 2/100
                else: 
                    rate_x = 1.5/100
                print("Your current balance in" + " " + timing + " " + "years will be")
                print(deposit_interest(cb,rate_x,timing))
            elif choice == 2:
                timing1 = str(input("How many years you want to invest your money"))
                money = str(input("Please enter the amount of money you would like to deposit"))
                money = int(money)
                if d > 50000:
                    rate_x = 3/100
                elif d > 30000:
                    rate_x = 2/100
                else: 
                    rate_x = 1.5/100
                print("Your current balance in" + " " + timing + " " + "years will be")
                print(deposit_interest(money,rate_x,timing))
        else:
            print("Option is not available, back to main menu")
            login()
        
    else:
        print("Either of your username or pin is wrong, did you create your account?")
        list1 = ["1-yes","2-no"]
        for i in list1:
            print(i)
        inp = int(input("Enter your choice below"))
        if inp == 1:
            list2 = ["1-do you want to attempt to log in again?","2-You forgot your pin"]
            for e in list2:
                print(e)
            the_answer = str(input("Please enter you choice"))
            the_answer = int(the_answer)
            if the_answer == 1:
                login()
            elif the_answer == 2:
                forgot_pin()
            else:
                print("Option is not available")
                login()
        elif inp == 2:
            print("Please create your account")
            sign_in()
    exit()

def mainmenu():
    option_one = int(input("Choose 1 to sign in and choose 2 to log in"))
    if option_one == 1:
        sign_in()
    elif option_one == 2:
        login()
    else:
        print("Option is not available")
        mainmenu()
    exit()
    
def exit():
    answer = str(input("Do you still want to conduct transaction? Yes or No"))
    if answer == "Yes":
        login()
    elif answer == "No":
        print("Thank you for using this app")
    else: 
        print("Option is not available")
        mainmenu()

mainmenu()


