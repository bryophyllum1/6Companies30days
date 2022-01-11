class Solution:
	def getNthUglyNo(self,n):
		# code here
		p2 = 0
		p3 = 0
		p5 = 0
		prev = 1
		l = [1]
		while len(l)<n:
		    x = 2*l[p2]
		    y = 3*l[p3]
		    z = 5*l[p5]
		    m = min(x, y, z)
		    l.append(m)
		    if m == x:
		        p2+=1
		    if m == y:
		        p3+=1
		    if m == z:
		        p5+=1
	    return l[-1]