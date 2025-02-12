from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumDigits(a):
            sum_digits_a = 0
            while a:
                sum_digits_a, a = sum_digits_a + a%10, a//10
            return sum_digits_a

        def checkMaxSumList(list_nums):
            max_sum = 0
            for i in range(len(list_nums)):
                for j in range(i, len(list_nums)):
                    if max_sum <= list_nums[i]+list_nums[j] and i != j:
                        max_sum = list_nums[i]+list_nums[j]
                        new_list = [list_nums[i],list_nums[j]]
            return max_sum, new_list

        nums_sum_digit, sol, max_sum = [sumDigits(x) for x in nums], {}, -1
        for i in range(len(nums_sum_digit)):
            if nums_sum_digit[i] not in list(sol.keys()):
                sol[nums_sum_digit[i]] = [nums[i]]
            else:
                sol[nums_sum_digit[i]].append(nums[i])
                possible_sum, sol[nums_sum_digit[i]] = checkMaxSumList(sol[nums_sum_digit[i]])
                if max_sum <= possible_sum:
                    max_sum = possible_sum
        return(max_sum)