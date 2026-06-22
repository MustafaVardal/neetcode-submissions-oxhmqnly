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
            m  = l + (r - l) // 2
            h_m = half_len - m

            Aleft = A[m - 1] if m > 0 else float('-inf')
            Aright = A[m] if m <len(A) else float('inf')
            Bleft = B[h_m - 1] if h_m > 0 else float('-inf')
            Bright = B[h_m] if h_m < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if (total_len % 2) == 1:
                    return max(Aleft, Bleft)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            if Aleft > Bright:
                r = m - 1
            else:
                l = m + 1