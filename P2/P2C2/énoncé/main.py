# Ecrivez votre code ici !
nombres = "1,2,3,4"
liste = nombres.split(",")
# Convertir les éléments en nonbre
datas = []
for nombre in liste:
   nombre_int = int(nombre)
   datas.append(nombre_int)
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


