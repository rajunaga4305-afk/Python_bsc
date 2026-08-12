n = eval(input("Enter rows"))

# Outer loop controls the number of rows
for i in range(1, n + 1):
    # Inner loop controls the number of stars printed in each row
    for j in range(1, i + 1):
        print("*", end=" ")
    # Move to the next line after each row is complete
    print()