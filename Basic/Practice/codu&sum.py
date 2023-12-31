# Codu and Sum Love 
# Given N number of x's, perform logic equivalent of the above Java code and print the output

# Problem Description
# Scanner sc = new Scanner(System.in);

# long sum = 0;

# int N = sc.nextInt();

# for (int i = 0; i < N; i++) {

# final long x = sc.nextLong(); // read input

# String str = Long.toString((long) Math.pow(1 << 1, x));

# str = str.length() > 2 ? str.substring(str.length() - 2) : str;

# sum += Integer.parseInt(str);

# }

# logger.debug(sum%100);

# Given N number of x's, perform logic equivalent of the above Java code and print the output

# Input
# First line contains an integer N

# Second line will contain N numbers delimited by space

# Output
# Number that is the output of the given code by taking inputs as specified above

# Constraints
# 1<=N<=10^7

# 0<=x<=10^18

# Difficulty Level
# Simple

# Time Limit (secs)
# 1

# Examples
# Example 1

# Input

# 4

# 8 6 7 4

# Output

# 64

# Example 2

# Input

# 3

# 1 2 3

# Output

# 14