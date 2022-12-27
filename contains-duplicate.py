class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        testArray = []
        for num in nums:
            if num in testArray:
                return True
            else:
                testArray.append(num)
        return False


array1 = [1, 2, 3, 4, 5, 6]
array2 = [1, 2, 1, 3, 4, 2]
array3 = [1, 2, 3, 4, 5, 1]
array4 = [2, 4, 6, 7, 8, 9]
solution = Solution()

print(solution.containsDuplicate(array1))
# results in false
print(solution.containsDuplicate(array2))
# results in true
print(solution.containsDuplicate(array3))
# results in true
print(solution.containsDuplicate(array4))
# results in false
