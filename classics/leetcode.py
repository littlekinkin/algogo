class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dd = {}
        for index, value in enumerate(nums):
            dd[value] = index
        for index, value in enumerate(nums):
            sub = target - value
            if sub in dd and index != dd[sub]:
                return [index, dd[sub]]
    def best_twoSum(self, nums, target):
        dd = {}
        for i in range(len(nums)):
            if nums[i] in dd:
                return [dd[nums[i]], i]
            else:
                dd[target - nums[i]] = i

    def lengthOfLongestSubstring(self, s):
        '''uniq'''
        curr = ''
        max_len = 0
        for w in s:
            if w not in curr:
                curr += w
            else:
                max_len = max(max_len, len(curr))
                index = curr.index(w)
                curr += w
                curr = curr[index+1:]
        return max(max_len, len(curr))

    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        total = n + m
        if total % 2:
            return self.find_kth()

    def find_kth(self, A, m, B, n, k):
        if m > n: return self.find_kth(B, n, A, m, k)
        if m == 0: return B[k-1]
        if k == 1: return min(A[0], B[0])
        ia = min(k/2, m)
        ib = k - ia
        if A[ia - 1] < B[ib -1]:
            return self.find_kth(A[ia:], m-ia, B, n, k-ia)
        elif A[ia - 1] > B[ib -1]:
            return self.find_kth(A, m, B[:-ib], n-ib, k-ib)
        else:
            return A[ia -1]

    def longestPalindromicSubstring(self, s):
        pass


        



if __name__ == '__main__':
    sl = Solution()
    print(sl.twoSum([2,7,11,15], 9))
    print(sl.best_twoSum([2,7,11,15], 9))
    print(sl.lengthOfLongestSubstring('abcabcbb'))
    print(sl.lengthOfLongestSubstring('bbbbb'))
    print(sl.lengthOfLongestSubstring('pwwkew'))
