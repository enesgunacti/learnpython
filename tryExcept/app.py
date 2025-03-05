try:
    #value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

# spesifik hatayı except ile yakalamak daha doğru bir yaklaşım. Her yere except yazarsan hangi hatadan olduğunu bulmak zorlaşır.