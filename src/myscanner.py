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
        w, h, _= self.image.shape
        nh= 1000
        nw= int((w/ h) * 1000)
        self.image= cv2.resize(self.image, (nh, nw)) 
        self.orig= self.image.copy()
        self.gray= cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.blurred=cv2.GaussianBlur(self.gray,(5,5),0)
        self.edged=cv2.Canny(self.blurred,30,50)

        self.width, self.height, _= self.image.shape
        self.area= self.width* self.height
        return self.edged, self.image

    def get_contours(self, edged):
        contours,hierarchy=cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  #retrieve the contours as a list, with simple apprximation model
        self.contours=sorted(contours,key=cv2.contourArea,reverse=True)
        return self.contours

    def get_best(self, contours, minareap= 0.25):
        target= None
        minarea= self.area * minareap
        for c in contours:
            ep= 0.1 * cv2.arcLength(c,True)
            approx= cv2.approxPolyDP(c,ep,True)
            if(len(approx)==4):
                if(cv2.contourArea(approx)< minarea):
                    continue
                target= approx
                print("Taget is {}".format(approx))
                break 
        if(target is None):
            print("No Page found")
            target= np.array([
                [[0,0]],
                [[self.height,0]],
                [[self.height, self.width]],
                [[0, self.width]]
            ])
        return target 

    def draw_all_contours(self, image, contours, minareap= 0.001):
        target= []
        minarea= self.area* minareap
        i=0
        print("Total {} contours found".format(len(contours)))
        for c in contours:
            ep= 0.01 * cv2.arcLength(c,True)
            approx=cv2.approxPolyDP(c, ep,True)
            if(cv2.contourArea(approx)< minarea):
                continue
            print("Area is {}".format(cv2.contourArea(approx)))
            target.append(approx)
            tmp= image.copy()
            cv2.drawContours(tmp, [approx], -1, (0, 255, 0), 5)
            cv2.imshow("Next{}".format(i), tmp)
            i+= 1
        target= np.array(target) 
        tmp= image.copy()
        cv2.drawContours(tmp, target, -1, (0, 255, 0), 5)
        cv2.imshow("next", tmp)


    def draw_contours(self, image, target):
        tmp= image.copy()
        cv2.drawContours(tmp, [target], -1, (0, 255, 0), 5)
        return tmp


    def transform(self, image, target):
        approx= mapp(target)
        print("Points are {}".format(approx))

        nh= 800
        nw= int((self.width/ self.height) * 800)
        pts=np.float32([[0,0],[nh,0],[nh,nw],[0,nw]])
        op=cv2.getPerspectiveTransform(approx,pts) 
        final=cv2.warpPerspective(image,op,(nh,nw))
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
sc= Scanner("imgs/page.jpg")
#sc= Scanner("imgs/book_page.jpeg") 

edged, image= sc.preprocess()

contours= sc.get_contours(edged)


#sc.draw_all_contours(image, contours)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#exit()


target= sc.get_best(contours)


outline= sc.draw_contours(image, target)
cv2.imshow("Outline", outline) 
out= sc.transform(image, target)
cv2.imshow("Output", out)

#out= sc.enhance(out)
#cv2.imshow("Enchanced", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''