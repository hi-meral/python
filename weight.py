weight = int(input(" Your weight : "))
unit = input(" L or Gram : ")


if (unit == "L"):
    converter = weight * 0.45
    print(f"Your weight is {converter} Kilo OR {weight} L")
elif (unit == "K"):
    converter = weight / 0.45
    print(f"Your weight is {converter} L OR {weight} Kilog")
else:
    print(f"Your weight is {weight} ")
