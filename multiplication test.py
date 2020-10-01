from random import randint

print ("Multiplication test")
c = int(input ("Smallest number: "))
d = int(input ("Largest number: "))

if d>c:
  while True:
    
    a = randint (c,d)
    b = randint (c,d)
    print (a,"*",b)
    
    vastaus = input (":")
    
    if vastaus == "":
      break
    elif int(vastaus) == int(a)*int(b):
      print ("Correct\n")
    else:
      print ("Wrong, the right answer is:")
      print (int(a)*int(b))
      print ("\n")
      
else:
  print("Error! Smallest number is bigger than or equal to the largest one")
