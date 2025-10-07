trip={
    'id':"ub112285",
    'pickup':"arcot",
    'drop':"chennai central",
    'fare':450.00,
    'driver':"ravi",
    'status':"completed"
}

print(trip["pickup"])
print(trip["status"])

for key, value in trip.items():
     print(key,":",value)

trip.update({"car_model" : "honda"})
print(trip)

trip.update({"car_model" : "hp delux"})
print(trip)

trip.pop("status")
print(trip)



