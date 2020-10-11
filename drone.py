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


cap = cv2.VideoCapture(0)
ret, frame = cap.read()
file = 'live.png'
cv2.imwrite( file,frame)

image_path = file

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.object_localization(image=image)
localized_object_annotations = response.localized_object_annotations

pillow_image = Image.open(image_path)
df = pd.DataFrame(columns=['name', 'score'])
for obj in localized_object_annotations:
    if obj.name=="dog" or "Animal":
        for i in range(0,5):
            cv2.imwrite('static\dog_images\pic{:>05}.jpg'.format(i),frame)
            
        
    df = df.append(
        dict(
            name=obj.name,
            score=obj.score
        ),
        ignore_index=True)

    r, g, b = 0, 0, 0

    draw_borders(pillow_image, obj.bounding_poly, (r, g, b),
                 pillow_image.size, obj.name, obj.score)

print(df)

location=[]
while(True):
    import requests
    import json

    send_url = "http://api.ipstack.com/check?access_key=cc6910e9ecaea0af63f1aefcc62cb612"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    location.append((geo_json['latitude'],geo_json['longitude']))
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']

import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCXTPJIpoP1rR6GB1h4NZbvHEMZiQFN_Fc')
address=[]
for item in location:
    reverse_geocode_result = gmaps.reverse_geocode(item)
    address.append(reverse_geocode_result[0]['formatted_address'])


