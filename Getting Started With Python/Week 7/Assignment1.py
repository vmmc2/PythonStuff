largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try: # tento fazer a conversao de string para numero.
        value = int(num)
        if largest is None:
            largest = value
        elif largest < value:
            largest = value
        if smallest is None:
            smallest = value
        elif smallest > value:
            smallest = value
    except: # se der ruim, eu dou output de erro.
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
