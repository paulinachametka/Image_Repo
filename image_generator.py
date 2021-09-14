import requests
from random_word import RandomWords
r = RandomWords()

# Return a single random word
word = r.get_random_word()

f = open('C:/Users/pauli/Desktop/api_key.txt', "r")
secret_key = str(f.read())


print(word)
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': word,
    },
    headers={'api-key': secret_key}
)
print(r.json())