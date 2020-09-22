x=2
y=3
b=1
a=int(input("Kuinka monta fibonacci lukua?: "))
if a%2!=0:
  c=1
else:
  c=0
print (x)
if a == 1:
  exit()
print (y)
a=a/2
while b < a:
  x=x*y
  print (x)
  if c!=0:
    if b+1 >= a:
      break
  y=x*y
  print (y)
  b=b+1
