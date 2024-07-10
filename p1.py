class solution:
    def tobin(self,num):
        arr=[]
        for i in range(num+1):
            count = 0
            while i!=0:
                if i%2 ==1:
                    count+=1
                i = i//2
            arr.append(count)
        return arr          


sol = solution()
num = int(input("enter your number : "))
print(sol.tobin(num))
