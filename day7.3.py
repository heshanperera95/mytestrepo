class rect:
	def __init__(self,l,w):
		self.length=l
		self.width=w
		self.area=l*w
	def show(self):
		print(self.length,self.width)
		print("Area is : ",self.area)
a=int(input("Enter Length: "))
b=int(input("Enter Width : "))
R=rect(a,b)
R.show()

