def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print("Vad vill du räkna?")

    num1 = int(input("Första tal: "))
    num2 = int(input("Andra talet: "))

    print("Vad vill du göra med", num1, "och", num2)
    print("1: Multiplikation\n2: Division\n3: Addition\n4: Subtraktion")

    number = input("Välj operation (1-4): ")

    if number == "1":
        print("Resultat:", multiplication(num1, num2))
    elif number == "2":
        print("Resultat:", divide(num1, num2))
