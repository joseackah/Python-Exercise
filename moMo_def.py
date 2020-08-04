customer = {
    "phone" : "0201000000",
    "name" : "Gabriel",
    "pin" : 1234,
    "balance" : 50020

}

customer1 = {
    "phone" : "0202000000",
    "name" : "Stephen",
    "pin" : 6010,
    "balance" : 12000

}

vendor = {
    "phone": "0203000000",
    "name": "Kofi",
    "pin": 1010,
    "balance": 11000
    
}

telco = {
    "code": 110

}

def deposit():
    #code = eval(input("enter telco code: "))
    #if code == telco['code']:
        number = input('enter phone number: ')
        if number == customer['phone']:
            amount = eval(input('enter amount to deposit: '))
            if amount >= 1:
                customer['balance'] = customer['balance'] + amount
                print('amount deposited is: ', amount)
                print('your new balance is: ', customer['balance'])
                print('transaction successful.')
                
            else:
                print('enter amount more 1 cedis.')

    #else:
        #print('enter number again.')


def witdrawal():
    #code = eval(input('enter telco code: '))
    #if code == telco['code']:
        number = input('enter number to withdraw from:  ')
        if number == customer['phone']:
            amount = eval(input('enter the amount to witdraw: '))
            if amount >= 1:
                pin = eval(input('enter pin to confirm transaction: '))
                if pin == customer['pin']:
                    venNpin = eval(input('enter vendor pin: '))
                    if venNpin == vendor['pin']:
                        customer['balance'] = customer['balance'] - amount
                        print('amount witdrawed is: ', amount)
                        print('your new balance is: ', customer['balance'])
                        print('transaction successful.')
                    else:
                        print('Try again')
                        
        else:
            print('enter the correct number.')
    #else:
        #print('is not ok')


def transfer():
    #code = eval(input('enter telco code: '))
    #if code == telco['code']:
        senderNumber = input("enter sender's number: ")
        if senderNumber == customer1['phone']:
            amount = eval(input("enter amount to send: "))
            if amount >= 2:
                vendPin = eval(input("enter vendor's pin: "))
                if vendPin == vendor['pin']:
                    vendor['balance']= vendor['balance'] - amount
                    customer['balance'] = customer['balance'] - amount
                    customer1['balance'] = customer1['balance'] + amount
                    print('amount transferred is: ', amount)
                    print('your new balance is: ', customer['balance'])
                    print('transaction successful')

def moMoPro():
    cod = eval(input('Enter Telco code to Proceed: '))
    if cod == telco['code']:
        choose = eval(input('Welcome to Python Mobile Money Services. \nMenu  \n1) Deposit \n2) Withdrawal \n3) Transfer \nEnter: '))
        if choose == 1:
            deposit()
        elif choose == 2:
            witdrawal()
        elif choose == 3:
            transfer()
        else:
            print('Wrong input.')
            back = eval(input('Enter 0 to go back: '))
            if back == 0:
                moMoPro()
            else:
                #return
                print('try')
    else:
        print('Try again')


    

moMoPro()


