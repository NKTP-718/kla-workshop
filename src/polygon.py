class polygon():
	"""Represents an individual polygon"""
	def __init__( self, meta, xy):

		self.meta = meta
		self.xy = []
		_,nop,*points = xy.split("  ")
		self.nop = int(nop)
		for point in points:
			self.xy.append(tuple(map( int, point.split(' '))))

	def display_polygon(self):

		print(self.meta,end='')
		print("xy",end='  ')
		print(self.nop,end='  ')
		for i in self.xy:
			print(i[0], i[1],end=' ')
		print('\b\nendel')

	def record_polygon( self, filename):

		with open(filename, 'a') as f:
			f.write(self.meta)
			f.write("xy  ")
			f.write(str(self.nop))
			for i in self.xy:
				f.write("  "+str(i[0])+' '+str(i[1]))
			f.write("\nendel\n")

	def foo( self, target):

		# if no. of points doesnt match, not the same polygon
		if self.nop != target.nop:
			return False

		# if length of all sides are equal
		import math
		self_sides = []
		target_sides = []
		for i in range(self.nop-1):
			self_sides.append( math.dist(self.xy[i],self.xy[i+1]))
			target_sides.append( math.dist(target.xy[i],target.xy[i+1]))

		# Only for milestone 3 n 5
		# self_sides.sort()
		# target_sides.sort()

		if self_sides == target_sides:
			return True
		return False