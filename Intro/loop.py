sentence = "Hej på dig"

for letter in sentence:
    print(letter)

    for i in range(1, 11):
        if i == 5:
            continue
    print(i)

gambling = True

while gambling:
    print("$$$")

    if input() == "stop":
        break

while True:
    print("Mata in ett nummer")

    number_1 = input()

    try:
        number_1 = int(number_1)
    except:
        print("Försök igen")