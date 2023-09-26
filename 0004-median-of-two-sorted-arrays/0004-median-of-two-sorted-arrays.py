class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=sorted(nums1+nums2)
        print(num3)
        print((1+len(num3)%2))
        print(num3[int(len(num3)/2)])
        if (len(num3))%2==0:
            print(" path1")
            x=(num3[int(len(num3)/2)] + num3[int(len(num3)/2)-1])/2 
        else:
            print("path2")
            x=num3[int(len(num3)/2)]
        return x