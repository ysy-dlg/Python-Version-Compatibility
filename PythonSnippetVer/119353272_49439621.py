from keras import Input, Model, backend as K
from keras.applications import VGG16
from keras.layers import TimeDistributed, Lambda
input_shape = (224, 224, 3)
vgg19 = VGG16(input_shape=input_shape,
              include_top=False,
              weights=None)