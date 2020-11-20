# vision_for_the_blind_2
vision_for_the_blind_2 is a tool to help the blind.
It can extract text from an image, or capture information from the image.  

Currently, the following file formats are supported:

- Windows bitmaps - *.bmp, *.dib
- JPEG files - *.jpeg, *.jpg, *.jpe
- Portable Network Graphics - *.png 
- Portable image format - *.pbm, *.pgm, *.ppm *.pxm, *.pnm 
- Sun rasters - *.sr, *.ras
- TIFF files - *.tiff, *.tif 
- Radiance HDR - *.hdr, *.pic

To start, there are a few requirements. 
 
Please download the [model](https://drive.google.com/file/d/1yGfKPnTp29Va1ktGO9Or7phTgTvRqGPA/view?usp=sharing).  

You need to install pytesseract.  

`pip install pytesseract`  

Find the directory of installation. If you are in MacOS, it's likely to be `/usr/local/Cellar/tesseract/{version}/bin/tesseract`.  
Then go to `{project root directory}/config/config.py`.
Paste directory of installation to pytesseract_location property.  

For other properties in `config.py`, please update them with your local directory where you store `model_9.h5` and `tokenizer.p`.  
model_9.h5 is the model you just downloaded and tokenizer.p is included in github.

You need to download modules in nltk library like below.
```
$ python
>>> import nltk
>>> nltk.download("stopwords")
>>> nltk.download("sent_tokenize")
```

Also you need install all libraries in requirements.txt.

`pip install -r requirements.txt`  

Tensorflow doesn't work with Python with version > 3.8 in Windows. So if you are working on Windows, please use some lower version, 3.7.0 for example.   

Now there are two ways to use vision_for_the_blind_2-api and command line tool. We'll talk about them separately.

### API
Our rest API is developed using django. To use it, start it in your server.  
Go to {project root}/vision_for_the_blind_2, then run the following command in terminal.  

`python manage.py runserver`  


API is running and can accept requests.  
Now to read text from a picture, you need a rest client. We'll use [Postman](https://www.postman.com/) as an example.  
method: POST  
URL: {your server ip}:8000/file/upload  
You'll need two attributes in request body.  
- file, this is the file you want text from. Make sure you are using a tool that can send files.  
- option, option is optional. You have two options here:  
1, t (default) - extract text from an image  
2, c - capture information from an image (this is a dog for example.)  
Then you can send the request. You will get a plain text back.

### Command Line Tool
You can also use vision_for_the_blind_2 as command line tool.  
Go to {project root}/vision_for_the_blind_2, then you can run commands in terminal.   

`python vision_for_blind.py {full path of image}  `  


Make sure you have the full path, **including the extension**, of the image. Normally in MacOS, full path looks like `'Users/{your username}/...'`  

Like the API, you can also have option to capture the info with command like this:  
`python vision_for_blind.py {full path of image} c`  
You can also run the following to extract text, even though it's the default option:  
`python vision_for_blind.py {full path of image} t`  
 