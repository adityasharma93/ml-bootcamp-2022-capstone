import cv2
import numpy as np
import glob

'''
img_array = []
for filename in glob.glob('/Users/adsharma/Desktop/virat_stuff/frames_output/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('bbox_check.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
'''

img_array = []
filepath = '/Users/adsharma/Desktop/virat_stuff/frames_output/VIRAT_S_000001_frame_0.jpg'
directory_path = '/Users/adsharma/Desktop/virat_stuff/frames_output/VIRAT_S_000001_frame'
num_files = len(glob.glob('/Users/adsharma/Desktop/virat_stuff/frames_output/*.jpg'))
count1 = 0
count2 = 0
check_num = 0

img = cv2.imread(filepath)
height, width, layers = img.shape
size = (width, height)

out = cv2.VideoWriter('bbox_check.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 15, size)

while((count1*100) < num_files):
	count1 += 1
	count2 = 0
	while((((count1*100)+count2) < num_files) and count2 < 100):
		count2 += 1
		check_num = (count1 * 100) + count2
		print(check_num)
		#print(directory_path, str(check_num))
		filename = '{}_{}.jpg'.format(directory_path, str(check_num))
		img = cv2.imread(filename)
		img_array.append(img)

	for i in range(len(img_array)):
		out.write(img_array[i])

out.release()
