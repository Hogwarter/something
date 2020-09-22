import random
print ("Multiplication test")
c = int(input ("Smallest number: "))
d = int(input ("Largest number: "))
while True:
  a = random.randint (c,d)
  b = random.randint (c,d)
  print (a,"*",b)
  vastaus = input (":")
  if int(vastaus) == int(a)*int(b):
    print ("Correct\n")
  else:
    print ("Wrong, the right answer is:")
    print (int(a)*int(b))
    print ("\n")
