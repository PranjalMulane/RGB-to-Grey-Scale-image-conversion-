from django.shortcuts import render
from django.shortcuts import redirect
import numpy as np

import cv2


def recognise(request):
    if request.method == 'POST' and request.FILES:
        image = (request.FILES['image'])

        filestr = request.FILES['image'].read()

        npimg = np.fromstring(filestr, np.uint8)

        frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)




        # Reading color image
        # img = cv2.imread("lotus.jpg")

        # Converting color image to grayscale image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Showing the converted image
        cv2.imwrite("media/image.jpg",frame)
        # cv2.imshow("Converted Image",gray)

        #saving original and black and white image
        cv2.imwrite("media/result.jpg",gray)

        # waiting for key event
        cv2.waitKey(0)

        # destroying all windowss
        cv2.destroyAllWindows()

        return render(request , "index.html" , {'img_modifications' : True})



    return render (request, 'index.html')
   