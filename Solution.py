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


if __name__ == "__main__":
    Solution.findMaxAverage(nums=[1,12,-5,-6,50,3], k = 4)