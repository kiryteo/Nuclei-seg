"""from PIL import Image

img = Image.open('multipage.tif')

for i in range(4):
    try:
        img.seek(i)
        print img.getpixel( (0, 0))
    except EOFError:
        # Not enough frames in img
        break"""



from skimage import io
import scipy
import imageio

image = io.imread('/home/ashwin/Pictures/c1_seg.tif')

#print(image[0][0])
#print(image.shape[0])

for each in range(image.shape[0]):
	ffile = 'file-{}.png'.format(str(each + 1))
	imageio.imwrite(ffile, image[each])