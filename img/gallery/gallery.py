
import cv2
from os import listdir
from os.path import isdir
import importlib
import sys


pic_names = [filename for filename in listdir('.') if '.jpg' in filename.lower()]


thumbnail_width = 200.0
display_height  = 600.0

gallery_html = '<div id="links">\n'

for pic_name in pic_names:
	print 'processing', pic_name, '...'

	image = cv2.imread(pic_name)

	display_ratio = display_height/image.shape[0]
	display_image = cv2.resize(image, (0,0), fx=display_ratio, fy=display_ratio)
	cv2.imwrite('display/'+ pic_name, display_image)

	thumbnail_ratio = thumbnail_width/image.shape[1]
	thumbnail_image = cv2.resize(image, (0,0), fx=thumbnail_ratio,fy=thumbnail_ratio)
	cv2.imwrite('thumbnails/'+ pic_name, thumbnail_image)

	gallery_html += '    <a href=\"img/gallery/display/' + pic_name + '\" title=\"' + pic_name + '\" data-gallery>\n' + \
	                '        <img src=\"img/gallery/thumbnails/' + pic_name + '\" alt=\"' + pic_name + '\">\n' + \
	                '    </a>\n'

gallery_html += '</div>\n'

with open("gallery_code.txt", 'w') as f:
	f.write( gallery_html )

