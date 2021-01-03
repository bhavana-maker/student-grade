unit=int(input("enter no.of units consumed="))
if(unit>=1 and unit<=50):
      Rate=unit*3
elif(unit>=51 and unit<=100):
      Rate=unit*6
elif(unit>=100 and unit<=150):
      Rate=unit*9
elif(unit>=151 and unit<=200):
      Rate=unit*12
else:
      Rate=unit*15
print("unit=",unit)
print("Rate=",Rate)

      
          
