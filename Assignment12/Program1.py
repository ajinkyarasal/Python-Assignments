#Write a program which accepts one character and checks whether it is vowel or consonant.
#Input: a
#Output: Vowel

def CheckVowel(char):
    isVowel = False
    vowelList = ("a","e","i","o","u")
    for vowel in vowelList:
        if char.lower() == vowel.lower():
            isVowel = True
            return isVowel


def main():
    Result = False
    Result = CheckVowel("a")
    if Result:
        print("Vowel")
    else:
        print("Consonant")
    
if __name__ == "__main__":
    main()