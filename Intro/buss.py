print("Hur gammal är du?")

age = input()
age = int(age)

if age > 18:
    print("Din biljett kostar 21kr")

elif age >= 18 and age <64:
    print("Då kostar din biljett 32 kr")

elif age >= 65 and age <70:
    print("Din biljett kostar 21 kr")

elif age >= 20 and age <30:
    print("Du är vuxen så din biljett kostar 32 kr")