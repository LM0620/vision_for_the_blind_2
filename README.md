# vision_for_the_blind_2
vision_for_the_blind_2 is a tool to help the blind.
It can extract text from an image, or capture information from the image.  

Currently, the following file formats are supported:

- Windows bitmaps - *.bmp, *.dib (always supported)
- JPEG files - *.jpeg, *.jpg, *.jpe (see the Note section)
- JPEG 2000 files - *.jp2 (see the Note section)
- Portable Network Graphics - *.png (see the Note section)
- WebP - *.webp (see the Note section)
- Portable image format - *.pbm, *.pgm, *.ppm *.pxm, *.pnm (always supported)
- PFM files - *.pfm (see the Note section)
- Sun rasters - *.sr, *.ras (always supported)
- TIFF files - *.tiff, *.tif (see the Note section)
- OpenEXR Image files - *.exr (see the Note section)
- Radiance HDR - *.hdr, *.pic (always supported)
- Raster and Vector geospatial data supported by GDAL (see the Note section)  

To start, there are a few requirements.  
You need to install pytesseract.  

`pip install pytesseract`  

Find the directory of installation. If you are in MacOS, it's likely to be `/usr/local/Cellar/tesseract/{version}/bin/tesseract`.  
Then go to `{project root directory}/config/config.py`.
Paste directory of installation to pytesseract_location property.  

You need to download modules in nltk library like below.
```
$ python
>>> import nltk
>>> nltk.download("stopwords")
>>> nltk.download("sent_tokenize")
```

Also you need install all libraries in requirements.txt.

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


Make sure you have the full path, including the extension, of the image. Normally in MacOS, full path looks like `'Users/{your username}/...'`  

Like the API, you can also have option to capture the info with command like this:  
`python vision_for_blind.py {full path of image} c`  
You can also run the following to extract text, even though it's the default option:  
 `python vision_for_blind.py {full path of image} t`  
 