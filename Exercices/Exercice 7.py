numb = int(input("Enter a number: "))

while numb <1 or numb > 10:
    numb = int(input("Enter a number: "))
    if numb < 1 or numb > 10:
        print("Vous avez choisi:",numb,"Le nombre n'est pas compris entre 1 et 10")

print("Vous avez choisi:", numb, "il est compris entre 1 et 10")