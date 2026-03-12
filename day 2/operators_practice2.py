is_member = input("are you the member?") == "yes"
consume = float(input("how much do you consume?"))
if is_member:
    if consume >= 200:
        consume = consume * 0.8
        print(f"{consume:.2f}")
    else:
        consume = consume * 0.9
        print(f"{consume:.2f}")
else:
    if consume >= 300:
        consume = consume * 0.95
        print(f"{consume:.2f}")
    else:
        print(f"{consume:.2f}")