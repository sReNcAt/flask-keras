#-*- coding: utf-8 -*- 

from keras.preprocessing.image import img_to_array, load_img, ImageDataGenerator
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')


rarray = "";
caterror = 0;
dogerror = 0;
cate = ""
doge = ""
def aa(j):
    
    global rarray
    global caterror
    global dogerror
    global cate
    global doge
    
    #imgur = 'data/target/who/'+str(j)+'.jpg'
    imgur = 'uploads/'+str(j)
    imag=cv2.imread(imgur)
    imag=cv2.resize(imag,(150,150))
    '''
    cv2.imwrite('data/target/cats/resize.jpg',imag)
    img = load_img('data/target/cats/resize.jpg')
    '''
    img = imag
    x = img_to_array(img)
    y = img_to_array(img)
    #print(x.shape)
    x = x.reshape((1,) + x.shape)
    X_test=x
    #X_test = X_test.transpose(0,3,1,2)
    #print (X_test.shape)
    #print("냐아아아아옹")
    X_test = X_test.reshape(X_test.shape[0], 150, 150, 3)

    X_test = X_test.astype('float32')
    X_test /= 255
    file_names='cat_dog'
    #model.fit(train_generator, samples_per_epoch=nb_train_samples, nb_epoch=nb_epoch,
    
    
    from keras.models import model_from_json
    model2 = model_from_json(open(file_names+'.json').read())
    model2.load_weights(file_names+'.h5')
    #predicted_vector = model2.predict(X_test, batch_size=1, verbose=0)
    predicted_class = model2.predict_classes(X_test)
    #evaluated = model2.evaluate(X_test,"cats", batch_size=32, verbose=1, sample_weight=None)
    
    #print('----------')
    
    #print(X_test)
    #print('predicted vector', evaluated)
    
    #print('predicted class', predicted_class)
    if(predicted_class==[0]):
        resu = "cat"
        #resu = "beer"
    if (predicted_class==[1]):
        resu = "dog"
        #resu = "soju"

    return 'IMG : '+imgur+" = "+resu;