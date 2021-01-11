class Atm(object) :
 def __init__ (self , cardNumber , pinNumber) :
  self.cardNumber = cardNumber
  self.pinNumber = pinNumber

  def cashWithdrawal(self) :
   print("You have withdrawn 100 Dollars from your account.")

  def balanceEnquiry(self) :
   print("You Have 100,000 Dollars In Your Balance.")