"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # toplanti 5 de basladi diyelim ve 8 de bitti. Yani 5 den once bos ve 5 den once alicaksa yanlizca 5 e kadar alabilir yani 5 dahil degil. 
        # toplanti ayrica 8 de biticek yani bu demek oluyor bu kisi yanlizca 8 den sonra alabilir. 8 den once alamaz. baslangici ve bitisi de. 
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            A = intervals[i - 1]
            B = intervals[i]
            print(A.end, B.start)
            if A.end > B.start:
                return False
        return True