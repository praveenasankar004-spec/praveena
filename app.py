
Name=(input("enter your Name :"))
Age=int(input("enter your Age :"))
Class=(input("enter your Class :"))
Tamil=int(input("enter your Tamil Mark :"))
English=int(input("enter your English Mark :"))
Maths=int(input("enter your Maths Mark :"))
Science=int(input("enter your Science Mark :"))
Social=int(input("enter your Social mark :"))
Total=Tamil+English+Maths+Science+Social
print("Total Marks :",Total)
if(90<Total): 
    print("Grade A")
elif(90>Total and 70<Total):
    print("Grade B")
elif(70>Total and 50<Total):
    print("Grade C")
elif(50<Total and 30>Total):
    print("Grade D")
else:
    print("No Grade")
    
    
    
