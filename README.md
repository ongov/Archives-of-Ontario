# AI Archival File Lister Process Page
AI Process Page allows users to upload files and obtain their file name,
tilte, format and file size using Python's built-in tools, and extract keywords using AI-enable tool-Gensim.

This tool has been deployed for the Ministry of Government and Consumer Services. 

# Supported File Format
* .png
* .jpg
* .doc
* .docx
* .pptx
* .xlsx
* .pdf
* .mp4
* .wav

# How to Run the App on Your Laptop
**`All required libraries and software are downloaded and installed on a Red Hat Enterprise Linux Server (RHEL in short)`**

### Create a fileInfoGetter environment

#### If your operating system is RHEL

Run the following command in your terminal to clone the project from Gitlab repo:

    $ git clone https://gitlab.com/FarnazGoortani/gsic--ao.git
    

#### If your operating system is `NOT` RHEL

##### Option 1:

[Create a virtural machine](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Virtualization/3.0/html/Evaluation_Guide/Evaluation_Guide-SP-Create_New_VM.html), and then run the following command in your terminal to clone the project from Gitlab repo:

    $ git clone https://gitlab.com/FarnazGoortani/gsic--ao.git

##### Option 2:

Download and install [all the required libraries and software](#python-libraries-and-software-that-you-will-need) by yourself.

### Activate the environment (skip if you are following option 2)

Run the following command in your terminal

    $ source $HOME/fileInfoGetter/fileInfoGetterEnv/bin/activate

Your terminal should now look like this:

![User-entered text](/READMEimages/virtual_environment.jpg)

### Run the fileInfoGetter file

Finally, we can run the python file in terminal, or direcly run it on any Python IDE if you are following option 2.
    
    $ python3.6 fileInfoGetter.py
    
Enter the following URL in Google Chrome.

    http://localhost:5000

# What You Should See
Home Page
![User-entered text](/READMEimages/Homepage.PNG)

# Python Libraries and Software That You Will Need
All required libraries and software are already installed in virtual environment - fileInfoGetterEnv. Links are given for references.
### Python Libraries:
* [flask](http://flask.pocoo.org/) (to create the web application)
* [flask_dropzone](https://flask-dropzone.readthedocs.io/en/latest/) (to upload files on the website)
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/) (to generate result spreadsheet)
* [gensim](https://radimrehurek.com/gensim/summarization/keywords.html) (to extract keywords given plain text content)
* [docx2txt](https://github.com/ankushshah89/python-docx2txt) (to extract text content from .docx files)
* [pdfminer.six](https://github.com/pdfminer/pdfminer.six) (to extract text content from .pdf files)
* [speech_recognition](https://github.com/Uberi/speech_recognition#readme)(to perform text recognition on .mp4 files)
* [pptx](https://python-pptx.readthedocs.io/en/latest/) (to extract text content from .pptx files)
* [keras](https://keras.io/) (to perform object recognition for image files)
    * We are using the pre-trained model - [NASNet](https://keras.io/applications/#nasnet) to perform this task
* [wand](http://docs.wand-py.org/en/0.5.1/#user-s-guide) (to convert pdf files to png f(to find root word)iles)
* [hashlib](https://docs.python.org/3/library/hashlib.html) (to generate checksum)
* [nltk](https://www.nltk.org/) (to find root word)
### Software/Tools:
* [antiword](http://www.winfield.demon.nl/) (convert .dco to .docx files)
* [ffmpeg](https://www.ffmpeg.org/) (to convert .mp4 files to .wav files)
* [tesseract](https://github.com/tesseract-ocr/tesseract/wiki#centos-fedora-scientificlinux-opensuse-rhel-packages) (to perform character recognition for image files)
* [ImageMagick](https://www.imagemagick.org/) (to convert bitmap images)
* [TensorFlow](https://www.tensorflow.org/) (to execute keras)

# How to Deploy Application to a WSGI Server
The application is currently hosting on a Red Hat Enterprise Linux Server (RHEL in short), user name is `cliadmin`. 
RHEL works almost the same as CentOS, and here is the instruction:
[How To Serve Flask Applications with Gunicorn and Nginx on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-centos-7)

# How to Test and Refine the Tool
The tool consists of three python files: fileInfoGetter.py, infoGetter.py and Summarizer. 
fileInfoGetter.py is responsible for hosting the flask application and handle all the responses that are happening.
infoGetter.py contains all the helper functions, and lastly Summarizer is an object that can be used to summarize content of an article.
Whenever you want to make change to any of the three files, make sure you have a backup copy in case something goes wrong. This Gitlab site contains
the latest uploaded source code, so download the source codes from here and then start making changes on the server.

# How to Upload New File to Gitlab
If you wrote your source code on your local environment/laptop, you can upload your files here: https://www.file.io/, you will get a link.
Then go to the server and use the following command:

    $ wget https://file.io/example
    
After that you will see a file called 'example' under current working directory, make sure to assign a meaningful file name or replace with
an existing file using:

    $ mv example newfilename
    
In most of the cases, after you are done making changes, run the following three commands on the server:

    $ git add . --ignore-removal
The above command will add/overwrite the files that you have changed and ignore all the files that you have deleted.

    $ git commit -m "some meaningful comment"
The above command will commite all the added files to Gitlab.

    $ git push origin master
A simple push sends the made changes to the master branch of the remote repository associated with the working directory.
It will ask you the account and password that is associated with the master branch.

For more git basic commands, here is a [cheatsheet](https://www.hostinger.com/tutorials/basic-git-commands) for you.

# Things that You Need to Be Aware of

There are something that you may want to know before using this tool:
* Title extraction function is not working ideally because there is no universal pattern that can be applied to find the title of the file, we assume the first line of the file content to be the title however that does not apply to all the files.
* Unable to access the file path from user's end, this is because Flask does not want to expose necessary information about client's system
* Use the 'Empty Folder' button to get rid of failed files, if a file is unable to be processed, you have to remove it immediately, otherwise, whenever you upload a new file, the tool will start processing from the beginning of the folder and keeps failing.
* Do not upload more 50 files at once
* Please sperate video/audio files from common files such as .doc, .pdf as the process time will increase exponentially and cause the tool to crash. 

# Possible Future Enhancement
* Support more file format, so far the tool has covered over 80% of the commonly used file format. For office purposes, there is one more file format that can be added to the tool and it's challenging to do so - outlook data files. You need to configure an email client on the server, if you are interested in this, this [article](https://www.affordablewebdesign.com/outlook-email-setup-comcast-users/) may be helpful to you.
* Improve title extraction using A.I. with better model. Title extraction is the hardest task among all this tool's funcionalties as there is no universal pattern on every single files.
* Append information to the existing spreadsheet instead of making a new one. When users upload new files, the information will be added to the end of previous result.
