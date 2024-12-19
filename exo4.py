a=(int(input("Saisissez un nombre:")))
b=(int(input("Saissez le chiffre que vous souhaitez cherchez:")))
c=0
for d in str(a):
 if d == str(b):
  c+=1
print("Il y a ",c,"fois",b,"dans",a)