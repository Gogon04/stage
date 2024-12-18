a = int(input("Entrer un premier nombre A:"))
c = input("Entrer un premier opérateur ")
b = int(input("Entrer un second nombre B:"))
f = input("Entrer un second opérateur ")
e = int(input("Entrer un troisième nombre C: "))
d =0
q = 0
g = 0
n = 0
total = [ a,b,c,e,f ]
chiffres = [a,b,e]
opérateur = [c,f]

if c == '+':
    d = a + b 
elif c == '-':
    d = a - b
elif c == '*':
    d = a * b 
elif c == '/':
    d = a / b
if f == '+' :
    n = d + e
elif f == '-':
    n = d - e
elif f == '/':
    n = d / e
elif f == '*':
    n = d*e
print(n)   
for p in chiffres :
    q+=1
for z in opérateur :
    g+=1
    
