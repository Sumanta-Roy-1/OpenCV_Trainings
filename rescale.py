import cv2 as cv

img = cv.imread('Photos\Bike.jpg')

# cv.imshow('BIKE', img)

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimentions = (width,height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img)
# cv.imshow('BIKE', img)
cv.imshow('BIKE_RESIZED', resized_image)
cv.waitKey(0)  #  it waits for any key to be pressed    