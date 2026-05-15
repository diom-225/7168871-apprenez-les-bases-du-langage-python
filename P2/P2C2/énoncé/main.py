# Ecrivez votre code ici !
nombres = "1,2,3,4"
liste = nombres.split(",")
# Convertir les éléments en nonbre
datas = []
for i in liste:
    if i == '1':
       datas.append(1)
    elif i == '2':
       datas.append(2)
    elif i == '3':
      datas.append(3)
    elif i == '4':
      datas.append(4)
print(datas)
# Calculons la somme des nombres
sommes = sum(datas)
print(sommes)

# Calculons la moyenne
moyenne = sommes / len(datas)
print(moyenne)

# Calculons et affichons le nombre de nombres dans la liste qui sont supérieurs à la moyenne
donnée = []
for x in datas:
   if x > moyenne:
      donnée.append(x)
      print(len(donnée))


