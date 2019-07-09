import cv2 
import numpy as np 
from .mapper import mapp   
import os
#from skimage.filters import threshold_local


class Scanner:
    def __init__(self, filepath):
        self.image= cv2.imread(filepath)
        self.path, self.basename= os.path.split(filepath)
        self.fname, self.ext= os.path.splitext(self.basename)
        print("File naem is {}".format(self.fname))
        print("File extensiton is {}".format(self.ext))
        print("Path is {}".format(self.path))

    def getpath(self, suffix):
        nname= "".join([self.fname,suffix,self.ext])
        return os.path.join(self.path, nname)


    def preprocess(self):
        #self.image= cv2.resize(self.image, (1300, 800))
        self.image= cv2.resize(self.image, (1000, 750)) 
        self.orig= self.image.copy()
        self.gray= cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.blurred=cv2.GaussianBlur(self.gray,(5,5),0)
        self.edged=cv2.Canny(self.blurred,30,50)
        return self.edged, self.image

    def get_counters(self, edged):
        contours,hierarchy=cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  #retrieve the contours as a list, with simple apprximation model
        self.contours=sorted(contours,key=cv2.contourArea,reverse=True)
        return self.contours

    def get_corners(self, contours):
        target= None
        for c in contours:
            p=cv2.arcLength(c,True)
            approx=cv2.approxPolyDP(c,0.02*p,True)
            #print("Len is {}".format(len(approx)))
            if(len(approx)==4):
                target= approx
                print("Taget is {}".format(approx))
                break 
        return target 

    def draw_contours(self, image, target):
        tmp= image.copy()
        cv2.drawContours(tmp, [target], -1, (0, 255, 0), 5)
        return tmp


    def transform(self, image, target):
        approx= mapp(target)
        print("Points are {}".format(approx))

        pts=np.float32([[0,0],[800,0],[800,800],[0,800]])
        op=cv2.getPerspectiveTransform(approx,pts) 
        final=cv2.warpPerspective(image,op,(800,800))
        return final

    def enhance(self, image):
        warped = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #T = threshold_local(warped, 11, offset = 10, method = "gaussian")
        T= threshold_local(warped, block_size=11, method="gaussian", offset= 0)
        warped = (warped > T).astype("uint8") * 255
        return warped

    def save(self, img, name):
        path= self.getpath(name)
        cv2.imwrite(path, img)
        return path


'''
sc= Scanner("static/imgs/page.jpg")
#sc= Scanner("imgs/book_page.jpeg") 

edged, image= sc.preprocess()

contours= sc.get_counters(edged)
target= sc.get_corners(contours)

outline= sc.draw_contours(image, target)
cv2.imshow("Outline", outline) 
sc.save(outline, "_outline")

out= sc.transform(image, target)
cv2.imshow("Output", out)
sc.save(out, "_out")

#out= sc.enhance(out)
#cv2.imshow("Enchanced", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''