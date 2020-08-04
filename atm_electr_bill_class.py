
class atm:
    balance = 500

    def __init__(self, pin):
        self.pin = pin
        
    
    
    def deposit(self):
        amount = eval(input('enter deposit amount: '))
        self.balance = self.balance + amount
        print('your deposited amount is ', amount, '\n Your new balance is ', d.balance)
        print('Transaction successful.')
    
    def atm_Pin(self):
        pin = input('enter pin to proceed: ')
        if len(pin) == 4:
            return
        else:
            print('enter correct number')

    def getBalance(self):
        self.balance = self.balance
        choose = eval(input('choose account. \n1: Savings \n2: current \nEnter: '))
        if choose == 1:
            print(self.balance)
        elif choose == 2:
            print(d1.balance)
        else:
            print('service not available')

    def transfer(self):
        amount = eval(input('enter transfer amount: '))
        if amount == self.balance - 5:
            self.balance = self.balance - amount
            d1.balance = d1.balance + amount
            print(' verify amount to transfer:', amount)
            enter = input("Press enter to Proceed.")
            print('transaction successful')
        else:
            print("You don't have enough balance for this transaction.")
            

    def withdrawal(self):
        amount = eval(input('enter withdraw amount: '))
        if amount == self.balance - 5:
            self.balance = self.balance - amount
        else:
            print("You don't have enough balance for this transaction.")

    def atmProcess(self):
        print('Welcome to AITI-KACE Bank \nATM Services.')
        print('tips for the day \nIf you card get missing report to the bank immediately for the necessary action.')
        d.atmPin()
        choice = eval(input('Services \n1: Deposit \n2: Withdrawal \n3: Check balance \n4: Transfer \nEnter:  '))
        if choice == 1:
            d.deposit()
        elif choice == 2:
            d.withdrawal()
        elif choice == 3:
            d.getBalance()
        elif choice == 4:
            d.transfer()

        else:
            print('You have entered a wrong number.')

        


d = atm(1234)
d1 = atm(5678)






class elecBill:
    
    vat = 0.1250
    natElecL = 0.0200
    striL = 0.0300
    nhilGet = 0.0500
    serCharg = 0.4075
    montBill = {}

    def __init__(self, unitPrice):
        self.unitPrice = 0.7979

    def meterRead(self):
        
        if cur > prev:
            metread = current - previous
            print(metread, 'kWh')

        else:
            return

    def monthBill(self):
        self.montBill = round((metread * self.unitPrice),3)
        print('Bill is: ', self.montBill)

    def vatR(self):
        vaR = ((current - previous) * self.unitPrice)
        self.va = round((self.vat * ((32*self.serCharg) + vaR)),2)
        print('Vat on bill: ', self.va)
    def natElecLe(self):
        nat = ((current - previous) * self.unitPrice)
        self.natElec = round((self.natElecL * nat),2)
        print('National Electr. Levy: ', self.natElec)
    def striLi(self):
        light = ((current - previous) * self.unitPrice)
        self.striLii = round((self.striL * light),2)
        print('street Light: ', self.striLii)
    def nhilGetF(self):
        get = ((current - previous) * self.unitPrice)
        self.nhilGe = round((self.nhilGet * ((32*self.serCharg) + get)),2)
        print('NHIS and GETFUND Levy: ', self.nhilGe)
    def servChar(self):
        servCha = round((32 * self.serCharg),2)
        print('Service charges for 32days: ', servCha)
    def totalThisMonth(self):
       
        totalThisMont = round(((self.montBill) + (32 * self.serCharg) + ((self.montBill + (32 * self.serCharg)) * self.nhilGet) + (self.montBill * self.striL) + 
                                (self.montBill * self.natElecL) + (((self.montBill + (32 * self.serCharg)) * self.vat))),3)
        print('Total current bill: ', totalThisMont)


    
    def elecCal(self):
        
        choice = eval(input('choose 1: monthly calcuation \n2: other services \nEnter: '))
        if choice == 1:
            print(meterNu)
            d.meterRead()
            d.monthBill()
            d.vatR()
            d.natElecLe()
            d.striLi()
            d.nhilGetF()
            d.servChar()
            d.totalThisMonth()
        elif choice == 2:
            choose = eval(input('1: NHIS and GETFUND \n2: Service charges \n3: Value Added Tax(VAT) \n4: Meter Readings \n5: Stright Light \n6: National Electrification Levy \n7: This Month Bill \n Enter: '))
            if choose ==1:
                d.nhilGetF()
            elif choose ==2:
                d.servChar()
            elif choose ==3:
                d.vatR()
            elif choose == 4:
                d.meterRead()
            elif choose == 5:
                d.striLi()
            elif choose == 6:
                d.natElecLe()
            else:
                print('Wrong selection.')
                    
            
            
            
        else:
            print('start again.')

print('Electricity bill calculation.')
meterNu = eval(input(' Enter Meter number: '))
previous = eval(input('Enter Previous meter readings: '))
current = eval(input('Enter Current meter readings: '))
metread = current - previous

d = elecBill(0.7979)


d.atmProcess()
d.elecCal()
