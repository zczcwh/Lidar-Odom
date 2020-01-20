import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras import layers as L
import h5py
import os

#%% prepare training and testing datasets
datasave_path="/mnt/VOL1/czheng/LiDAR/ours/Pointnet_tf2"
f = h5py.File(os.path.join(datasave_path, "ply_data_train0.h5"), "r")
x_train = np.array(f['data'])
y_train = np.array(f['label'])
#y_train = tf.keras.utils.to_categorical(y_train)
f.close()

#print('x_train.shape = ',x_train.shape)
#%%
f = h5py.File(os.path.join(datasave_path, "ply_data_test0.h5"), "r")
x_test = np.array(f['data'])
y_test = np.array(f['label'])
#y_test = tf.keras.utils.to_categorical(y_test)
f.close()

####data norm
mean = x_train.mean(axis=0)
x_train -=mean
std = x_train.std(axis=0)
x_train/=std
x_test-=mean
x_test/=std

#output norm
# y_test[:, 0:3] = y_test[:, 0:3] *10
# y_test[:, 4] = y_test[:, 4] *10
# y_test[:, 5] = y_test[:, 5] *100
#
# y_train[:, 0:3] = y_train[:, 0:3] *10
# y_train[:, 4] = y_train[:, 4] *10
# y_train[:, 5] = y_train[:, 5] *100

print('x_train.shape=',x_train.shape)
print('x_test.shape=',x_test.shape)

#%% define PointNet

inputs = L.Input(shape=(1000,6))

x = inputs

x = L.Dense(64,activation='relu')(x)
x = L.Dense(64,activation='relu')(x)

x = L.Dense(64,activation='relu')(x)
x = L.Dense(128,activation='relu')(x)
x = L.Dense(1024,activation='relu')(x)

x = L.GlobalMaxPooling1D()(x)

x = L.Dense(512,activation='relu')(x)
x = L.Dense(256,activation='relu')(x)
x = L.Dense(7,activation='linear')(x)
# x = L.Dense(10,activation='linear')(x)


outputs = x

model =  keras.Model(inputs=inputs, outputs=outputs)
model.summary()

#%% set optimizer, loss and metrics
optz = keras.optimizers.Adam(lr = 2e-3)
model.compile(optimizer = optz, loss='MSE',metrics = ['mae'])

#%% train model
history = model.fit(x = x_train,y=y_train,shuffle="batch", batch_size=64, epochs=200,validation_data=(x_test,y_test))

#%% test model

res = model.predict(x_test)

# res[:, 0:3] = res[:, 0:3] /10
# res[:, 4] = res[:, 4] /10
# res[:, 5] = res[:, 5] /100

f = h5py.File("pred_label.h5", "r+")
del f['predict_label']
f['predict_label'] = res
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
f.close()