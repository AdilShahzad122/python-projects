import cv2


source="1.jpeg"
destination="newImage.jpeg"
scale_percent = 50
 
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
#cv2.imshow('Original Image', src)
#percent by which the image is resized
scale_percent = 50

#calculate the 50 percent of original dimensions
newwidth = int(src.shape[1] * scale_percent / 100)
newheight = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (newwidth, newheight)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination,output) 
cv2.waitKey(0)

