def reverse_array(arr):
    i,j=0 ,len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
        return arr
print(reverse_array([1,2,3,4,5])) 
# Time: O(n) • Space: O(1)
def min_mx(arr):
    if not arr:
        return None,None
    mn=mx=arr[0]
    for x in arr:
        if x<mn:
            mn=x
        if x>mx:
            mx=x
    return mn,mx
print(min_mx([3,1,4,1,5,9,2,6,5,3,5]))
# Time: O(n) • Space: O(1)
def sum_array(arr):
    total=0
    for x in arr:
        total+=x
    return total
print(sum_array([1,2,3,4,5]))
# Kth largest / Kth smallest
import heapq
from multiprocessing import heap 
def kth_largest(arr,k):
    if k <1 or k >(len(arr) ):
        return None
    return heapq.nlargest(k,arr)[-1]
print(kth_largest([3,1,4,1,5,9,2,6,5,3,5],3))

def kth_smallest(arr,k):
    if k <1 or k >(len(arr) ):
        return None
    return heapq.nsmallest(k,arr)[-1]
print(kth_smallest([3,1,4,1,5,9,2,6,5,3,5],3))
# Time: O(n log k) • Space: O(k)

# Sort array of 0s, 1s and 2s (Dutch National Flag)

def sort_012(arr):
    low,mid,high=0,0,len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
print(sort_012([2,0,1,2,0,1,1,0]))
# Time: O(n) • Space: O(1)

# Move all negative elements to one side (partition)       
def move_negatives(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1

    return arr
print(move_negatives([12,-7,5,-3,9,-1,0,4,-6]))
# Time: O(n) • Space: O(1)

def union_sorted(a,b):
    i,j=0,0
    res=[]
    while i <len(a) and j<len(b):
        if a[i]<b[i]:
            if not res or res[-1]!=a[i]:
                res.append(a[i])
            i+=1
        elif a[i]>b[j]:
            if not res or res[-1]!=b[j]:
                res.append(b[j])
            j+=1
        else:
            if not res or res[-1]!=a[i]:
                res.append(a[i])
            i+=1
            j+=1
    while i <len(a):
        if not res or res[-1]!=a[i]:
            res.append(a[i])
        i+=1                          
    while j <len(b):
        if not res or res[-1]!=b[j]:
            res.append(b[j])
        j+=1
    return res
print(union_sorted([1,2,4,5],[2,3,5,6]))


def duplicate(arr):
    seen=set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False
print(duplicate([1,2,3,4,5,3]))

# find first duplicate element in array
def duplicate_elemets(arr):
    seen=set()
    for n in arr:
        if n in seen:
            return n 
        seen.add(n)
    return None
print(duplicate_elemets([1,2,3,4,5,3]))
# Time: O(n) • Space: O(n)

# Find all duplicates in an array
def all_duplicates(arr):
    seen=set()
    duplicates=set()
    for n in arr:
        if n in seen:
            duplicates.add(n)
        else:
            seen.add(n)
    return duplicates   
print(all_duplicates([1,2,3,4,5,3,2,6,4]))
# Time: O(n) • Space: O(n)




# floyd's cycle 
def find_duplicate(nums):
    slow=nums[0]
    fast=nums[0]
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break
    slow=nums[0]
    while slow!=fast:
        slow=nums[slow]
        fast=nums[fast]
    return slow
print(find_duplicate([1,3,4,2,2]))   


# Time: O(n) • Space: O(1)
# valid anagrams
def are_anagarms(s1,s2):
    if len(s1)!=len(s2):
        return False
    r=sorted(s1)
    s=sorted(s2)
    if r==s:
        return True
    return False
print(are_anagarms("listen","silent"))

# Time: O(n log n) • Space: O(n)

# two sum
def two_sum_exist(arr,target):
    seen=set()
    for num in arr:
        complement=target-num
        if complement in seen:
            return True
        seen.add(num)
    return False
print(two_sum_exist([1,2,3,4,5],9))

# Time: O(n) • Space: O(n)
def two_sum(nums,target):
    seen={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return (seen[complement],i) # complement is key that stores index
        seen[num]=i #store num with index
    return None
print(two_sum([1,2,3,4,5],9))
# Suppose nums = [1,2,3,4,5] and target = 9. As the loop runs:
# i=0, num=1 → store seen[1] = 0
# i=1, num=2 → store seen[2] = 1
# i=2, num=3 → store seen[3] = 2
# i=3, num=4 → store seen[4] = 3
# i=4, num=5 → compute complement = 9 - 5 = 4. Now 4 in seen is True, and seen[4] yields 3. 
# Returning (seen[4], 4) gives indices (3, 4) which point to values 4 and 5 that sum to 9.

def group_anagrams(strs):
    group={}
    for word in strs:
        key=tuple(sorted(word))
        if key not in group:
            group[key]=[]
        group[key].append(word)
    return list(group.values()) 
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# Time: O(n k log k) • Space: O(n k) where n is
# Why tuple?
# Because dictionary keys must be immutable
# List cannot be a key, but tuple can
# So this key helps group anagrams correctly.

def top_k_frequent(nums,k):
    freq={}
    for n in nums:
        freq[n]=freq.get(n,0)+1
    import heapq
    heap=[]
    for num,count in freq.items():
        heapq.heappush(heap,(-count,num))  
    result=[]
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])    
    return result
print(top_k_frequent([1,1,1,2,2,3],2))
# Time: O(n log k) • Space: O(n)

def top(nums,k):
    freq={}
    for n in nums:
        freq[n]=freq.get(n,0)+1
    heap=[]
    for num,count in freq.items():
        heapq.heappush(heap,(-count,num))
        result=[]
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    return result
print(top([1,1,1,2,2,3],2))


# encode and decode
def encode(strs):
    encoded=""
    for s in strs:
        encoded+=str(len(s))+"#"+s
    return encoded

def decode(s):
    res=[]
    i=0
    while i <len(s):
        j=i
        while s[j]!="#":
            j+=1
        length=int(s[i:j])
        j+=1
        word=s[j:j+length] # Advance i to j + length to read the next encoded item.
        res.append(word)    
        i=j+length
    return res

def product_array_except_self(nums):
    n=len(nums)
    result=[1]*n

    prefix=1
    for i in range(n):
        result[i]=prefix
        prefix*=nums[i]

    suffix=1
    for i in range(n-1,-1,-1):
        result[i]*=suffix
        suffix*=nums[i]
    return result
print(product_array_except_self([1,2,4,6]))        

def isValidSudoku(board):
    rows=[set() for _ in range(9)]
    columns=[set() for _ in range(9)]
    boxes=[set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            val=board[r][c]
            if val==".":
                continue
            if val in rows[r]:
                return False
            rows[r].add(val)

            if val in columns[c]:
                return False
            columns[c].add(val)
            box_index=(r//3)*3 +(c//3)
            if val in boxes[box_index]:
                return False
            boxes[box_index].add(val)
    return True
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8
# For a cell at (r, c):

# Box index = (r // 3) * 3 + (c // 3)
# Example:
# If (r,c) = (4,5) → middle right box:

# (4//3)=1
# (5//3)=1

# → 1*3 + 1 = 4 → box 4

def longest_consecutive(nums):
    num_set=set(nums)
    longest=0
    for num in num_set:
        if num-1 not in num_set:
            length=1
            current=num
        while current+1 in num_set:
            current+=1
            length+=1    
            longest=max(longest,length)
    return longest

def is_palindrome(s):
    cleaned="".join(c.lower() for c in s if c.isalnum())
    return cleaned==cleaned[::-1]

def is_plaindrome(s):
    left,right=0,len(s)-1
    while left<right:
        while left< right and not s[left].isalnum():
            left+=1
        while left< right and not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True
print(is_palindrome("A man, a plan, a canal: Panama"))
# Time: O(n) • Space: O(1)

# two sum II - Input array is sorted
def two_sum_sorted(number,target):
    left,right=0,len(number)-1
    while left<right:
        current_sum=number[left]+number[right]
        if current_sum==target:
            return[left+1,right+1]
        elif current_sum<target:
            left+=1
        else:
            right-=1

def three_sum(nums):
    nums.sort()
    res=[]
    for i in range(len(nums)):
        if i >0 and nums[i]==nums[i-1]:
            continue
        l,r=i+1,len(nums)-1
        while l<r:
            total_nums=nums[i]+nums[l]+nums[r]
            if total_nums==0:
                res.append([nums[i],nums[l],nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                l+=1
                r-=1
            elif total_nums<0:
                l+=1
            else:
                r-=1
    return res
print(three_sum([-1,0,1,2,-1,-4]))
# Time: O(n^2) • Space: O(n)

def maxArea(height):
    l,r=0,len(height)-1
    max_area=0
    while l<r:
        h=min(height[l],height[r])
        area=h *(r-l)
        if area>max_area:
            max_area=area
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return max_area

def trap(height):
    left,right=0,len(height)-1
    left_max,right_max=0,0
    water=0
    while left<right:
        if height[left]<height[right]:
            if height[left]>=left_max:
                left_max=height[left]
            else:
                water+=left_max-height[left]
            left+=1
        else:
            if height[right]>=right_max:
                right_max=height[right]
            else:
                water+=right_max-height[right]
            right-=1    
    return water
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

# Time: O(n) • Space: O(1)

def max_profit(prices):
    min_prices=float('inf')
    max_profit=0
    for price in prices: # track the lowest price best buying price
        if price < min_prices:
            min_prices=price
        # check if selling today gives better profit    
        profit=price-min_prices
        max_profit=max(max_profit,profit)
    return max_profit


def lengthoflongestsubstring(s):
    char_set=set()
    left=0
    longest=0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        longest=max(longest,right-left+1)
    return longest

def charcterReplacement(s,k):
    count={}
    left=0
    max_freq=0
    result=0
    for right in range(len(s)):
        char=s[right]
        count[char]=count.get(char,0)+1
        # Increase its count in the dictionary.
        # count.get(char, 0) → return existing count OR 0
        # +1 → add 1 more occurrence
        max_freq=max(max_freq,count[char])
        while (right-left+1)-max_freq>k:
            count[s[left]]-=1
            left+=1
        result=max(result,right-left+1)
    return result
# right - left + 1 = window size
# maxFreq = number of already matching characters
# Difference = characters we need to replace
# If replacements needed > k → window is invalid → shrink it.

def checkinclusion(s1,s2):
    if len(s1)>len(s2):
        return False
    s1_count=[0]*26
    window_count=[0]*26
    for c in s1:
        s1_count[ord(c)-ord('a')]+=1
    left=0
    for right in range(len(s2)):
        window_count[ord(s2[right])-ord('a')]+=1
        if right-left+1>len(s1):
            window_count[ord(s2[left])-ord('a')]-=1
            left+=1
        if window_count==s1_count:
            return True        
    return False
print(checkinclusion("ab","eidbaooo"))
# Time: O(n) • Space: O(1)