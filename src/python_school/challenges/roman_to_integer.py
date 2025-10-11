# 13. Roman to Integer
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.



# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class RomanToInteger:
    """
    A class to convert Roman numerals to integers.
    """
    
    @staticmethod
    def roman_to_integer(s: str) -> int:
        """
        Converts a Roman numeral string to an integer.
        
        The method iterates through the Roman numeral string from right to left,
        converting it to an integer. It handles the subtractive cases (e.g., IV, IX).

        :param s: The Roman numeral string (e.g., "MCMXCIV").
                  Constraints: 1 <= len(s) <= 15, s contains only valid Roman numeral characters.
        :type s: str
        :return: The integer representation of the Roman numeral (e.g., 1994).
        :rtype: int
        """
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for char in reversed(s):
            curr_value = roman_map[char]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value
        return total
    
    def roman_to_integer_old(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (15 <= len(s) <= 1):
            return 0
        if any(char not in "IVXLCDM" for char in s):
            return 0
        previousChar = ""
        total = 0
        for char in s[::-1]:
            if (0 > total > 3999):
                return 0
            if char == "I":
                if previousChar and previousChar[0] in ("V", "X"):
                    total -= 1
                else:
                    total += 1
            elif char == "V":
                total += 5
            elif char == "X":
                if previousChar and previousChar[0] in ("L", "C"):
                    total -= 10
                else:
                    total += 10
            elif char == "L":
                total += 50
            elif char == "C":
                if previousChar and previousChar[0] in ("D", "M"):
                    total -= 100
                else:
                    total += 100
            elif char == "D":
                total += 500
            elif char == "M":
                total += 1000
            previousChar = char + previousChar
        return total

if __name__ == "__main__":
    solver = RomanToInteger()
    # Example 1:
    print(f"Input: III, Output: {solver.roman_to_integer('III')}")
    # Example 2:
    print(f"Input: LVIII, Output: {solver.roman_to_integer('LVIII')}")
    # Example 3:
    print(f"Input: MCMXCIV, Output: {solver.roman_to_integer('MCMXCIV')}")