a = int(input("Entrer un premier nombre A: "))
b = int(input("Entrer un second nombre B: "))
c = input("Entrer votre opérateur:") 
d = 0
if c == '+':
    d = a + b
elif c == '-':
    d = a - b
elif c == '*':
    d = a * b
elif c == '/':
    d= a/b
print(d)    