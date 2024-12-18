a=(input("Choisissez un mot:"))
if "e" in a:
  print("Le mot contient la lettre e")
if "e" not in a:
  print("Le mot choisi ne contient pas lettre e")
  for tr in a :
   if tr == 'e':
    a+=1     
    print ("il y a ",a,"dans le mot")