def hello():
    number = input("Enter a number: ")
    i = 0
    for i in range(10):
        i += 1
        print(f"{number} x {i} = {int(number) * i}")

hello()