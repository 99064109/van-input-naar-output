# Chyvayno Felicia
# Opdracht: pizzaCalculator.py

# Dit zijn de prijzen van de pizza's.
prijs_medium_pizza = 10.95
print(type(prijs_medium_pizza))
prijs_large_pizza = 10.95
prijs_extra_large_pizza = 10.95

# Hier vraag ik input van de gebruiker.
aantal_medium_pizza = int(input("Hoeveel medium pizza's '25cm' wilt u hebben? "))
aantal_large_pizza = int(input("Hoeveel large pizza's '30cm' wilt u hebben? "))
aantal_extra_large_pizza = int(input("Hoeveel extra_large pizza's '35' wilt u hebben? "))

# Dit is de berekening.
bedrag_bestelling_medium = prijs_medium_pizza *aantal_medium_pizza
bedrag_bestelling_large = prijs_large_pizza * aantal_large_pizza
bedrag_bestelling_extra_large = prijs_extra_large_pizza * aantal_extra_large_pizza

totaalbedrag= bedrag_bestelling_medium + bedrag_bestelling_large + bedrag_bestelling_extra_large
print(totaalbedrag)








# medium pizza 25cm $4,95
# large pizza 30cm $8,95
# extra large pizza $35cm 10,95