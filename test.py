from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from PIL import Image
import pytesseract
import argparse
import os


#hi this is just me testing stuff.

train = [
    ('I guess.', 'neg'),
    ('Fine then', 'neg'),
     ('Ok then', 'neg'),
     ('Fine', 'neg'),
     ("I can't deal with this", 'neg'),
     ("Whatever.", "neg"),
     ("lol ok", "neg"),
     ('Yeah sure!', 'pos'),
     ('Yeehaw!', 'pos'),
     ('Yeah totally!', 'pos'),
     ('so excited', 'pos')
 ]

cl = NaiveBayesClassifier(train)

m1 = TextBlob("I have booked my first ever flight! So excited", classifier=cl)
print(m1.sentiment)
print(m1.classify())

h1 = TextBlob("West Palm?")
print(h1.sentiment)

m2 = TextBlob("Yeehaw!")
print(m2.sentiment)
print(cl.classify(m2))

h2 = TextBlob("ok then. You seemed like you'd changed your mind last time we spoke.")
print(h2.sentiment_assessments)

m3 = TextBlob("No I mean we got a good house its all good")
print(m3.sentiment_assessments)

h3 = TextBlob("Alrighty. I was concerned about spending a few days with that group. I figured Chris will thirst over you, and I'd get to know the convention bar. Am I missing anyone.")
print(h3.sentiment_assessments)

h4 = TextBlob("Have fun I guess. It's a bit of an about face.")
print(h4.sentiment_assessments)

m4 = TextBlob("I'm excited to go on a plane ffs")
print(m4.sentiment_assessments)

h5 = TextBlob("I got the impression you were bored shitless at Distrito so I wondered why you would spend days with them.")
print(h5.sentiment_assessments)

img = Image.open('text1.png')
img2 = Image.open('text2.jpg')
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe' 
result = pytesseract.image_to_string(img)
print(result)
result2 = pytesseract.image_to_string(img2)
print(result2)

myarray = result2.split("\n\n")
print(myarray)