ATM_card=input("insert the atm_card")
if ATM_card=="right side"or ATM_card=="left side":
  language=input("select language")
  if language=="english"or language=="english"or language=="hindi"or language=="bengoli":
    pin=int(input("enter your pin"))
    if pin>=1000 and pin<=9999:
      transaction_type=input("enter transaction_type")
      if transaction_type=="withdrawal"or transaction_type=="Withdrawal":
          account_type=input("enter account type")
          if account_type=="current" or account_type=="saving":
             amount=int(input("enter amount"))
             key_name=input("enter_name")
             if amount>=500 and amount<2000 and amount%500==0:
               a=amount//2000
               b=amount%2000
               c=b//500
               d=b%500
               print("notes of 2000",a,"notes of 500",c)
               key_name=input("enter ok")
               if key_name=="ok"or key_name=="ok":
                 money_receip=input("enter money_receip")
                 if money_receip=="y" or money_receip=="no":
                    print("money_received")
                 else:
                     print("thanks for transaction")
               else:
                  print("limited amount")
      elif transaction_type=="balance enquiry"or transaction_type=="balance enquiry":
          account_type=("enter amount_type")
          key_name=input("enter ok")
          print("total amount")
          if key_name=="ok"or key_name=="ok":
              print("thankes for enquiry")
          elif key_name=="ok" or key_name=="ok":
              print("transaction compelete")
          else:
              print("invalid key")
      elif transaction_type=="deposit money"or transaction_type=="deposit money":
            account_no=int(input("enter account no"))
            if account_no>=1000000000 and account_no<=9999999999:
              bill_amount=int(input("enter bill amount"))
              if bill_amount>=1000000000 and bill_amount<=9999999999:
                 amount=int(input("enter amount"))
                 key_name=input("enter ok")
                 if key_name=="ok"or key_name=="ok":
                  print("succesful")
                 else:
                   print("unsuccesful")
      elif transaction_type=="bill_payment"or transaction_type=="bill_payment":
            account_no=int(input("enter account no")) 
            if account_no>=1000000000 and account_no<=9999999999:
              bill_id=int(input("enter bill ID"))
              if bill_id>=1000000000 and bill_id<=9999999999:
                 amount=int(input("enter amount"))
                 key_name=input("enter ok")
                 if key_name=="ok" or key_name=="Ok":
                    print("succesful")
                 else:
                    print("unsuccesful")
              else:
                  print("not succesful") 
      else:
          print("invalid pin")
    else:
        print("no bengoli language ")
  else:
      print("rejected")
                   
                      

               
