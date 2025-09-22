#for loop
names=["sarath","ramesh","sanjay","ventesh"]

for text in names:1
print(text.upper())

#while loop

current_pin = "1234"
entered_pin = ""

while entered_pin != current_pin:
    entered_pin = input("Enter your current pin: ")

print("Access granted")

#break
name= [1,2,3,4,5,6,7,]
for i in  name:
    if i==5:
        break
    print(i)

#continous

n=[1,2,-3,-4,10]

for num in n:
    if num <0:
        continue
    print(num)

# Example

count =5

while count >0:
    print(f"countdown: {count}")
    count -=1

print("Time up")    


items=[]

while True:
    item = input("add item ('done' the finish):")
    if item.lower()=='done':
        break
items.append(item)

print("items the card:", item)    

    
