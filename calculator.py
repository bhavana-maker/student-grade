def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b
select=int(input("select operation 1,2,3,4,="))
a=int(input("enter first number="))
b=int(input("enter second number="))
if select==1:
 print(a,"+",b,"=",add(a,b))
elif select==2:
 print(a,"-",b,"=",sub(a,b))
elif select==3:
 print(a,"*",b,"=",mul(a,b))
elif select==4:
 print(a,"/",b,"=",div(a,b))
else:
 print("invalid") 
        
