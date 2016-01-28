class Vehicle(object):
	"""docstring for Vehicle"""
	def __init__(self, engine_type,**kwargs):
		self.engine_type = engine_type
		for k,v in kargs.items():
			setattr(self,k,v)
	def setColor(self,color):
		self.color = color
	def setSpeed(self,speed):
		self.speed=speed

class car(Vehicle):	
def __init__(self,car_category,engine_type,**kwargs):
	super().__init__(engine_type,kwargs)
	self.car_category=car_category
	self.doors=5
	self.wheels=4

mycar=Car('VTI120',color='red','saloon',engine_cc=1500,max_speed=200)	

		