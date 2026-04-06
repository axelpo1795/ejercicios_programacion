def count_cap_low(text):
    cap = 0
    low = 0

    for character in text:
        if character.isupper():
            cap += 1
        elif character.islower():
            low += 1
    
    print(f"There’s {cap} upper cases and {low} lower cases")

count_cap_low("I love Nación Sushi")
