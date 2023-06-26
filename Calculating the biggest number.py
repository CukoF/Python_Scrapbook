n = int(input("How many numbers do you give?: "))

for i in range(n):
    input_number = int(input(f"{i+1}. number: "))
    bigger_num = 0
    if i == 0 or bigger_num < input_number:
        bigger_num = input_number

print(f"The biggest number is {bigger_num}.")