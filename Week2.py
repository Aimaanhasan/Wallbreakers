class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0 
        for i in S:
            if i in J:
                count=count+1
        return count

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

    # Full table of Morse Code for every English letter
        morse_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    # Dictionary of translated words
        seen = {}
    
    # Translate every english word to Morse Code
        for word in words:
            morse_word = ""
            for letter in word:
                # Access Morse Code table using ASCII values
                morse_word += morse_table[ord(letter) - ord('a')]

            # Check if Morse Code word already seen then add it
            if morse_word not in seen:
                seen[morse_word] = word

    # Return number of unique Morse Code words
        return len(seen)

class Solution:
    # compute the next sum square
    def check(self, x: int):
        s = 0
        while x != 0:
            s += (x%10)**2
            x //= 10
        return s
		
    def isHappy(self, n: int) -> bool:
	    # regiester first element
        note = {n: 1}
		# repeat till a new check(n) occur second time in out "note" or if number became 1
        while n != 1:
            n = self.check(n)
            if n in note:
                return False
            note[n] = 1 # register every new computed sum
        return True



class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A=A.split()
        B=B.split()
        lst=[]
        for i in range(len(A)):
            if count[i]==1:
                if A[i] not in B[i]


class Solution(object):
    def distributeCandies(self, candies):
        mySet = set(candies)
        l1 = len(mySet)
        l2 = len(candies) / 2
        
        if l2 >= l1:
            return int(l1)
        else:
            return int(l2)


from collections import Counter

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len({tuple(tuple(sorted(Counter(S[j::2]).items())) for j in range(2)) for S in A})

    class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        c=a.intersection(b)
        return (list(c))

    #incomplete
    class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)
        f= '.'
        for i in board:
            for j in i:
                if j != f:
                    if board.count(j)>1:
                        return False
            print('rowchecked')
        
        a=0
        lst=[]
        bools=True
        
        while bools:
            for i in board:
                if i[a] !=f:
                    lst.append(i[a])
            a=a+1
            if len(lst)==9:
                bool=False
        
                

    class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        v=[]
        count1=[]
        count2=[]
        
        for i in range(len(s)):
            v.append((s[i],t[i]))
        print(v)
        for i in range(len(s)):
            count1.append(s.count(s[i]))
        
            count2.append(t.count(t[i]))
        if count1==count2:
            
            return True
        else:
            return False

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def pat(a, bw, cs):
            for n in cs:
                if n in bw:
                    a.append(bw.index(n))
                else:
                    bw.append(n)
                    a.append(bw.index(n))
            return a
        pn, ps, strl = [], [], str.split()
        pn = pat([], [], pattern)
        ps = pat([], [], strl)
        if pn == ps:
            return True
        else:
            return False

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=6
        self.map= [None]*self.size
        
    def gethash(key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        keyhash= gethash(key)
        keyvalue= [key,value]
        if self.map[keyhash] is None:
            self.map[keyhash]=list([keyvalue])
            return True 
        else:
            for i in self.map[keyhash]:
                if i[0]==key:
                    i[1]=value
                    return True
        self.map[keyhash].append(keyvalue)
        return True 

        
        
    
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        keyhash=self.gethash(key)
        if self.map[keyhash] is not None:
            for i in self.map[keyhash]:
                if i[0]==key:
                    return i[1]
            else:
                return None
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        keyhash=self.gethash(key)
        if self.map[keyhash]==None:
            return False
        else:
            for i in range(0,len(self.map[keyhash])):
                if self.map[keyhash][i][0]==self.key:
                    self.map[keyhash].pop(i)
                    return True
        


# Your MyHashMap object will be instantiated and called as such:
#obj = MyHashMap()
#obj.put(key,value)
#param_2 = obj.get(key)
#obj.remove(key)


#hashset not implemented


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d=[]
        e=[]
    #print(s)
    #print(p)
        w=collections.Counter(p)
    #print(w)
        for i in range(len(s)):
            a=(s[i:len(p)])
            c=collections.Counter(a)
        
        #print(c)
            p=" "+p
            if w==c:
                print(s[i:len(p)])
           # print('hello')
                #d.append(s[i:len(p)])
                e.append(i)
            
            #print(p)
        #        d.append((s[i],i))
                
         #       i=i+1
          #  i=i+1
    #print(d)
        return e
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=collections.Counter(s)
        for i in range(len(s)):
            
            if c[s[i]]==1:
                return i 
        return -1

# subdomain visit count not implemented

import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c=collections.Counter(s)
        d=collections.Counter(t)
        e=d-c
        print(e)
        f="".join(list(e.elements()))
        return f
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #remove commas and spaces and replace the banned word from the paragraph with ""
        curoccur = 0
        banset = set(banned)
        maxword = ""
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paraList = paragraph.lower().split()
        for word in paraList:
            count = paraList.count(word)
            if count > curoccur and word not in banset:
                maxword = word
                curoccur = count
        return maxword

import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        x=sorted(s,reverse=True)
        print(x)
        return "".join(map(str,x))

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s,n=sum(set(nums)),len(nums)
        return [sum(nums)-s,n*(n+1)//2-s]

#no of atoms not implemented

class Trie():
    head={}
    
    def add(self,word):
        cur=self.head
        for i in word:
            if i not in cur:
                cur[i]={}
            cur=cur[i]
        cur['*']=True
    def Search(self,word):
        cur=self.head
        for i in word:
            if i not in cur:
                return False
            cur=cur[i]
        if '*' in cur:
            return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur =self.head
        for i in prefix:
            if i not in cur:
                return False
            cur = cur[i]
        return True

class Solution:
    
    def longestWord(self, words: List[str]) -> str:
        a = Trie()
        words.sort()
        for i in words:
            a.add(i)
        print(words)
        count=0
        while True:
            bools=False
            z = None
            while bools == False:
                z= max(words,key=len)
                print(z)
                st=z[0]
                for i in range(1,len(z)):
                    if a.Search(st):
                        st=st+z[i]
                        print(st)
                        bools = True
                    else:
                        bools = False
                        break

                words.remove(z)
            break
        return z
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head={}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur =self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        # * denotes the Trie has this word as item
        # if * doesn't exist, Trie doesn't have this word but as a path to longer word
        cur['*'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur =self.head
        for i in word:
            if i not in cur:
                return False
            cur=cur[i]
        if '*' not in cur:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur =self.head
        for i in prefix:
            if i not in cur:
                return False
            cur = cur[i]
        return True
            

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


#wwwordsearch ii not implemented 
