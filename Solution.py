class Solution:
    
    # 643 Maximum Average Subarray I
    def findMaxAverage(nums, k):
        result = []
        for i in range(k):
            y = [abs(x) for x in nums]
            current = max(y)
            if current in nums:
                result.append(current)
                nums.remove(current)
            else:
                result.append(-current)
                nums.remove(-current)
        answer = float(sum(result)/k)
        print(answer)
        return answer
    
    # 1456 Maximum number of Vowels in a substring of Given Length
    def maxVowels(s: str, k: int) -> int:
        vowel = ['a','e','i','o','u']
        num = 0
        times = 0
        str_length = 0
        answer = 0

        for i in s:
            while str_length < k:
                try:
                    if s[times+str_length] in vowel:
                        num +=1
                    str_length+=1
                except:
                    break
                
            if answer < num:
                answer = num
            num = 0
            str_length = 0
            times +=1
        print(answer)


    def isSubsequence(s: str, t: str) -> bool:
        i = 0
        j = 0
        while (i < len(s) and j < len(t)):
            if s[i] == t[j]:
                i+=1
            j+=1
        if i == len(s):
            print("True")
            return True
        else:
            print("False")
            return False
                    


if __name__ == "__main__":
    #Solution.findMaxAverage(nums=[1,12,-5,-6,50,3], k = 4)
    #Solution.maxVowels(s='abciiidef',k=3)
    Solution.isSubsequence(s='abc',t='ahbgdc')
