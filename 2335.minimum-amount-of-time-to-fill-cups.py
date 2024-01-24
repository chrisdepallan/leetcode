#
# @lc app=leetcode id=2335 lang=python3
#
# [2335] Minimum Amount of Time to Fill Cups
#

# @lc code=start


class Solution:
    def fillCups(self, amount: List[int]) -> int:
       
        ans = 0
        while sum(amount):
            amount.sort()
            ans += 1
            amount[2] -= 1
            amount[1] = max(0, amount[1] - 1)
        return ans
        

            
        # return count
# @lc code=end

