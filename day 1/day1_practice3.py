name = input("what is ur name")
while True:
    try:
        age = int(input("enter ur age"))
        break
    except ValueError:
        print("enter a number")
hobby = input("enter your hobby")
clear_name = len(name.replace(" ",""))
word_count = len(name.split())
print(f"hello,everyone,my name is {name},my age is{age}")
print(f"my hobby is {hobby}")
print(f"after {30-age} years old i am 30 years old")
if word_count>1:
    print(f"my name have {len(name.split())} words and it include {clear_name} letters")
else:
    print(f"ur name have {clear_name} words")