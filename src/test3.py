#run the model for emotion detection using facial features

import cv2

import sys
import os

workingdirectory = os.getcwd()
sys.stdout.reconfigure(encoding="utf-8")

# preprocess
# def convert(file_path):
#     print("Processing image...")
#     img = cv2.imread(file_path, cv2.IMREAD_ANYCOLOR)
#     print("Converting RGB image to grayscale...")
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     print("Converted RGB image to grayscale...")
#     print("Resizing image to 48x48 scale...")
#     img = cv2.resize(gray,(48, 48))
#     print("Resized...")
#     cv2.imwrite(filename='uploads/saved_img.jpg', img=img)
#     print("Image saved!")
#     return "uploads/saved_img.jpg"

# predict
def giveResult(file_path):
    saved_path = file_path
    print("from python2"+file_path)
    # saved_path = convert(file_path)

    model_path = r"D:\\programming\\javaP\\learning_NetBeans\\src\\model2.h5"
    from keras.models import load_model
    mymodel = load_model(model_path) #91% accuracy

    # mymodel.summary()

    # import cv2
    # from matplotlib import pyplot as plt

    test_img = cv2.imread(saved_path)
    # plt.imshow(test_img)
    # plt.show()

    test_img = cv2.resize(test_img,(48,48))
    # plt.imshow(test_img)

    test_input = test_img.reshape((1, 48, 48, 3))

    mymodel.predict(test_input)

    var = (mymodel.predict(test_input) > 0.5).astype("int32")

    res = "Prediction of img by Model: "
    if var[0][0]==1:
        res += 'Angry'
    elif var[0][1] == 1:
        res += 'Disgust'
    elif var[0][2] == 1:
        res += 'Fear'
    elif var[0][3] == 1:
        res += 'Happy'
    elif var[0][4] == 1:
        res += 'Neutral'
    elif var[0][5] == 1:
        res += 'Sad'
    else:
        res += 'Surprise'
    
    return res


# get file from java and call these functions accordingly

path = sys.argv[1]
#path  = "C:\\Users\\User\\test.jpg"
print("from python1 "+path)

result = giveResult(path)

print(result)

# return the result to caller