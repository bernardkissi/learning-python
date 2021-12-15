class Customer:
	
	totalcustomer = 0

	def __init__(self, name):
		self.name = name
		self.totalcustomer += 1
		# 

	@property
	def fullname(self):
		return self.name ...


	@classmethod
	def resetCounter(cls):
		cls.totalcustomer = 0

	@staticmethod
	def CustomerAccountCreationFailed():
		print("the customer could not be created")


#####################################################


	from customer import Customer

	customer1 = Customer("s")
	Customer.createCustomer(10)

	print(Customer) #should return a string

	<class Customer bound x909808098>

	def __str__(self):
