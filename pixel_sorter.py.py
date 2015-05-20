
from PIL import Image
from random import randrange
import time
now = time.clock()

#putting it all together.
# h = sort horizontally or vertically, b = sort by either black or white pivot, r = reverse
def pixel_sorter(filename, h = True, b=True, r = False):
	'''filename, horizontal = True, black = True, reverse = False'''
	# using the Image class from PIL, get pixel data a 2d array
	
	im = Image.open(filename)
	SIZE = im.size
	print "loading pixels..."

    # store the image data
	pixels = im.getdata()

	# sort the pixels into a 3d array
	split_array = []
	length = 0
	if(h):
		split_array = get_rows(pixels,SIZE)
		length = SIZE[1]
	else:
		split_array = get_cols(pixels,SIZE)
		length = SIZE[0]
	new_array = []
	print "sorting pixels..."

	for i in xrange(length):
		# sort each row based on pixel values
		new_array.append(sort_by_value(split_array[i],b,r))

	# make a new image and populate it with our sorted pixels
	new_pixels = []
	if(h):
		new_pixels = put_rows(new_array,SIZE)
	else:
		new_pixels = put_cols(new_array,SIZE)
	new_im = Image.new('RGB',SIZE)
	new_im.putdata(new_pixels)
	print "loading image...."
	new_im.show()
	print "saving image..."
	now = time.clock()
	new_im.save( str( int(now) ) + "_" + filename )
	
	return None

def shuffle(arr):
	for i in xrange(len(arr)):
		r = randrange(len(arr))
		temp = arr[i]
		arr[i] = arr[r]
		arr[r] = temp
	return None

# randomize 
def randomize_array(arr,SIZE):
	for x in xrange(SIZE):
		for i in xrange(len(arr)):
			r = randrange(len(arr))
			temp = arr[i]
			arr[i] = arr[r]
			arr[r] = temp
	return None

# an alternate method of coverting the 3d array cols
# which produces large columns
def put_cols_split(cols,SIZE):
	new_pixels = []
	for x in xrange(SIZE[0]):
		for i in range(SIZE[1]):
			new_pixels.append(cols[x][i])
	return new_pixels

# coverts the 3d array cols back into a 2d array
def put_cols(cols,SIZE):
	new_pixels = []
	for x in xrange(SIZE[1]):
		for i in range(SIZE[0]):
			new_pixels.append(cols[i][x])
	return new_pixels

# coverts the 3d array rows back into a 2d array
def put_rows(rows,SIZE):
	new_pixels = []
	for x in xrange(SIZE[1]):
		for i in range(SIZE[0]):
			new_pixels.append(rows[x][i])
	return new_pixels
	
# splits the 2d array into rows based on height and width
def get_rows(pixels,SIZE):
	rows = []
	temp_pixels = []
	for i in xrange(SIZE[1]):
		temp_pixels = []
		for x in range(i*SIZE[0], SIZE[0]*(i+1)):
			temp_pixels.append(pixels[x])
		rows.append(temp_pixels)
	return rows

# splits the 2d array into cols based on height and width
def get_cols(pixels,SIZE):
	cols = []
	temp_pixels = []
	for i in xrange(SIZE[0]):
		temp_pixels = []
		for x in xrange(SIZE[1]):
			temp_pixels.append(pixels[x*SIZE[0]+i])
		cols.append(temp_pixels)
	return cols	

# an alternative sort that generates a diagonal pattern from the pixel data
def diagonal_sort(pixels,SIZE,alt=False):
	size = [SIZE[0],SIZE[1]]
	if alt:
		size[0],size[1] = SIZE[1],SIZE[0]
	print "Diagonal Sort"
	rows = []
	print "Sorting rows..."
	for i in xrange(size[1]):
		temp_pixels = []
		for x in range(i, i + size[0]):
			temp_pixels.append(pixels[x])
		rows.append(temp_pixels)
		
	new_pixels = []
	print "Building image..."
	for i in xrange(size[1]):
		for x in range(size[0]):
			new_pixels.append(rows[i][x])
	return new_pixels

# find the pixel with the value closest to (255,255,255)
def brightest(arr):
	max = 0 	# black
	max_index = 0
	for i in xrange(len(arr)):
		temp = arr[i][0] + arr[i][1] + arr[i][2]
		if temp > max:
			max = temp 	
			max_index = i
	return max_index

# find the pixel with the value closest to (0,0,0)
def darkest(arr):
	min = 255*3	# white
	min_index = 0
	for i in xrange(len(arr)):
		temp = arr[i][0] + arr[i][1] + arr[i][2]
		if temp < min:
			min = temp
			min_index = i
	return min_index

# sort the pixels using the darkest or brightest pixel as a pivot
def sort_by_value(arr, black = True, reverse=False):
	value = 0
	if ( black ):
		value = darkest(arr)
	else:
		value = brightest(arr)
	
	sorted_arr = arr[:value]
	sorted_arr.sort()
	if(reverse):
		sorted_arr.reverse()
	return sorted_arr + arr[value:]
    