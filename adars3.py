with open("text.txt","r") as f:
    soz = f.read().split()
    max=soz[0]
    for i in soz:
        if max>i:
            max=i
print(f"eng uzun soz->{max}")

