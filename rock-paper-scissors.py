# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O5h6vgTzExdYhRGUIvXSy3_h-BsRKxMF

**Data Diri** 
- nama  : muhammad rizky rahmattullah
- email : scriptkiddies@protonmail.com
- phone : +62881025883097 
- kota  : surabaya
"""

!wget --no-check-certificate \
  https://dicodingacademy.blob.core.windows.net/picodiploma/ml_pemula_academy/rockpaperscissors.zip \
  -O /tmp/rockpaperscissors.zip

import zipfile,os

local_zip = '/tmp/rockpaperscissors.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()

BASIS_DIR = "/tmp/rockpaperscissors/rps-cv-images/"

from tensorflow.keras.preprocessing.image import ImageDataGenerator

training_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest",
    validation_split=0.4,
)

train_generator = training_datagen.flow_from_directory(
    BASIS_DIR,
    target_size=(150, 150),
    class_mode="categorical",
    shuffle=True,
    subset="training",
)

validation_generator = training_datagen.flow_from_directory(
    BASIS_DIR,
    target_size=(150, 150),
    class_mode="categorical",
    shuffle=True,
    subset="validation",
)

import tensorflow as tf

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Conv2D(16, (3, 3), activation="relu", input_shape=(150, 150, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
     
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
     
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
     
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.5),
     
        tf.keras.layers.Dense(128, activation="relu"),
     
        tf.keras.layers.Dense(512, activation="relu"),
     
        tf.keras.layers.Dense(3, activation="softmax"),
    ]
)

model.compile(
    loss="categorical_crossentropy", 
    optimizer=tf.optimizers.Adam(),
    metrics=["accuracy"]
)

target_akurasi = 0.85

class myCallback(tf.keras.callbacks.Callback):
	def on_epoch_end(self, epoch, logs={}):
		if(logs.get('accuracy') > target_akurasi):
			print("\nMencapai akurasi% 2.2f%%, jadi hentikan pelatihan !!" %(ACCURACY_THRESHOLD*100))
			self.model.stop_training = True

# Instantiate a callback object
callbacks = myCallback()

history = model.fit(
    train_generator,
    steps_per_epoch=25,
    epochs=50,
    validation_data=validation_generator,
    validation_steps=4,
    verbose=2,
    callbacks=[callbacks],
)

import numpy as np
from google.colab import files
from keras.preprocessing import image
import matplotlib.pyplot as plt

uploaded = files.upload()

for fn in uploaded.keys():

    path = fn
    img = image.load_img(path, target_size=(150, 150))
    imgplot = plt.imshow(img)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    print(fn)
    print('hasil deteksi gambar :')
    if classes[0][0] == 1:
        print("KERTAS")
    elif classes[0][1] == 1:
        print("BATU")
    elif classes[0][2] == 1:
        print("GUNTING")
    else:
        print("Tidak Diketahui")

