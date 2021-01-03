sname=input("enter student name=")
srollno=input("enter roll no")
sub1=float(input("enter sub1 name="))
sub2=float(input("enter sub2 name="))
sub3=float(input("enter sub3 name="))
sub4=float(input("enter sub4 name="))
sub5=float(input("enter sub5 name="))
sub6=float(input("enter sub6 name="))
total=sub1+sub2+sub3+sub4+sub4+sub5+sub6
percentage=(total/600)*100
print("total=",total)
print("percentage=",percentage)
if(percentage>=80 and percentage<=100):
  print("grade==A")
elif(percentage>=60 and percentage<=79):
  print("grade=B")
elif(percentage>=50&percentage<=59):
  print("grade==c")
elif(percentage>=40&percentage<=49):
  print("great==D")
else:
  print("fail")
            
            
