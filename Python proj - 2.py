import mysql.connector as mysql                                                     # IMPORTING MYSQL
con=mysql.connect(host='localhost',user='root',password='rishi',database='reservation',charset='utf8')
cur=con.cursor()


print("\n")
print("="*55,"WELCOME  TO  INDIAN  RAILWAYS  BOOKING  SITE","="*61)                     # INTRO LINE




def main1():                            # DEFINING PHASE 1
    print("\n"*2)
    print('+'*62,"WELCOME TO THE LOGIN PAGE",'+'*73)
    print("\n1. Sign Up")                                         # MENU DRIVEN PHASE 1
    print("2. Login In")
    print("3. Delete Account")
    print("4. Exit")
    ch=int(input("Enter your choice : "))

  
    if ch==1:                                                           # SIGN UP 
        n1=input("Enter your Name : ") 
        pn=int(input("Enter your Phone Number : "))
        e=input("Enter your E-mail : ")
        p=input("Enter your Password : ")
        
        s="INSERT INTO main1 (name,ph_no,email,password) VALUES (%s,%s,%s,%s)"                  # ENTERS THE VALUE IN MYSQL TABLE
        b1=(n1,pn,e,p)
        cur.execute(s,b1)
        con.commit()
        print("\n")
        print("YOUR ACCOUNT HAS BEEN CREATED SUCESSFULLY !!! ")
        v=0
        while v==0:
            ch6=input("Would you like to move to RESERVATION PAGE or would like to continue to LOGIN PAGE (R/L) :")
            if ch6.upper()=='R':
                main2()
            elif ch6.upper()=='L':
                main1()
                break
            else:
                print(" Please enter a valid choice !!! ")
                v=0

                
    elif ch==2:                                             # LOG IN
        #n5=input("Enter your Name : ")
        e1=input("Enter your REGISTERED E-mail : ")
        p1=input("Enter your Password : ")
        print("\n")
        log="SELECT * FROM main1 WHERE email='{}' AND password='{}'".format(e1,p1)
        cur.execute(log)
        re=cur.fetchall()
        row1=cur.rowcount
        # print(row1)
        # print(re[1])
        if (row1 == 1):
            print("You have Logged in succesfully !!!")
            main2()
        else:
            print("Incorrect password !")
            print("Please enter Correct Password !!!")
            main1()
      
    elif ch==3:                                             # DELETE ACCOUNT
        n6=input("Enter your Full Name : ")
        e2=input("Enter your REGISTERED E-mail : ")
        p2=input("Enter your Password : ")
        b=1
        while b==1:
            ch2=input("Are you sure that you want to DELETE your account (Y/N) : ")
            if ch2.upper()=='Y':
                print("\nACCOUNT DELETED !!!")
                dele="DELETE FROM main1 where password='{}' AND email='{}'".format(p2,e2)
                cur.execute(dele)
                con.commit()
                
                main1()
                break
                
            elif ch2.upper()=='N':
                main1()
            else:
                print(" Please enter a valid choice !!! ")
                b=1

                
    elif ch==4:                         #EXIT
        #break
        print("~"*49,"THANK  YOU  FOR  VISITING  INDIAN  RAILWAYS  BOOKING  SITE","~"*52)

    else:
        print("Please enter a valid choice !!! ")
        main1()
        
        

    
def main2():                                # DEFINING PHASE 2
    print("\n")
    print("\n")
    
    print('+'*59,"WELCOME TO THE RESERVATION PAGE",'+'*70)
    print("\n")
    print("1. Booking")                 # MENU DRIVEN PHASE 2
    print("2. Checking")
    print("3. Cancellation")
    print("4. Log Out")
    ch1=int(input("Enter your choice : "))

    
    if ch1==1:                                  # BOOKING
        pname=input("Enter the name of Main Passenger : ")
        a1=int(input("Enter the age : "))
        c=2
        while c==2:
            ch3=input("Do you want another passenger (Y/N): ")
            if ch3.upper()=='Y':
                pa2=input("Enter the name of Another passenger : ")
                a2=int(input("Enter the age : "))
                c=2
            elif ch3.upper()=='N':
                break
            else:
                print("Please enter a valid choice !!! ")
                c=2
        pn1=int(input("Enter your Phone Number : "))
        source=input("Enter your SOURCE : ")
        destin=input("Enter your Destination : ")
        tno=int(input("Enter Train Number : "))
        tna=input("Enter Train Name : ")
        d=input("Enter Date Of Journey (yyyy:mm:dd) : ")
        import random
        clas=input("Enter class (SL,3AC,2AC,1AC,CC,EC,2S) : ")           # CLASS 
        print("\n")
        if clas.upper()=='SL':
            coac=random.randint(1,12)
            coach1=str(coac)
            o1=random.randint(1,72)
            print("Your Coach number is : S"+coach1)
            print("Your Seat number is : ",o1)
        elif clas.upper()=='3AC':
            coac1=random.randint(1,4)
            coach1=str(coac1)
            o1=random.randint(1,72)
            print("Your Coach number is : B"+coach1)
            print("Your Seat number is : ",o1)
        elif clas.upper()=='2AC':
            coac2=random.randint(1,4)
            coach1=str(coac2)
            o1=random.randint(1,72)
            print("Your Coach number is : A"+coach1)
            print("Your Seat number is : ",o1)
        elif clas.upper()=='1AC':
            coac3=random.randint(1,2)
            coach1=str(coac3)
            o1=random.randint(1,72)
            print("Your Coach number is : H"+coach1)
            print("Your Seat number is : ",o1)
        elif clas.upper()=='CC':
            coac4=random.randint(1,14)
            coach1=str(coac4)
            o1=random.randint(1,72)
            print("Your Coach number is : C"+coach1)
            print("Your Seat number is : ",o1)
        elif clas.upper()=='EC':
            coac5=random.randint(1,4)
            coach1=str(coac5)
            o1=random.randint(1,72)
            print("Your Coach number is : E"+coach1)
            print("Your Seat number is : ",o1)
        elif clas.upper()=='2S':
            coac6=random.randint(1,4)
            coach1=str(coac6)
            o1=random.randint(1,72)
            print("Your Coach number is : D"+coach1)
            print("Your Seat number is : ",o1)
        else:
            print("!!!!!! PLEASE ENTER A VALID CHOICE !!!!!! GOING BACK TO RESERVATION PAGE !!!!!!")
            print("\n")   
            main2()
        
        import random
        lst10=[]
        for i in range(9):
            lst10.append(str(random.randint(1,9)))
        print("PNR number of your trip is : ")
        print('9',end='')
        for i in lst10:
            print(i,end='')
        print("\n"*2)
        
        str10="9"
        for i in lst10:
            str10+=i

        
        
        print('#'*10,"YOUR TRIP HAS BEEN SUCESSFULLY BOOKED !!!",'#'*10)
        print("\n")
        print('='*30,"THANK  YOU !!! HAVE A SAFE JOURNEY !!! " ,'='*86)
        pq=input("DO YOU WANT TO SEE A COPY OF YOUR TICKET (Y/N) : ")
        if pq.upper()=="N":
            print("A COPY OF YOUR TICKET WILL BE EMAILED TO YOU THROUGH YOUR MENTIONED EMAIL ID !!!!")
        elif pq.upper()=="Y":

            def ticket():
                print('_'*162)
                print("\n",' '*70,"INDIAN      RAILWAYS")
                print('_'*162)
                    
                                                                                        # DEFINING OUTLINE OF TICKET
                    
                print("SOURCE = ",source,' '*100,"DESTINATION = ",destin)
                print("\n")
                print("TRAIN NAME = ",tna,' '*88,"TRAIN NUMBER = ",tno)
                print("\n")
                print("COACH NUMBER = ",coach1,' '*100,"SEAT NUMBER = ",o1)
                print("\n") 
                print("DATE = ",d,' '*100,"PHONE NUMBER  = ",pn1)
                print("\n")
                print("NAME = ",pname,' '*99,"AGE = ",a1)
                print("\n")
                    
                print('_'*162)
                print("\n",' '*65,"HAVE A SAFE AND HAPPY JOURNEY ! ! !")
                print('_'*162)
            ticket()


            

            
        z="INSERT INTO main2 (pname,age,ph_no,source,destin,tr_non,tr_name,date,pnr) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        k=(pname,a1,pn1,source,destin,tno,tna,d,str10)                                 # ENTERS THE VALUE IN MYSQL TABLE 
        cur.execute(z,k)
        con.commit()

        
            
        
        main2()

        
    elif ch1==2:                                                # CHECKING DETAILS
        qwe=int(input("Enter your Trip's PNR number : "))
        #pnr1=int(input("Enter the Phone Number :" ))
        

        # result=""
        check="SELECT pname,age,ph_no,source,destin,tr_non,tr_name,pnr FROM main2 WHERE pnr='{}'".format(qwe)

        cur.execute(check)
        result=cur.fetchall()
        row2=cur.rowcount
        if row2==1:
            print("\nDetails of your trip are as follows : ")
            for i in result:
                print("Name :- ",i[0])
                print("Age :- ",i[1])
                print("Phone Number :- ",i[2])
                print("SOURCE :- ",i[3])
                print("DESTINATION :- ",i[4])
                print("Train Number :- ",i[5])
                print("Train Name :- ",i[6])
                print("PNR :- ",i[7])
        else:
            print("\nNo such PNR found !!!")
            print("Please enter a valid PNR !!!")

        main2()
        
        
    elif ch1==3:                                                    # CANCELLING
        # ph_no=int(input("Enter the Phone Number associated with your ticket : "))
        pnr2=int(input("Enter the PNR number of your trip : "))
        
        while True:
            ch4=input("Are you sure that you want to CANCEL your trip (Y/N) : ")
            if ch4.upper()=='Y':
                print("\nYour Ticket has been CANCELLED succesfully !!!")
                delet="DELETE FROM main2 where pnr='{}'".format(pnr2)
                cur.execute(delet)
                con.commit()
                main2()
                break
            elif ch4.upper()=='N':
                print("\n")
                main2()
            else:
                print(" Please enter a valid choice !!! ")
                print("\n")
                main2()
                break

                
    elif ch1==4:                                # LOG OUT
        h=6
        while h==6:
            ch5=input("Are you sure that you want to LOG OUT (Y/N) : ")
            if ch5.upper()=='Y':
                main1()
                break
            elif ch5.upper()=='N':
                main2()
            else:
                print(" Please enter a valid choice !!! ")
                h=6
    else:
        print("Please enter a valid choice !!! ")
        main2()


main1()                 # MAIN PROGRAMM

        
