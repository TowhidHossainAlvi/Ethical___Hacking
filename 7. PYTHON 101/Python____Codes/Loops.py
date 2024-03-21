# Example of a for loop
print("for loop")
for i in range(5):
    print(i)
print("------------")


# Example of a while loop
print("while loop")
count = 0
while count < 5:
    print(count)
    count += 1
print("------------")


# Example of a do-while loop equivalent
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print("------------")

# Iterate over a list
print("Prining list using for loop")
list = [1, 2, 3, 4, 5]
for num in list:
    print(num)
print("------------")

# Nested loop to print multiplication table
print("Nested loop")
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=' ')
    print()  # Print newline after each row
print("------------")


# Using break to exit loop early
print("'break' in loop")
for i in range(1, 6):
    if i == 3:
        break
    print(i)
print("------------")


# Using continue to skip an iteration
print("'continue' in loop")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("------------")


# Using else block with a loop
print("Block in loop")
for i in range(1, 4):
    print(i)
else:
    print("Loop completed successfully!")

print("------------")
