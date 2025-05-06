# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

class Solution:
    def removeUtil (self, s):
		#code here
		cm=''
		l=0
		n=len(s)
		while l<n:
		    rep=False
		    while l+1<n and s[l+1]==s[l]:
		        rep=True
		        l+=1
		    if not rep:
		        cm+=s[l]
		    l+=1
	    if n==len(cm):
	        return cm
	    return self.removeUtil(cm)
