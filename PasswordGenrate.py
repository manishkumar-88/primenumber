lowletters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capletters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers =['0','1','2','3','4','5','6','7','8','9']
special =['!','@','#','$','%','&','*']


import random
user= input("how strong you want your password (strong/weak)? ")
if user=="weak":
 for i in range(7):
  password =""
  password+=random.choice(lowletters)
  print("password is ",password, end="")
elif user =="strong":
  password =""
  password+=random.choice(lowletters)
  password += random.choice(lowletters)
  password += random.choice(lowletters)
  password+=random.choice(special)
  password+=random.choice(capletters)
  password+=random.choice(numbers)
  password+=random.choice(capletters)
  password += random.choice(capletters)
  print("password is ", password, end=" ")
else:
   print("wrong input please enter only strong or weak")

