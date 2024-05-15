rolls = [(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)]

# Calculate the sum for each combination
sum_values = [sum(roll) for roll in rolls]

# Remove duplicates and sort the sum values
unique_sum_values = sorted(set(sum_values))

print("All possible sum values for three dice:")
print(unique_sum_values)