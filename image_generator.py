import requests
import urllib.request
import json
import random
from database_info import *
from io import BytesIO
from PIL import Image

def generate_image():
    url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
    words = json.loads(url.read())
    word = random.choice(words)

    # Return a single random word

    #f = open('C:/Users/pauli/Desktop/api_key.txt', "r")
    #secret_key = str(f.read())
    api_key = os.getenv("api_key", "optional-default")

    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': word,
        },
        headers={'api-key': api_key}
    )
    #print(r.json())
    url = r.json().get('output_url')
    #url = 'https://api.deepai.org/job-view-file/773a9572-98f5-4d6a-a933-cc929b0f7df9/outputs/output.jpg'

    #string = r"C:\Users\pauli\Documents\Github\Image_Repo\static\images\ " + str(word) + '.png'
    #string = r"C:\Users\pauli\Documents\Github\Image_Repo\static\images\ " + str(word) + '.png'


    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    name = 'static/images/' + str(word) + '.jpg'

    print(name)
    img.save(name, 'JPEG')

    #filename = r"{}".format(string)
    #filename = filename.replace(' ','')

    #urllib.request.urlretrieve(url, filename)


    path = "images/" + word + ".jpg"
    #insert_data(word,path )


