import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras import layers as L
import h5py
import os

os.environ['CUDA_VISIBLE_DEVICES']='7'
#%% prepare training and testing datasets
datasave_path="/mnt/VOL1/czheng/LiDAR/ours/Pointnet_tf2"
f = h5py.File(os.path.join(datasave_path, "ply_data_train0.h5"), "r")
x_train = np.array(f['data'])
y_train = np.array(f['label'])
#y_train = tf.keras.utils.to_categorical(y_train)
f.close()

#print('x_train.shape = ',x_train.shape)
#%%
f = h5py.File(os.path.join(datasave_path, "ply_data_all0.h5"), "r")
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

####################

def mine_hard_samples(model, x_train,y_train, batch_size):
   while True:
       samples, targets = [], []
       while len(samples) < batch_size:
           x_data = x_train
           y_data = y_train
           preds = model.predict(x_data)
           errors = np.mean(np.abs(preds - y_data), axis = 1) > .001
           samples += x_data[errors].tolist()
           targets += y_data[errors].tolist()

       regular_samples = batch_size * 2 - len(samples)

       samples += x_train[:regular_samples].tolist()
       targets += y_train[:regular_samples].tolist()

       samples, targets = map(np.array, (samples, targets))

       idx = np.arange(batch_size * 2)
       np.random.shuffle(idx)
       batch1, batch2 = np.split(idx, 2)
       yield samples[batch1], targets[batch1]
       yield samples[batch2], targets[batch2]




####################################################################################################

model =  keras.Model(inputs=inputs, outputs=outputs)
model.summary()

#%% set optimizer, loss and metrics
optz = keras.optimizers.Adam(lr = 1e-3)
model.compile(optimizer = optz, loss='MSE',metrics = ['mae'])

#%% train model             
history = model.fit_generator(mine_hard_samples(model, x_train,y_train, batch_size=64), epochs=800, steps_per_epoch=4, validation_data=(x_test,y_test))
#%% test model

res = model.predict(x_test)


f = h5py.File("pred_label.h5", "r+")
del f['predict_label']
f['predict_label'] = res
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
f.close()
