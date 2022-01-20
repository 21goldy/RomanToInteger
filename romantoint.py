from os import system
system("cls")

def romanToInt(s: str) -> int:
    letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    # MCMXCIV
    i = len(s)-1
    while i >= 0:
        if i>0 and letters[s[i]] > letters[s[i-1]]:
            n += letters[s[i]] - letters[s[i-1]]
            i -= 2
        else:
            n += letters[s[i]]
            i -= 1

    return n

print(romanToInt('IV'))        # 4
print(romanToInt('MCMXCIV'))   # 1994
print(romanToInt('MMMDCCCXC')) # 3890
print(romanToInt('XLIX'))      # 49