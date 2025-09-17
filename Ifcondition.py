age=10

if age >= 18:
    print("you can vote")
else:
    print("you cant vote") 

#for example

marks=50

if marks >=70:
    print("Grade A")
elif marks >=50:
    print("Grade B")
elif marks >=40:
    print("Grade c")
else:
    print("fail") 

#nested if 

age=18
driving_license="no"

if age >=18:
    if driving_license == "yes":
     print("you can drive")
    else:
     print("you can go license")
else:
    print("you can young")  

#other example

marks=75
attendance=75

if marks >=80 and attendance>=75:
   print("your or eligible")
else:
   print("not eligible")

#other 1

order_amount=1000
day= "sat"
member="gold"

if (order_amount >=1000 and day in['sat, sun']) or member=="gold":
   print("20% discount")
else:
   print("no discount")




    