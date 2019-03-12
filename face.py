
import cv2
import os
if os.path.exists('face_result'):
    pass
else:
    os.mkdir('face_result')

pathoffront='D:\opencv\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml'

'''
这里注意一定要用全路径   否则报错  error: (-215) !empty() in function cv::CascadeClassifier::detectMultiScale
具体参照   https://blog.csdn.net/qq_20156437/article/details/80702022
我从网上下载了cv2  (https://github.com/opencv/opencv)  这里面包含了分类器模型haarcascade_eye.xml等 我保存的位置是
/home/apollo/pan/cv2/data/haarcascades/ 一定要能寻找到分类器模型

'''


faceCascade = cv2.CascadeClassifier(pathoffront)


def  recong_face(dir):


    i = 0
    for root, dirs, files in os.walk(dir):

        for file in files:


            picture=os.path.join(root, file)
            #print (picture)

            image = cv2.imread(picture)  #读取图片   这里可以加一个判断，否则没有读取到图片还会引起其他莫名其妙的错误





            size = image.shape   #python比较不人性化的就是有时候程序执行结果不对，但是程序会报错，比如我们没有获得文件的句柄，但是程序会报成函数错误，会误导我们以为模块出了问题
            h, w = size[0], size[1]  #获取图片的大小   后续我根据这个比例缩放


            #print (h,w)   #打印大小

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2,
                                                 minNeighbors=5, minSize=(30, 30), )
            for (x, y, width, height) in faces:
                cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
                im2 = cv2.resize(image, (int(w*0.55), int(h*0.55)), interpolation=cv2.INTER_CUBIC)
             # int(w*0.55), int(h*0.55)是按照55%的比例缩放，注意这个参数只接受整数，这里需要转换一下
                cv2.imshow("mcj %d" % i, im2)
            try:
                cv2.imwrite('face_result//remcj %d.jpg' % i,im2)                 #必须添加格式  否则不会显示   处理一下异常 否则imwrite还会报错
            except:
                pass


            i = i + 1
    cv2.waitKey(0)


#
# if __name__=='__main__':
#     recong_face()


