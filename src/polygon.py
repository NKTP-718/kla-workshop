# utility functions to rotate co-ordinates
# def rotate_90(xy):
#     return ( -xy[1], xy[0])
# def rotate_180(xy):
#     return ( -xy[0], -xy[1])
# def rotate_270(xy):
#     return ( xy[1], -xy[0])

class polygon(object):
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

	def is_match_3( self, target):
		# if no. of points doesnt match, not the same polygon
		if self.nop != target.nop:
			return False
		# different approach checking for the offset od the polygons
		import math
		offset = math.dist( self.xy[0], target.xy[0])
		for i,j in zip( self.xy, target.xy):
			if offset != math.dist( i, j):
				return False
		return True

	def is_match_2( self, target):
		# different approach
		# if no. of points doesnt match, not the same polygon
		if self.nop != target.nop:
			return False

		import math
		p1 = p2 = 0
		# finding the first side of the second polygon that matches with the first polygon and the cycling through to check if they are same
		while p1 < self.nop-2:
			if math.dist( self.xy[p1], self.xy[p1+1]) != math.dist( target.xy[p2], target.xy[p2+1]):
				if p1 != 0:
					return False
				else:
					p2 += 1
					if p2 == target.nop-2:
						return False
			else:
				p1 += 1
				p2 += 1
			# if p2 >= target.nop-1:
				# p2 = 0
			p2 = p2%(target.nop-1)
		return True

	def is_match( self, target):
		# if no. of points doesnt match, not the same polygon
		if self.nop != target.nop:
			return False

		import math
		# checking if the sides are all equal
		shape1 = shape2 = []
		for i in range(self.nop-2):
			shape1.append(math.dist( self.xy[i], self.xy[i+1]))
			shape2.append(math.dist( target.xy[i], target.xy[i+1]))
		shape1.sort()
		shape2.sort()
		return shape1 == shape2

	def merge_polygons( self, polygon2):

		newcoords = []
		if polygon2.xy == self.xy:
			return True
		else:
			for i,j in zip(self.xy,polygon2.xy):
				newcoords.append(i)
				if i != j:
					newcoords.append(j)

		return newcoords
