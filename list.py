# creating for lists in apps

playlist=["shape you", "naa ready", "annan varan"]
zomoto=["pizza","noodles","chikenbater"]
recent_location=["chennai","arcot","chittor"]

print("spolity playlist:" ,playlist)
print("zomotp foods:", zomoto)
print("uber location:", recent_location)

# lists methods

playlist.append("oo antava")
print("after append" , playlist)

playlist.insert(1,"song_sarath")
print("after insert", playlist)

playlist.remove("annan varan")
print("after removing" ,playlist)

playlist.pop()
print("after pop" ,playlist)

playlist.reverse()
print("after reverse" ,playlist)

print("count" , playlist.count("naa ready"))

# list slicing

print("top 2 songs",playlist[0:2])

# list iteration

for food in zomoto:
    print("all food" , food)

# check if

if "pizza" in zomoto:
    print("yes")

zomoto [1]="italy"
print(zomoto)

mixed=["sarath",23,1.22]

for a in mixed:
    print(a)



recent_location=["home", "work", "airport"]

for i,location in enumerate (recent_location):
    print(f"loction {i}: {location}")






