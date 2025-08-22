#ejercicio 

def print_numbers(text1, text2)-> int: 
    count = 0
    for number in range(1, 101 ):
        if number % 3 == 0 and number % 5 == 0: 
            print(text1 + text2)
        elif number % 3 == 0: 
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count +=1
    return count

print(print_numbers("Fizz", "Buzz")) 