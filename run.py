import sys

print(sys.path)

import tensorflow as tf
import keras

print(tf.__version__)
print(keras.__version__)
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
