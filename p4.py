class Solution(object):
    def productExceptSelf(self, arr):
        product = 1
        temp = []
        for i in range(len(arr)):
            if i ==0 :
                for j in range(i+1,len(arr)):
                    product *= arr[j]
            else:    
                if i == len(arr)-1:
                    for j in range (0,len(arr)-1):
                        product *= arr[j]
                else :
                    for j in range(0,i):
                        product *= arr[j]
                    for j in range(i+1 , len(arr)):
                        product *= arr[j]
            temp.append(product)
            product = 1
        return temp

sol = Solution()
nums1 = [1,2,3,4]
print(f"the product of {nums1} is -->",sol.productExceptSelf(nums1))
nums2 = [-1,1,0,-3,3]
print(f"the product of {nums2} is -->",sol.productExceptSelf(nums2))