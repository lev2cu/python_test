
atan2(b,a)	Arctangent,
hypot(x,y)	Hypotenus; Euclidean distance
a**b		power, a^b
math.sqrt(a) 	.log; .exp; .pi; .e 
around(a)	round

z = 3+4j	a complex number
z.real		.imag; .conj();

a=array([2,3,4,5])		Row vector
array([2,3,4,5])[:,NewAxis]	Column vector

arange(1,11, dtype=Float)	
range(1,11)			1,2,3, ... ,10
range(10.)			0.0,1.0,2.0, ... ,9.0
a[::-1] or			Reverse
concatenate((a,a))	Concatenate two vectors
identity(3)		Identity matrix
a[0,]			First row
a[:,0]			First column
a.take([0,2]).take([0,3], axis=1)	Array as indices- a([1 3], [1 4])
(a>90).choose(a,90)		clipping: replace all elements over 90
a.clip(min=2, max=2)		clip upper and lower values 
a.shape or a.getshape()		Matrix dimensions
a.size				lenght of matrix

maximum(a,b)			pairwise max
concatenate((a,b)).max()	max of all values in two vectors

concatenate((a,b), axis=0)
vstack((a,b))			Bind rows

concatenate((a,b), axis=1)
hstack((a,b))			Bind columns

a.setshape(2,3)    		reshaping rows first
a.flatten()			flatten to vectors (by rows)

b = a.copy()			copy of a

vdot(a,b)	Vector dot product
cross(a,b)	Cross product

a.ravel().nonzero()	Non-zero elements, indices... find(a)
















