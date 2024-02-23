class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        def get_count( s):
            if len(s) == 0:
                return''
            string = ''
            curr_s = s[0]
            count = 1
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    string += (str(count)+curr_s)
                    curr_s = s[i]
                    count = 1
            string += (str(count) + curr_s)
            return string
        s = self.countAndSay(n-1)
        return get_count(s)