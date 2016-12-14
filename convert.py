import cv2
#import tensorflow as tf
import numpy as np
import base64
IMAGE_SIZE = 64


f = open('base64file.txt')
#I cut hedder of base64 THIS part
# >  data:image/png;base64, <
data = f.read()

''''
convert image base64 -> cv2(mat)
''''

cv_train_image = []
img = base64.b64decode(data)#base64 decode
npimg = np.fromstring(img, dtype=np.uint8) #binary?
source = cv2.imdecode(npimg, 1) #convert to cv2(mat format)
cv2.imwrite("source.jpg",source)#check code.source

''''
edit image for learning
''''

res_source= cv2.resize(source, (IMAGE_SIZE, IMAGE_SIZE)) #resize images for learning.
cv_train_image.append(res_source.flatten().astype(np.float32)/255.0) #flatten images.
np_train_data  = np.asarray(train_image) # convert to array
print(np_train_data)

'''
#example usage
       train_accuracy = sess.run(acc, feed_dict={
                images_placeholder: np_train_data,
                labels_placeholder: train_label,
                keep_prob: 1.0})
'''
