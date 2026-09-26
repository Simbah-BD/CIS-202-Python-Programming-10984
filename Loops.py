muffins = 10
cupcakes = 10

item = input()
while item != "0":
    if item == "muffin":
        if muffins > 0:
            muffins -= 1
        else:
            print("Out of stock")
    elif item == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Out of stock")
    item = input()

print("muffins:", muffins, "cupcakes:", cupcakes)
