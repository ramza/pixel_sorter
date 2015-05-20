# pixel_sorter
This program is inspired by Kim Asendorf's processing work. I thought it would be a good exercise to build my own implemenation in python. This is a work in progress.

how to use

open the command line and navigate to a folder containing both the source image and pixel_sorter.py and run python

to run the file in python use execfile("pixel_sorter.py")
to sort the source image use pixel_sorter("filename.jpg")

pixel_sorter takes 4 parameters including the image file name. The others are booleans representing horizontal, Black, and reverse. By default they are set to true, true, and false, respectively. Horizontal chooses between a horizontal or vertical sort. Black searches for either the darkest or lightest RBG value. This index is used as a pivot point for selecting a segment of the row or column. The last boolean reverses the selected segement.
