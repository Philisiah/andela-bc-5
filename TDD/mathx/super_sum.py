def super_sum(*args):
	'''sums up the arguments'''
	total = 0
	for i in args:
		if type(i) == list:
			total = super_sum(*i)
		else:
			total += i
			return total     