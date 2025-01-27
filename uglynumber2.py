class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        n2, n3, n5 = 2, 3, 5
        p2, p3, p5 = 0, 0, 0

        for i in range(1,n):
            arr.append(min(n2,min(n3,n5)))

            if arr[i] == n2:
                p2+= 1
                n2 = arr[p2] * 2
            if arr[i] == n3:
                p3+= 1
                n3 = arr[p3] * 3
            if arr[i] == n5:
                p5+= 1
                n5 = arr[p5] * 5
                
        return arr[-1]



        