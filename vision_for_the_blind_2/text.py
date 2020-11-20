# Fan Lin: 100%
import pytesseract
import cv2
from config import config
from PIL import Image
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


def image_bw(path):
    img = Image.open(path)
    img= img.convert('L')
    img.save('new.jpg')
    threshold = 200
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    photo = img.point(table, '1')
    photo.save('new2.jpg')
    newpath = 'new2.jpg'
    return newpath


def get_setence(newpath):
    image = cv2.imread(newpath)
    pytesseract.pytesseract.tesseract_cmd = config.properties['pytesseract_location']
    string = pytesseract.image_to_string(image)
    sentence = get_sentence(string)
    return sentence

def get_sentence(string):

    tokens = [t for t in string.split()]
    sw = stopwords.words('english')
    if tokens in sw:
        string.remove(tokens)
    nstring = sent_tokenize(string)
    return nstring
