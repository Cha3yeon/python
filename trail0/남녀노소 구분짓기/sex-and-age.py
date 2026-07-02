G = int(input())
A = int(input())

if G ==1:
    if A >= 19:
        print("WOMAN")
    else:
        print("GIRL")
else:
    if A >= 19:
        print("MAN")
    else:
        print("BOY")