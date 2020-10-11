import os

import image
from keras.models import model_from_json
from keras.preprocessing.image import img_to_array
import cv2
import tensorflow as tf
import numpy as np


import keras

from tensorflow.keras.applications.efficientnet import preprocess_input

from PIL import Image

import io, os
from numpy import random
from google.cloud import vision
from pillow_utility import draw_borders, Image
import pandas as pd
import cv2
from PIL import Image
from google.cloud import vision
from google.cloud.vision import types
import io, os
from numpy import random
from google.cloud import vision
from pillow_utility import draw_borders, Image
import pandas as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"abc.json"
client = vision.ImageAnnotatorClient()



import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
import cv2
import image
from keras.models import model_from_json
from keras.preprocessing.image import img_to_array
import cv2
import tensorflow as tf
import numpy as np


UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\imgages')


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'bmp'}
app = Flask(__name__)





@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/inputform", methods=["GET", "POST"])
def input_symptoms():

    if request.method == 'POST':
        try:

            # to load pre-saved model


            image = request.files['image']
            
            image.save('temp_image.bmp')

            loaded_model = keras.models.load_model("dog_breed_classifier.h5")

            img = Image.open('./temp_image.bmp').resize((224, 224))


            ddd = loaded_model.predict(preprocess_input(np.expand_dims(img, axis=0)))



            breed = ddd[0]

            current_labels=['Chihuahua', 'Japanese_spaniel', 'Maltese_dog', 'Pekinese', 'Shih-Tzu', 'Blenheim_spaniel', 'papillon', 'toy_terrier', 'Rhodesian_ridgeback', 'Afghan_hound', 'basset', 'beagle', 'bloodhound', 'bluetick', 'black-and-tan_coonhound', 'Walker_hound', 'English_foxhound', 'redbone', 'borzoi', 'Irish_wolfhound', 'Italian_greyhound', 'whippet', 'Ibizan_hound', 'Norwegian_elkhound', 'otterhound', 'Saluki', 'Scottish_deerhound', 'Weimaraner', 'Staffordshire_bullterrier', 'American_Staffordshire_terrier', 'Bedlington_terrier', 'Border_terrier', 'Kerry_blue_terrier', 'Irish_terrier', 'Norfolk_terrier', 'Norwich_terrier', 'Yorkshire_terrier', 'wire-haired_fox_terrier', 'Lakeland_terrier', 'Sealyham_terrier', 'Airedale', 'cairn', 'Australian_terrier', 'Dandie_Dinmont', 'Boston_bull', 'miniature_schnauzer', 'giant_schnauzer', 'standard_schnauzer', 'Scotch_terrier', 'Tibetan_terrier', 'silky_terrier', 'soft-coated_wheaten_terrier', 'West_Highland_white_terrier', 'Lhasa', 'flat-coated_retriever', 'curly-coated_retriever', 'golden_retriever', 'Labrador_retriever', 'Chesapeake_Bay_retriever', 'German_short-haired_pointer', 'vizsla', 'English_setter', 'Irish_setter', 'Gordon_setter', 'Brittany_spaniel', 'clumber', 'English_springer', 'Welsh_springer_spaniel', 'cocker_spaniel', 'Sussex_spaniel', 'Irish_water_spaniel', 'kuvasz', 'schipperke', 'groenendael', 'malinois', 'briard', 'kelpie', 'komondor', 'Old_English_sheepdog', 'Shetland_sheepdog', 'collie', 'Border_collie', 'Bouvier_des_Flandres', 'Rottweiler', 'German_shepherd', 'Doberman', 'miniature_pinscher', 'Greater_Swiss_Mountain_dog', 'Bernese_mountain_dog', 'Appenzeller', 'EntleBucher', 'boxer', 'bull_mastiff', 'Tibetan_mastiff', 'French_bulldog', 'Great_Dane', 'Saint_Bernard', 'Eskimo_dog', 'malamute', 'Siberian_husky', 'affenpinscher', 'basenji', 'pug', 'Leonberg', 'Newfoundland', 'Great_Pyrenees', 'Samoyed', 'Pomeranian', 'chow', 'keeshond', 'Brabancon_griffon', 'Pembroke', 'Cardigan', 'toy_poodle', 'miniature_poodle', 'standard_poodle', 'Mexican_hairless', 'dingo', 'dhole', 'African_hunting_dog'
]

            sorted_lists = [x for _, x in sorted(zip( breed, current_labels))]

            result_dict = dict(zip(current_labels,  breed))

            print(sorted_lists)


            top_two_results = sorted_lists[-1]

            print(top_two_results)

            resultss=top_two_results

            

            return render_template('index.html',resultss=resultss)

        except:

            return render_template('index.html', results="No File Found")
@app.route("/adopt", methods=["GET", "POST"])
def adopt():
    
    location=[]
    
    import requests
    import json

    #For live demo run object_detection_google_cloud.py and what ever proceeds this
    #send_url = "http://api.ipstack.com/check?access_key=cc6910e9ecaea0af63f1aefcc62cb612"
    #geo_req = requests.get(send_url)
    #geo_json = json.loads(geo_req.text)
    #location.append((geo_json['latitude'],geo_json['longitude']))
    images = os.listdir(os.path.join(app.static_folder, "dog_images"))

    #for i in range(len(images)):
        #location.append((str(random.uniform(-90, 90)),str(random.uniform(-180, 180))))

    location=[('30.7421','76.8188'),('30.7421','76.8188'),('30.7525','76.8101'),('30.7475','76.7842'),('30.7489','76.7875')]

    import googlemaps
    gmaps = googlemaps.Client(key='AIzaSyCXTPJIpoP1rR6GB1h4NZbvHEMZiQFN_Fc')
    
    address=[]
    for item in location:
        reverse_geocode_result = gmaps.reverse_geocode(item)
        print(reverse_geocode_result)
        address.append(reverse_geocode_result[0]['formatted_address'])
    
    combined_info = zip(images, address)

    return render_template('index - Copy.html',combined_info=combined_info,images=images)



if __name__ == '__main__':
    app.run(debug=True)
