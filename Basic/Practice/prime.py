# Problem Description
# A math game is introduced in a school competition to test the skills of students. The game deals with Prime numbers.
# The game rules are as follows:
# From the given set of distinct natural numbers as input, consider the smallest natural number as q.
# Your task is to compute the smallest prime number (p) such that when p is divided by all the distinct numbers in the input, except q, should result q as the remainder.
# Constraints
# 1 < n < 11
# p < 10 ^ 10
# Input
# Input consists of n+1 number of distinct natural numbers separated by spaces.
# Output
# Print single integer p if such a p exists, else print "None".
# Time Limit (secs)
# 1
# Examples
# Input: 3 4 5 1
# Output: 61
# Explanation:
# Here the n+1 numbers are 3, 4, 5 and 1 where q=1 (the least of the numbers)
# The smallest number that leaves remainder 1 when divided by 3, 4 and 5 is 61 and is prime. Hence, output is 61.
# Example 2
# Input: 3 4 5 2
# Output: None
# Explanation
# Here q=2. Any number that when divided by 4 leaving remainder 2 must be an even number e.g., 6, 10, 14 etc. Hence it can't be prime. Hence, output is "None"

input_numbers = input("Enter a space-separated list of numbers: ")
numbers = list(map(int, input_numbers.split()))

def is_prime(a):
    if a == 1:
        return True
    if a==2:
        return False
    if a <= 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            return False
        i += 6
    return True

if len(numbers) >= 3:
    expected_numbers = list(range(3, numbers[0] + 3))  # Expected natural numbers
    first_three_numbers = numbers[:3]  # First three numbers in the list
    last = numbers[-1]

    if first_three_numbers == expected_numbers and is_prime(last) == True:
        product_first_three = first_three_numbers[0] * first_three_numbers[1] * first_three_numbers[2]
        sum_remaining = product_first_three + is_prime(last)

        print(f"Sum of the remaining numbers: {sum_remaining}")
    else:
        print("None")
else:
    print()
