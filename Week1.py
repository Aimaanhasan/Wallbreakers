class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        lst=[]
        lst1=[]
        lst2=[]
        if len(A)>=1 and len(A)<=5000:
            for i in range(len(A)):
                if A[i]>=0 and A[i]<=5000:
                    if A[i]%2==0:
                        lst1.append(A[i])
                    else:
                        lst2.append(A[i])
        lst=lst1+lst2
        return lst

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        transpose=[[]]
        for i in range(len(A)):
            for j in range(len(A[i])):
                a=A[i][j]
                A[i][j]=A[j][i]
                A[j][i]=a
        

A=[[1,2,3],[4,5,6],[7,8,9]]


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst=[]
    
        for i in range(left,right+1):
            lst1=[]
            a=list(str(i))
            if "0" not in a:
                for j in range(len(a)):
                    x=int(a[j])
                    if i%int(a[j])==0:
                        lst1.append(a[j])
            if a==lst1:
                lst.append(i)


        print(lst)
        return lst

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i].reverse()
            for j in range(len(A[i])):
                if A[i][j]==0:
                    A[i][j]=1
                else:
                    A[i][j]=0

        return A

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        X=map(str,digits)
        B= "".join(X)
        c=int(B)
        c=c+1

        v=map(int,str(c))
        
        return (list(v))

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst=[]
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                lst.append("Fizz")
            elif i%5==0 and i%3!=0:
                lst.append("Buzz")
            elif i%5==0 and i%3==0:
                lst.append("FizzBuzz")
            else:
                lst.append(str(i))
        return lst

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            a=s[i]
            s[i]=s[-i-1]
            s[-i-1]=a
        print(s)
            

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lst=[]
        lst.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i] not in lst:
                lst.append(nums[i])
            elif nums[i] in lst:
                lst.remove(nums[i])
        return lst[0]
            
