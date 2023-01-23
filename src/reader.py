from polygon import polygon

def read_source(filename):
	units = []
	with open(filename, 'r') as f:
		# ignore header
		while True:
			buffer = f.readline()
			if buffer.split(' ')[0] == "strname":
				f.readline()
				break
		# body
		lines = []
		while True:
			buffer = f.readline()
			if buffer == "endel\n":
				units.append(polygon( lines[0]+lines[1]+lines[2], lines[3]))
				lines = []
				continue
			elif buffer == "endstr\n":
				return units
			lines.append(buffer)