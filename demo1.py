import keras
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.imagenet_utils import decode_predictions
from keras.applications import nasnet, inception_resnet_v2
import numpy as np
import matplotlib.pyplot as plt 


#Load the NASNET Model
inception_res_net_v2_model = inception_resnet_v2.InceptionResNetV2(weights='imagenet')


filename = 'dog.jpg'
# load an image in PIL format
original = load_img(filename, target_size=(299, 299))
print('PIL image size',original.size)
plt.imshow(original)
plt.show()
 
# convert the PIL image to a numpy array
# IN PIL - image is in (width, height, channel)
# In Numpy - image is in (height, width, channel)
numpy_image = img_to_array(original)
plt.imshow(np.uint8(numpy_image))
plt.show()
print('numpy array size',numpy_image.shape)
 
# Convert the image / images into batch format
# expand_dims will add an extra dimension to the data at a particular axis
# We want the input matrix to the network to be of the form (batchsize, height, width, channels)
# Thus we add the extra dimension to the axis 0.
image_batch = np.expand_dims(numpy_image, axis=0)
print('image batch size', image_batch.shape)
plt.imshow(np.uint8(image_batch[0]))

processed_image = inception_resnet_v2.preprocess_input(image_batch.copy())

predictions = inception_res_net_v2_model.predict(processed_image)

label = decode_predictions(predictions)


print(label)
