#mobile money transaction converted to OOP(class method)

class customer1(object):
    name = 'Accra boy'
    pin = 1234
    phoneNumber = '0201234567'
    balance = 5200

    def deposit(self,):
        #self.phoneN = phoneN
        if eval(input('enter pin: ')) == d.pin:
            amount = eval(input('enter amount: '))
            self.balance = self.balance + amount
            print('Transaction successful.')
            print('Amount deposited is', amount, 'your new balance is', (self.balance + amount))
        else:
            print('incorrect pin.')


    def withdrawal(self):
        amount = eval(input("Enter amount to withdraw: "))
        if amount < self.balance:
            print('amount you are withdrawing is: ', amount)
            input("Enter pin to confirm: ")
            self.balance - amount
            print('Transaction successful.')
            print('Your old balance is',self.balance, 'and the new balance is', (self.balance - amount))
        else:
            print("You don't have enough money in your account.")
        

    def get_balance(self):
        return self.balance

    def transfer (self):
        senderN = input("Sender's Number: ")
        amount  = eval(input('Enter amount to transfer: '))
        if amount < self.balance:
            print('Amount to transfer:', amount)
            input('Enter pin to proceed: ' )
            self.balance = self.balance - amount
            d1.balance = d1.balance + amount
            print('Transaction successful.')
            print('You have transferred',amount, 'to this number', d.phoneNumber)
            print('Your balance is: ', d.balance)
            
        else:
            print("You don't have enough balance for this transaction")
        
    def momoP(self):
        print('Welcome to Python MOMO services. \nMenu')
        choice = eval(input('1) Transfer Money \n2) Deposit Money \n3) Withdraw Money \n4) Get Balance \nEnter: '))
        if choice == 1:
            d.transfer()
            ano = eval(input('Enter 0 for another transaction or 1 to exit: '))
            if ano == 0:
                d.momoP()
            elif ano == 1:
                return
            else:
                return
        elif choice == 2:
            d.deposit()
            ano = eval(input('Enter 0 for another transaction or 1 to exit: '))
            if ano == 0:
                d.momoP()
            elif ano == 1:
                return
            else:
                return
        elif choice == 3:
            d.withdrawal()
            ano = eval(input('Enter 0 for another transaction or 1 to exit: '))
            if ano == 0:
                d.momoP()
            elif ano == 1:
                return
            else:
                return
        elif choice == 4:
            d.get_balance()
            ano = eval(input('Enter 0 for another transaction or 1 to exit: '))
            if ano == 0:
                d.momoP()
            elif ano == 1:
                return
            else:
                return
        else:
            print('Wrong Entry.')
            start = input('Enter 0 to start again: ')
            d.momoP()

d = customer1()
d1 = customer1()


#d.deposit(12354)
#d.transfer()
d.momoP()


#print(d.balance)
#print(d1.balance)

        