counter = 0  # global variable

def increase():
    global counter   # Needed to make an update on a global variable
    counter += 1

increase()
increase()
print(counter)
