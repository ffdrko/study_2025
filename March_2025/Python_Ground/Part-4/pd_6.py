a = input("Enter the number: ")

print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)}x {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Some imp lines of code.")
print("End of program")