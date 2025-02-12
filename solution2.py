from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumDigits(a):
            sum_digits_a = 0
            while a:
                sum_digits_a, a = sum_digits_a + a%10, a//10
            return sum_digits_a
        
        dict_nums, max_sum = {}, -1
        for num in nums:
            sum_digits = sumDigits(num)
            if sum_digits not in dict_nums:
                dict_nums[sum_digits] = [num]
            else:
                dict_nums[sum_digits].append(num)
                dict_nums[sum_digits] = sorted(dict_nums[sum_digits], reverse=True)[:2]

        for key in dict_nums:
            if len(dict_nums[key]) >= 2 and max_sum <= sum(dict_nums[key]):
                max_sum = sum(dict_nums[key])
        return(max_sum)