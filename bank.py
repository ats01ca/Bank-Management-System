dic={}
Nlist=["Hemanth","Prashanth","navi"]
Plist=[1414,1212,1515]

h=500
p=500
n=500
nc=0
Alist=[h,p,n,nc]
while True:
    print("-------------------------------------------")
    print("|********welcome to bank of vijay*********|")
    print("|-----------------------------------------|")
    print("|Press  1. Open a new account             |")
    print("|Press  2. Withdraw Money                 |")
    print("|Press  3. Deposit Money                  |")
    print("|Press  4. Check Customers & Balance      |")
    print("|Press  5. Check Your Balance             |")
    print("|Press  6. Exit/Quit                      |")
    print("|Press  7. Modify Account Details         |")
    print("|Press  8. Close Account                  |")
    print("-------------------------------------------")
    b=[1,2,3,4,5,6,7,8,9]
    try:
        Cinput=int(input("Enter Number :"),len(b))
    except ValueError:
        print("Press Enter Valid Number only")
        Cinput=int(input("Enter Number :"),len(b))

    if Cinput==1:
        Name=input("Enter Youre Name : ")
        Nlist.append(Name)
        try:
            Pin=int(input("Set Your Pin Digital Only : "))
            Plist.append(Pin)
            
        except ValueError:
            print("Enter Digital Numbers Only")
            Pin=int(input("Now Set Your Pin : "))
            Plist.append(Pin)
        print("Your Account Created Successfully")
        print("Your User Name is :",Name)
        print("Your Pin is :",Pin)
        mainMenu = input('''Please press "Enter" key to go back to main menu...''')
    elif Cinput==2:
        Name=input("Enter Your Name : ")
        if Name in Nlist:        
            Pi=int(input("Enter your pin : "))
            n=Nlist.index(Name)
            if Plist[n]==Pi:
                print("Your Available Balance is : ",Alist[n])
                W=int(input("Enter Your Withdraw Amount : Rs."))
                if Alist[n]<W:
                    print("You have Insufficient Funds")
                    print("Please Check Your Balance")
                else:
                    Alist[n]=Alist[n]-W
                    print("Your Withdraw Amont is : Rs.",W)
                    print("Your Available Balance is : ",Alist[n])
            else:
                print("You are Entered Wrong Pin Number") 
                print("Please try again.....")
        else:
            print("You are Entered Invalid User Name") 
            print("Please try again.....")  
        mainMenu = input('''Please press "Enter" key to go back to main menu...''')

    elif Cinput==3:
        Name=input("Enter Your Name : ")
        if Name in Nlist:        
            Pi=int(input("Enter your pin : "))
            n=Nlist.index(Name)
            
            print("Your Available Balance is : ",Alist[n])
            D=int(input("Enter Your Deposit Amount : Rs."))
            Alist[n]=Alist[n]+D
            print("Your Deposit Amont is : Rs.",D)
            print("Your Available Balance is : ",Alist[n])

        else:
            print("You are Entered Invalid User Name") 
            print("Please try again.....") 
        mainMenu = input('''Please press "Enter" key to go back to main menu...''')
    elif Cinput==4:
        for i in Nlist:
            print("customer name : ",i,"   ",end=" ")
        print()
        for j in Alist:
            print("Amount in bank : ",j,"Rs.     ",end=" ")
        print()
        print("No. Of Customers in Bank : ",len(Nlist)+1)
        print("Total Money Available in Bank : ",sum(Alist))
        print()
        mainMenu = input('''Please press "Enter" key to go back to main menu...''')
    elif Cinput==5:
        Name=input("Enter Your Name : ")
        if Name in Nlist:        
            Pi=int(input("Enter your pin : "))
            n=Nlist.index(Name)
            if Plist[n]==Pi:
                print("Your Available Balance is : ",Alist[n])
            else:
                print("You are Entered Wrong Pin Number") 
                print("Please try again.....")
        else:
            print("You are Entered Invalid User Name") 
            print("Please try again.....")  

        mainMenu = input('''Please press "Enter" key to go back to main menu...''')
    elif Cinput==6:
        print("Thank you for Choosing our bank")
        print("Visit again")

    elif Cinput==7:
        print("Press 1 for Modify Name")
        print("Press 2 for Modify Pin")
        i=int(input("Enter the Number 1 or 2 only : "))
        if i==1:
            un=input("Enter Your Name : ")  
            if un in Nlist:
                up=int(input("Enter Your Pin : "))
                pp=Nlist.index(un)                
                if Plist[pp]==up:
                    ON=input("Enter Your Old Name : ")
                    NN=input("Update Your Name : ")
                    Nlist[pp]=NN
                    
                    print("Your Updated User Name is : ",Nlist[pp])
                else:
                    print("Your Entered Wrong Pin")
            else:
                print("Your Entered Invalid User Name")
        elif i==2:
            un=input("Enter Your Name : ")  
            if un in Nlist:
                up=int(input("Enter Your Pin : "))
                pp=Nlist.index(un)                
                if Plist[pp]==up:
                    OP=Plist[pp]
                    np=int(input("Enter Your New Pin : "))
                    Plist[pp]=np
                    print("Your Updated Pin is : ",Plist[pp])
                else:
                    print("Your Entered Wrong Pin")
                    mainMenu = input('''Please press "Enter" key to go back to main menu...''')
            else:
                print("Your Entered Invalid User Name")
        mainMenu = input('''Please press "Enter" key to go back to main menu...''')
    elif Cinput==8:
        Name=input("Enter Your Name : ")
        if Name in Nlist:        
            Pi=int(input("Enter your pin : "))
            n=Nlist.index(Name)
            if Plist[n]==Pi:
                print("Your Available Balance is : Rs.",Alist[n])
                print("If You Want to Close Your Account Press: 1")
                print("If You Dont Want to Close Your Account Press : 2")
                de=int(input("Enter Your Number : "))
                if de==1:
                    print("Please Take Your Remaining Amount : Rs.",Alist[n])
                    del Nlist[n]
                    del Plist[n]
                    del Alist[n]
                    print("Your Account has been Closed")
                else:
                    mainMenu = input('''Please press "Enter" key to go back to main menu...''')                
            else:
                print("You are Entered Wrong Pin Number") 
                print("Please try again.....")
                mainMenu = input('''Please press "Enter" key to go back to main menu...''')
        else:
            print("You are Entered Invalid User Name") 
            print("Please try again.....")  
        mainMenu = input('''Please press "Enter" key to go back to main menu...''')




        