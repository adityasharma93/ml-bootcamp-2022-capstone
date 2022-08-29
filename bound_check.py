import cv2

video_filepath = "/Users/adsharma/Desktop/virat_stuff/VIRAT_S_000001.mp4"
object_filepath = "/Users/adsharma/Desktop/virat_stuff/VIRAT_S_000001.viratdata.objects.txt"
frame_filepath = "/Users/adsharma/Desktop/virat_stuff/VIRAT_S_000001_frame_0.jpg"
bbox_frame_path = "/Users/adsharma/Desktop/virat_stuff/bbox_frame_0.jpg"
output_folder = "/Users/adsharma/Desktop/virat_stuff/frames_output"

#code to capture one frame and draw a boundary box around the car

#video_cap = cv2.VideoCapture(video_filepath)
#success,framecap = video_cap.read()

#if success:
#	print("FRAME CAPTURED SUCCESSFULLY")
#	cv2.imwrite(frame_filepath, framecap)
#else:
#	print("FRAME CAPTURE FAILED")

#obj_file = open(object_filepath, "r")

#while True:
#	line = obj_file.readline()
#	line = line.split()
	#print(line)
#	if line[-1] == '2':
#		break
#print(line)

#x1 = int(line[3])
#y1 = int(line[4])
#x2 = x1 + int(line[5])
#y2 = y1 + int(line[6])

#frm_img = cv2.imread(frame_filepath)

#frm_img = cv2.rectangle(frm_img,(x1,y1),(x2,y2),(255,0,0),2)
#cv2.imwrite(bbox_frame_path, frm_img)

#code to draw boundary box on all frames of a video for a particular object

frame_ref = 0
video_cap = cv2.VideoCapture(video_filepath)
obj_file = open(object_filepath, "r")

while True:
	line = obj_file.readline()
	line = line.split()
	if line[0] == '3':
		break
print("Reached the required object")
print(line)
total_frame_duration = int(line[1])
initial_frame = int(line[2])
obj_id = int(line[0])

while True:
	success, framecap = video_cap.read()
	if success:
		if ((frame_ref == int(line[2])) and (obj_id == int(line[0]))):
			x1 = int(line[3])
			y1 = int(line[4])
			x2 = x1 + int(line[5])
			y2 = y1 + int(line[6])
			framecap = cv2.rectangle(framecap,(x1,y1),(x2,y2),(255,0,0),2)

		cv2.imwrite("{}/VIRAT_S_000001_frame_{}.jpg".format(output_folder,str(frame_ref)),framecap)
		frame_ref += 1
		line = obj_file.readline()
		line = line.split()
	else:
		break
video_cap.release()
obj_file.close()