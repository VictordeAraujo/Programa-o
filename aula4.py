n= int(input( ))
for x in range(1,100):
  print(n)
  a=n//100
  n=n%100
  print("%d nota(s) de R$ 100,00" %a)
  b=n//50
  n=n%50
  print("%d nota(s) de R$ 50,00" %b)
  c=n//20
  n=n%20
  print("%d nota(s) de R$ 20,00" %c)
  d=n//10
  n=n%10
  print("%d nota(s) de R$ 10,00" %d)
  e=n//5
  n=n%5
  print("%d nota(s) de R$ 5,00" %e)
  f=n//2
  n=n%2
  print("%d nota(s) de R$ 2,00" %f)
  g=n//1
  n=n%1
  print("%d nota(s) de R$ 1,00" %g)
  break;
