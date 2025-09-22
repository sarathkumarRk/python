def name():
    print("Welcome to python practical")

name()    

def great(name):
    print(f"Hello {name},Welcome!")

great('sarath')   

def sub(a,b):
    print(a-b)

sub(5,3)

def add(a,b):
    return a+b
result=add(10,90)
print(result)

#for example

def add(*args):
    total=0
    for num in args:
        total +=num

    return total
    
print(add(1,2,3,1))


#other example

def create_profile(**kwargs):
    print("user profile")
    for key,value in kwargs.items():
          print(f"{key} :{value}")

create_profile(name="sarath", age=23, job="full stack python")       

