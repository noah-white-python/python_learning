#a program for temperature conversion
#val == value
#res == result
print("enter Q to quit")
while True:
    val = input("enter a temperature with symbol(eg:18c or 80f)").strip().upper()
    if val == "Q":
        print("the program has exited")
        break
    if val.endswith("F"):
        res = (float(val[:-1]) - 32) * 5 / 9
        print(f"conversion result is{res:.2f}")
    elif val.endswith("C"):
        res = float(val[:-1]) * 9 / 5 + 32
        print(f"conversion result is：{res:.2f}")
    else:
        print("transcription error")