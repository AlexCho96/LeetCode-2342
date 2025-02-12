# LeetCode - 2342. Max Sum of a Pair With Equal Sum of Digits

## Statement
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.


### Example 1
> **Input**: nums = [18,43,36,13,7] <br>
**Output**: 54 <br>
**Explanation**: The pairs (i, j) that satisfy the conditions are:  <br> - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.  <br> - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.  <br> So the maximum sum that we can obtain is 54.

### Example 2
> **Input**: nums = [10,12,19,14] <br>
**Output**: -1 <br>
**Explanation**: There are no two numbers that satisfy the conditions, so we return -1.