# Sports Stadium
# It is the sports event of the year for the residents of Sportsville.  Their team had finally made it to the finals of the Bowls League Cup.

# Problem Description
# It is the sports event of the year for the residents of Sportsville.  Their team had finally made it to the finals of the Bowls League Cup.

# They have booked tickets for the city contingent for the same row, and the size of the contingent (N) is smaller than the number of seats booked(S).Unfortunately, there was rain the previous night and some of the seats are still wet. Some of the contingent love Bowls so much and are excited enough not to mind sitting on a wet chair. There are k of these. However, others want to sit on a dry seat so that they can enjoy the match more.

# The contingent wants to minimize the distance between the first and last person in the row so that they can still conduct Mexican Waves, and other forms of support for their team.

# Because they want to sit together, any block of 15 or more contiguous unoccupied seats between the first person sitting and the last person sitting is unacceptable.

# There are M blocks of seats, starting with a dry block, with alternating wet and dry blocks.  The number of seats in each block is known.

# Given S (the number of seats in the row), N (the size of the contingent),k (the number of the contingent who are willing to sit in a wet seat), and the distribution of wet and dry blocks, write a program to find the minimum distance between the first and the last member of the contingent in the row.


# Input
# The first line contains four comma separated numbers representing S, N, k and M respectively.

# The second line is a set of M comma separated numbers representing the number of seats in each block of seats.  The first block is dry, and the remaining blocks alternate between wet and dry.

# Output
# One integer representing the minimum distance between the first and last member of the row.  If it is impossible to seat all the members according to their preferences,and with the unoccupied seat restriction,  the result should be 0.

# Constraints
# S,N,k < 1000,  M < 30

# Difficulty Level
# Complex

# Time Limit (secs)
# 1

# Examples
 

# Example 1

# Input 

# 100,50,5,6

# 3,10,30,5,30,22

# Output

# 49

# Explanation

# S = 100, and there are 100 seats in the row.  N=50, and there are 50 members in the contingent. k=5, and 5 people (out of the 50) do not mind sitting on wet seats.  M=6, and there are 6 blocks of seats.  The number of seats in each block is 3,10,30,5,30 and 22, with the first block of 3 seats being dry, the next 10 being wet and so on. 

# One possible positioning to achieve the minimum distance is to place the a set of 30 people in seats 14 to 43 (the dry block), the 5 people who do not mind sitting on wet seats in the wet block 44 to 48, and the remaining 15 people (of the 50) in the seats 49 to 63.  There is no unoccupied seat between the first person and the last person, and so this is acceptable.The distance between the last allocated seat (63) and the first allocated seat (14), is 49.  This is the output.

 

# Example 2

# Input 

# 100,50,5,8

# 3,7,10,10,20,10,20,20

# Output

# 64

# Explanation

# S = 100, and there are 100 seats in the row.  N=50, and there are 50 members in the contingent. k=5, and 5 people (out of the 50) do not mind sitting on wet seats.  M=8, and there are 8 blocks of seats. 

# One possible positioning is to have a set of 10 people sit in the dry block 11 â€“ 20, the 5 people who will accept wet seats in seats 21 â€“ 25 (in the wet block 21 â€“ 30), another 20 people in the dry block 31 â€“ 50, leave the wet block 51-60 empty, and seat the remaining 15 people in seats 61 â€“ 75 (in the dry block 61-80.  There is a block of 5 unoccupied seats (26-30) between the first person and the last person.  As this is not more than 15, this is acceptable. The distance from the last allocated seat (75) and the first allocated seat (11) is 64.  This is the result.