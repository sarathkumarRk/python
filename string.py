#find the first two num and last two num
myname = "sarath"

moblie= "9361956099"
masked=moblie[:2] +"******"+moblie[-2:]
print(masked)

#join the word
song = "shape OF you"
artist ="SARATH"
formated=f"{song.title()} - {artist.title()}"
print(formated)

#change the location
location="chennai part"
fixed_location=location.replace( "chennai part", "gundy")
print(fixed_location)

#find the car_id
message="booking your car_id: ucsbd1024. please keep it safe"
car_id=message.split(":")[1].split(".")[0].strip()
print(car_id)

#find the uber100 only promo_meg
promo_meg="its uber100 is that will be show they customer"
if "uber100" in promo_meg:
    print("its allowed")

#find the mother position
mother="my mother name is geetha"
print("position is:", mother.find("geetha"))

#find the initials sk word
name="sarath kumar"
initials="".join([word[0].upper() for word in name.split()])
print(initials)

#progarm not to be space
input="  airport   "
clean=input.strip()
print(clean)

#find the leng word
word1="dear hiring managener"
count=len(word1.split())
print(count)

