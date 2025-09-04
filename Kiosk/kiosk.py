print("Hej! Vad får det lov att vara?")
print("Det finns glass, varmkorv, läsk och godis")
print("Glass 20kr")
print("Varmkorv 15kr")
print("Läsk 15kr")
print("Godis 10kr")

svar = input("Vad vill du köpa?")

pris = input()

if svar == "glass":
    antal = int(input("Hur många vill du ha? "))
   
    if antal >= 10:
        print("Det är för många!")
    else:
        pris = 20 * antal
        print("Det blir {pris}kr")