class Solution:
    def partitionLabels(self, s: str):
        def get_last_index(s, start, end, last_index):
            result = start
            while start < end:

                if last_index[s[start]] > result:
                    result = last_index[s[start]]
                    end = result
                start += 1
            return result
        def partition_labels(s):
            last_index = {}
            for index, letter in enumerate(s):
                last_index[letter] = index
            result = []
            current_index = 0
            prev_value = 0
            while current_index < len(s):
                current_index = get_last_index(s, current_index, last_index[s[current_index]], last_index) + 1
                result.append(current_index- prev_value)
                prev_value = current_index
            return result

        return partition_labels(s)