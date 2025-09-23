uber_cities1={"chennai", "bangalore", "mumbai", "bangalore"}
uber_cities2={"chennai", "mumbai", "delhi", "bangalore"}

print(uber_cities1.union(uber_cities2))
print(uber_cities1.intersection(uber_cities2))
print(uber_cities1.difference(uber_cities2))

uber_cities1.remove("chennai")
print(uber_cities1)



# unique_cities=set(uber_cities)
# print(unique_cities)