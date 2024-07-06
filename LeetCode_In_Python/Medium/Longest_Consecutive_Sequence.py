class Solution:
    def longestConsecutive(self, nums):
        self.max = 0
        self.longest_consecutive_sequence(nums)
        return self.max

    def longest_consecutive_sequence(self,nums):
        nums_set = set(nums)
        sequence_dict = {}
        max = 0
        for num in nums:
            if num not in sequence_dict:
                self.find_sequences(num, nums_set, sequence_dict)
        print(sequence_dict)


    def find_sequences(self,num,nums, sequence_dict, cur=0):
        if num + 1 in nums:
            if num+1 in sequence_dict:
                ans = sequence_dict[num+1] + 1
            else:
                ans = self.find_sequences(num+1, nums, sequence_dict) + 1
        else:
            ans = 1
        sequence_dict[num] = ans
        if ans > self.max:
            self.max = ans
        return sequence_dict[num]