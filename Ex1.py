numbers = []
while True:
    input_from_user = input("Type the number here - If you want to quit, just press Enter: ")
    if input_from_user == "":
        break
    try:
        num = float(input_from_user)
        numbers.append(num)
    except ValueError:
        print("Wrong input, you just need to type a valid number:")
numbers.sort(reverse=True) 
print("These are 5 greatest numbers from your list:")
for i in numbers[:5]:  
    print(i)

    a