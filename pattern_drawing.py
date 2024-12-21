size = int(input("Enter the size of the pattern (positive integer): "))
row = 0
while row < size:
     for _ in range(size):  # The inner loop runs 'size' times
         print("*", end="")  # Print * without a newline
     print()
     row += 1
