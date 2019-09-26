#01
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

#02
import copy
class Solution:
    

    def myDeepCopy(self,a):
        if (isinstance(a, list) or isinstance(a, tuple)):
            return [self.myDeepCopy(element) for element in a]
        else:
            return copy.copy(a)

    
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row=len(A)
        col=len(A[0])
        print(row,col)
        x=[[1]*row]*col
        x=self.myDeepCopy(x)
        print(x)
        for i in range(len(x)):
            for j in range(len(x[i])):
                x[i][j]=A[j][i]
        return x

#03
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
#04
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

#05
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst=[]
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                print("Fizz")
                lst.append("Fizz")
            elif i%5==0 and i%3!=0:
                print("Buzz")
                lst.append("Buzz")
            elif i%5==0 and i%3==0:
                print("FizzBuzz")
                lst.append("FizzBuzz")
            else:
                print(i)
                lst.append(str(i))
        return lst
#06
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        X=map(str,digits)
        B= "".join(X)
        c=int(B)
        c=c+1

        v=map(int,str(c))
        
        return (list(v))
#07
class Solution:
    def titleToNumber(self, s: str) -> int:
        see=[]
        for i in range(len(s)):
            x=ord(s[len(s)-(i+1)])-64
            sums=x*(26**i)
            see.append(sums)
        return sum(see)

#08
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x = x*2
        return x==n
#09
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

#10
    not attempted
#11

class Solution:
    def reverseWords(self, s: str) -> str:
     #   print(len(s))
        lst=[]
        x=s.split()
      #  print(len(x))
       # print(x)
        for i in range(len(x)):
            a=list(reversed(x[i]))
        #    print(a)
            v=''.join(a)
            lst.append(v)
        
        c=' '.join(lst)
        z=print('"'+c+'"')
        return z
#attempted but wrong answer


#12
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [val.lower() for val in s if val not in string.punctuation and val not in string.whitespace]
        return s[:] == s[::-1]
#13
    not attempted
#14
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = ""
        if not strs: return l
        s = min(strs, key=len)
        for i in range(len(s)):
            if all([x.startswith(s[:i+1]) for x in strs]):
                l = s[:i+1]
            else:
                break
        return l
#15
class Solution:
    def findComplement(self, num: int) -> int:
        a=list(bin(num))
        a=a[2:]
        lst=[]
        print(a)
        for i in range(len(a)):
            if a[i]=='1':
                lst.append('0')
            else:
                lst.append('1')
        print(lst)
        lst=''.join(lst)
        print(lst)
        return int(lst,2)
#16
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a= bin(x)[2:]
        b= bin(y)[2:]
        print(a)
        print(b)
        if len(a)<len(b):
            v=len(b)-len(a)
            a='0'*v+a
            print(a)
        else:
            v=len(a)-len(b)
            b='0'*v+b
        c=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                c=c+1
        return c
        print(c)
            

#17
class Solution:
    def binaryGap(self, n: int) -> int:
        return max((lambda x: [x[i+1]-x[i] for i in range(len(x)-1)])([i for i,j in enumerate(bin(n)) if j == '1']), default = 0)
#18
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

#19
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x=target-nums[i]
            
            if x in nums and nums.index(x)!=i:
                return ([i,nums.index(x)])

#20
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        a=sorted(s, reverse=True)
        b=sorted(t, reverse=True)
        if(len(a)==len(b)):
            for i in range(len(a)):
                if a[i]!=b[i]:
                    return False
            return True
        return False

#union find
    not attempted
    
