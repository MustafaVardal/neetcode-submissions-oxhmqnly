class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0

        currSum = sum(arr[:k - 1])

        for l in range(len(arr) - k + 1):
            currSum += arr[l + k - 1]
            if currSum / k >= threshold:
                count += 1
            currSum -= arr[l]
        return count
