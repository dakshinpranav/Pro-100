class ATM (object):
    def __init__(self,cardNumber,pinNumber):
        self.pinNumber=pinNumber
        self.cardNumber=cardNumber

    def withDraw(self):
        print("Enter your amount")
    
    def checkBallance(self):
        print("Your ballance is ₹1005600")

    def changePin(self):
        print("Pin changed")

Atm=ATM(12345,7557)
print(Atm.cardNumber)
print(Atm.pinNumber)
Atm.withDraw()
Atm.checkBallance()
Atm.changePin()
