Account_holder_name=""
Account_balance=3000
card_number=["1830","7997","9398","1680"]
card_number_acces=""
Account_number=["99892924661","123456789","493335871757","327756649882"]
IFSC_Code=["SBIN0000989","SBIN34567","SBIN8430199","SBIN4489167"]
Root_IFSCcode_of_Bank="SBIN"
card_pin=["9989","0000","9999","7777"]
card_num_loop="1"
print("""
> Creat Account <1>
> Already Have Account <2>
""")
welcome=input("> ")
welcome_loop=""
import random
while welcome_loop!="1" and welcome_loop!="2":
    if welcome=="1":
        card=0
        while card==0:
            Create_CardNo=input("\n> Create Four Digits Card Number: ")
            if Create_CardNo in card_number:
                print(f"\nCard No Already Existed Try With Different No.")
            else:
                card_number.append(Create_CardNo)
                card=1
        pin=0        
        while pin==0:
            Create_Pin=input("\n> Set Four Digits Pin: ")
            if Create_Pin in card_pin:
                print("\nPin No Already Existed Try With Different pin.")
            else:
                card_pin.append(Create_Pin)
                random_acc_num=''.join([str(random.randint(0, 9)) for i in range(12)])
                random_acc_number=random_acc_num
                random_acc_code=''.join([str(random.randint(0, 9)) for i in range(7)])
                random_acc_ifscCode=Root_IFSCcode_of_Bank+random_acc_code
                print(f"\nYou Have Successfully Created Your New Account, This Is Your Card Number: '{Create_CardNo}', Account Number: '{random_acc_number}' , IFSC Code: '{random_acc_ifscCode}' and Password: '{Create_Pin}' Thankyou. ")
                Account_number.append(random_acc_number)
                IFSC_Code.append(random_acc_ifscCode)
                pin=1
        crd_num=input("\n> Enter your card number: ")
        welcome_loop=welcome
        break
    elif welcome=="2":
        crd_num=input("\n> Enter your card number: ")
        while card_num_loop!=card_number_acces:
            flag=0
            for c_n in card_number:
                card_number_acces=c_n
                if crd_num==card_number_acces:
                    print("""
\n>
> Withdraw Cash <1>
> Balance Enquiry <2>
> Deposite Cash <3>
                    """)
                    flag=1
                    card_num_loop=crd_num
                    find_index_card=card_number.index(crd_num)
                    break

              
            if flag==0:
                print("Card Number Not Valid Try Again")
                crd_num=input("\n> Enter your card number: ")
        welcome_loop=welcome
    else:
        print("Entered Wrong ❌ option")
        welcome=input("> ")
while card_num_loop!=card_number_acces:
    flag=0
    for c_n in card_number:
        card_number_acces=c_n
        if crd_num==card_number_acces:
            print("""
\n>
> Withdraw Cash <1>
> Balance Enquiry <2>
> Deposite Cash <3>
            """)
            flag=1
            card_num_loop=crd_num
            find_index_card=card_number.index(crd_num)
            break

              
    if flag==0:
        print("Card Number Not Valid Try Again")
        crd_num=input("\n> Enter your card number: ")
welcome_loop=welcome
command=input("> ")
command_loop=""
while command_loop!="1" and command_loop!="2" and command_loop!="3":
    if command=="1":
        print("""
\n>
> Savings Account <1>
> Current Account <2>
    """)
        command0=input("> ")
        command0_loop=""
        while command0_loop!="1" and command0_loop!="2":
            if command0=="1":
                command_savings_amt=input("\n> Enter Amount: ")
                command_savings_pin=input("\n> Enter Your Pin: ")
                if command_savings_pin==card_pin[find_index_card]:
                    print(f"> You have successfully completed your withdrawal of amount Rs.{command_savings_amt}/-.From your Savings Account XXX0")
                else:
                    print("You Entered Wrong Pin Try Again")
                    break
                command0_loop=command0
            elif command0=="2":
                command_current_amt=input("\n> Enter Amount: ")
                command_current_pin=input("\n> Enter Your Pin: ")
                if command_current_pin==card_pin[find_index_card]:
                    print(f"> You have successfully completed your withdrawal of amount Rs.{command_current_amt}/-.From your Current Account XXX0")
                else:
                    print("You Entered Wrong Pin")
                    break
                command0_loop=command0
            else:
                print("You Entered Wrong Option Try Again")
                command0=input("> ")
        command_loop=command
    elif command=="2":
        command_bal_enq=input("\n> Enter Your 4 Digits Pin: ")
        if command_bal_enq==card_pin[find_index_card]:
            print(f"> Mr.{Account_holder_name} Your Available Account Balance is Rs.{Account_balance}/-,Your Account Ending with XXX0. ")
        else:
            print("You Entered Wrong Pin")
        command_loop=command
    elif command=="3":
        command_dep_acc_num=input("\n> Enter Your Account Number: ")
        command_dep_ifc=input("\n> Enter Your IFSC Code: ").upper()
        if (command_dep_acc_num==Account_number[find_index_card]) and (command_dep_ifc==IFSC_Code[find_index_card]):
            command_dep_amt=input("\n> Enter Deposit Amount: ")
            print(f"> You Request of Deposited of Amount Rs.{command_dep_amt}/- Have Been Successfully Completed Of Account Ending with XXX0 ")
        else:
            print("You Have Entered Wrong Details, Please Check Your Details Correctly")
        command_loop=command

    else:
        print("You Entered Wrong Option Try again")
        command=input("> ")