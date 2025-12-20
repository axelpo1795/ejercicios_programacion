def reverse(text):
    result = ""
    for character in text:
        result = character + result
    return result

print(reverse("Hola mundo"))
