# Python program processing
# global variable

count = 5
def some_method():
	
	#count = 10
	
	x = count + 10
	print(x)
	
	def new():
		print(x)
		
	new()

	
some_method()

print(count)