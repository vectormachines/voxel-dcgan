import tensorflow as tf
import numpy as np
import util_mat
import config
from model import *

netG = Generator()

z = tf.placeholder(tf.float32, [config.batch_size, config.nz])
train = tf.placeholder(tf.bool)

x = netG(z, train, config.nsf, config.nvx)

t_vars = tf.trainable_variables()
varsG = [var for var in t_vars if var.name.startswith('G')]

saver = tf.train.Saver(varsG + tf.moving_average_variables())

config_proto = tf.compat.v1.ConfigProto()
config_proto.gpu_options.allow_growth = True

with tf.compat.v1.Session(config=config_proto) as sess:
    saver.restore(sess, config.params_path)
    batch_z = np.random.uniform(-1, 1, [config.batch_size, config.nz]).astype(np.float32)
    x_g = sess.run(x, feed_dict={z:batch_z, train:False})
    for i, data in enumerate(x_g):
        util_mat.save_mat("/content/out/{0}.mat".format(i), data[:, :, :, 0] > 0.9)