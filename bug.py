def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    total = sum(numbers)
    average = total / len(numbers) 
    return average

my_list = []
result = calculate_average(my_list) 
print(f"The average is: {result}") #This will return 0 as expected

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will return 30.0 as expected

my_list = [10, 20, 0, 40, 50] #ZeroDivisionError if we do not handle this case
result = calculate_average(my_list)
print(f"The average is: {result}") #This will return 24.0 as expected

my_list = ['a','b','c']
result = calculate_average(my_list) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(f"The average is: {result}")