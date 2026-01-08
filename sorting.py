class sorting():
    def __init__(self,data):
        self.data=data
        self.length=len(self.data)
    def selection_sort(self):
        for i in range(0,self.length):
            smallest=i
            for j in range(i+1,self.length):
                if self.data[smallest]>self.data[j]:
                    smallest=j
            self.data[i],self.data[smallest]=self.data[smallest],self.data[i]
        return self.data
    
    def bubble_sort(self):
        for i in range(self.length-1,-1,-1):
            for j in range(0,i):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
        return self.data
            
    def insertion_sort(self):
        for i in range(1,self.length):
            if self.data[i]<self.data[i-1]:
                smallest=self.data[i]
                for j in range(i-1,-1,-1):
                    if smallest<self.data[j]:
                        self.data[j+1]=self.data[j]
                self.data[j]=smallest
        return self.data
    
    def merge_list(self,left,right):
        left_len,right_len=len(left),len(right)
        i,j=0,0
        result=[]
        while i<left_len and j<right_len:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<left_len:
            result.append(left[i])
            i+=1
        while j<right_len:
            result.append(left[j])
            j+=1

        return result
    
    def divide_list(self,nums):
        if len(nums)==1:
            return nums
        mid=len(nums)//2
        left= self.divide_list(nums[:mid])
        right= self.divide_list(nums[mid:])
        return self.merge_list(left,right)
    
    def partition(self,nums,low,high):
        pivot=nums[low]
        i=low
        j=high
        while i<j:
            while nums[i]<=pivot and i<=high-1:
                i+=1
            while nums[j]>pivot and j>=low+1:
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
        nums[low],nums[j]=nums[j],nums[low]
        return j

    def quick_sort(self,nums,low,high):
        if low<high:
            pivot_index=self.partition(nums,low,high)
            self.quick_sort(nums,low,pivot_index-1)
            self.quick_sort(nums,pivot_index+1,high)
        return nums


nums=[9,8,7,6,5,4,3,2,1]
n=len(nums)
sorted_list=sorting(nums)
print(sorted_list.quick_sort(nums,0,n-1))

