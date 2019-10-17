#Convolutional Neural Network

#Part 1 - Building the CNN

#Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#Initialising the CNN
classifier = Sequential()

#Step 1 - Convolution
classifier.add(Convolution2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu', kernel_initializer = 'glorot_uniform'))

#Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

#Adding a second convolutional layer
classifier.add(Convolution2D(32, (3, 3), activation = 'relu', kernel_initializer = 'glorot_uniform'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

#Step 3 - Flattening
classifier.add(Flatten())

#Step 4 - Full connection
classifier.add(Dense(activation = 'relu', units = 128, kernel_initializer = 'glorot_uniform'))
classifier.add(Dense(activation = 'sigmoid', units = 1, kernel_initializer = 'glorot_uniform'))

#Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                target_size=(64, 64),
                                                batch_size=32,
                                                class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

classifier.fit_generator(training_set,
                        steps_per_epoch=(8000/32),
                        epochs=25,
                        validation_data=test_set,
                        validation_steps=(2000/32)) 

import numpy as np
from skimage.io import imread
from skimage.transform import resize
initial = 'dataset/test_set/dogs/dog.4'
for i in range(100,900):
    string = initial+str(i)+'.jpg'
    img = imread(string)
    img = resize(img,(64,64))
    img = np.expand_dims(img,axis=0)
    img = img/(255.0)
    prediction = classifier.predict_classes(img)
    if(prediction):
        print("DOG")
    else:
        print("CAT")
