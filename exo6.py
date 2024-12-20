a = int(input("Choisissez un nombre: "))
results = [a] 
for i in range(11):
    results.append(results[-1] * 3)
print(*results)