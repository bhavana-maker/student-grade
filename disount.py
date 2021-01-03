amt=int(input("enter amount"))
if(amt>=100 and amt<=1000):
 disc=amt
elif(amt>=1001 and amt<=2000):
    disc=0.1*amt
elif(amt>=2001 and amt<=3000):
    disc=0.2*amt
elif(amt>=3001):
    disc=0.25*amt
else:
 print("invalid amount")
print("amount=",amt)
print("disount=",disc)
print("net pay=",amt+disc)
 
