from PIL import Image
import glob
import os

#img = Image.open('/home/ashwin/segment/file-1.png')

#l = glob.glob('/home/ashwin/segment/images/*')
l2 = glob.glob('/home/ashwin/segment/labels/*')

for each in l2:
	fname = os.path.basename(each)
	fnum = fname.split('-')[1].split('.')[0]
	img = Image.open(each)

	img.crop((0,0,100,100)).save('cropped_labels/' + 'f' + str(fnum) + '-1_P.png')
	img.crop((100,0,200,100)).save('cropped_labels/' + 'f' + str(fnum) + '-2_P.png')
	img.crop((200,0,300,100)).save('cropped_labels/' + 'f' + str(fnum) + '-3_P.png')
	img.crop((300,0,400,100)).save('cropped_labels/' + 'f' + str(fnum) + '-4_P.png')
	img.crop((400,0,500,100)).save('cropped_labels/' + 'f' + str(fnum) + '-5_P.png')
	img.crop((500,0,600,100)).save('cropped_labels/' + 'f' + str(fnum) + '-6_P.png')