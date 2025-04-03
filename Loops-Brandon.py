# 1. Write a script that prints the numbers from 1 to 10 two different ways. 
# Use a while loop for the first, and a for loop for the second.


# while loop
w_num = 1
while w_num <= 10:
    print(w_num)
    w_num += 1

print("\n")

# for loop
for x in range(10):
    print(x + 1)

# Write a loop that prints all the numbers from 0 to 50 that are divisible by 3, 6, or 9.

print("\n")

div_num = 1
while div_num <= 50:
    if div_num % 3 == 0 or div_num % 6 == 0 or div_num % 9 == 0: # Checks if number is divisible by 3, 6, or 9
        print(div_num)
    div_num += 1


# Print how many times you need to divide 12 by 2 such that the amount of change per iteration is less than 0.0001.

num_iter = 0
delta_iter = 1
new_num = 12.0

print("\n")

while delta_iter > 0.0001:
    new_num = new_num / 2
    delta_iter = new_num
    num_iter += 1

    print(f"{num_iter} {delta_iter}")

print(f"\nIt takes {num_iter} iterations for the change per iteration of the division to be less than 0.0001.")
print(f"The change per iteration is specifically {delta_iter}.")