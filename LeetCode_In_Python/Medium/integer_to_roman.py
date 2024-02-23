class Solution:
    def intToRoman(self, num: int) -> str: 
        d = {'1000':'M','900':'CM','500':'D','400': 'CD','100':'C', '90':'XC','50' : 'L', '40':'XL', '10':'X', '9':'IX', '5':'V', '4':'IV','1':'I' }
        roman = ''
        while num >= 1:
            for key, value in d.items():
                if num >= int(key):
                    if len(value) == 1:
                        divided = (num //int(key))
                        roman = roman + (divided * value)
                        num = num - ((divided * int(key)))
                    else:
                        roman += (value)
                        num = num - int(key)
        return roman
