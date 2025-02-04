def hello():
    number = input("Enter a number: ")
    i = 0
    for i in range(number):
        i += 1
        print(f"{number}*{i} = {number*i}")

hello()