def remove_odd_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]
input_string = input("Type a list of numbers here, remember to separate them by press Space: ")
original_list = list(map(int, input_string.split()))
remove_odd_numbers_list = remove_odd_numbers(original_list)

print("This is your original list:", original_list)
print("This is your original list, but removed odd numbers:", remove_odd_numbers_list)