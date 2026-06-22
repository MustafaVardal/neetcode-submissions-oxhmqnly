class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A
        
        l = 0

        r = len(A)

        total_len = len(A) + len(B)
        half_len = (total_len + 1) // 2

        while l <= r:
            mid_left= l + (r - l) // 2
            j = half_len - mid_left

            Aleft = A[mid_left - 1] if mid_left > 0 else float('-inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Aright = A[mid_left] if mid_left < len(A) else float('inf')
            Bright = B[j] if j < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total_len % 2 == 1:
                    return float(max(Aleft, Bleft))
                
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            if Aleft > Bright:
                r = mid_left - 1
            else:
                l = mid_left + 1