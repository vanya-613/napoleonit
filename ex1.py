class Solution:
    def __init__(self):
        self.dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        '''convert Roman to Arabic numerals'''
        i = 0
        result = 0

        for i in range(0, len(s) - 1):
            # current character and value in Roman
            currentN = s[i]
            currentValue = self.dictionary[currentN]

            # next character and value in Roman
            nextN = s[i+1]
            nextValue = self.dictionary[nextN]

            if currentValue < nextValue:
                result -= currentValue
            else:
                result += currentValue

        # last symbol in Roman
        result += self.dictionary[s[-1]]

        return result
