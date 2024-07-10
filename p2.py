class solution:
    def arrange(self,arr):
        count = 0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[count], arr[i] = arr[i], arr[count]
                count += 1
        return arr

sol = solution()
arr = [0,1,0,3,12]
print(sol.arrange(arr))
arr = [0]
print(sol.arrange(arr))