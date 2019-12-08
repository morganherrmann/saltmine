from flask import Flask
import json
from requests.api import request
from flask.templating import render_template
from flask.json import jsonify
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from PIL import Image
import pytesseract
import argparse
import os
from collections import defaultdict
app = Flask(__name__)

current_salt = None

# a salt is made with a file path
# analyze() gets the sentiment
# save produces a text file to save to local file system
class Salt:
    def __init__(self, path):
        self.path = path
        self.texts = pytesseract.image_to_string(Image.open(path))

    def analyze(self):
        myarray = self.texts.split("\n\n")
        items = []
        i = 0
        for text in myarray:
            blob = TextBlob(text)
            tup = (text, i % 2, blob.sentiment, blob.sentiment_assessments)
            items.append(tup)
            i += 1
        self.analysis = items
        return items
    
    def save(self):
        e = defaultdict(list)
        for element in self.analysis:
            e[element[1]].append({'party': str(element[0]), 'sentiments': element[2], 'sentiment_analysis': element[3]})

        # do not touch this #####
        with open('download.txt', 'w') as outfile:
            json.dump(dict(e), outfile)
        print(json.dumps(dict(e)))
        # dont touch^###########
        return ""

# splash page
@app.route("/")
def hello():
    return render_template("home.html")

#calls SALT.save()
@app.route("/download")
def download():
    current_salt.save()
    return ""

#loads the image and starts tesseract
# renders screen of messages
@app.route("/load", methods=['GET'])
def render_answer():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)
    root.quit()
    root.mainloop()
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe' 


    salt = Salt(root.filename)
    current_salt = salt
    txts = salt.analyze()
    salt.save()
    return render_template('results.html', path=root.filename, texts = salt.analyze())

if __name__ == "__main__":
	app.run(port=5000, debug=True)