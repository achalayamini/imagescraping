README.txt
webimages_downloader.py

OBJECTIVE OF THE SCRIPT:

The module webimages_downloader.py is written to download all the images present in a web page. The user needs to enter a URL to a web page. The script then parses through the URL and finds all the images on the page. The images are then downloaded on to a new folder. The links(URLs) to each of the images are stored on a file on the local directory.

ASSUMPTIONS MADE: 
I have asssumed that the user is allowed to give an input from the command line.
Images are downloaded as it is presented in the server(no-resizing is considered if renderred in webpage)
The file with the URL list is appended on every use of the script. 

USAGE :
$ Python webimages_downloader.py
User needs to enter URL when prompted

PREREQUISITE:
External library BeautifulSoup needs to be installed

  Method of installation: 
    If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

           $ sudo apt-get install python-bs4 (for Python 2)
    If pip is installed, 
    
           $ sudo pip install beautifulsoup4

Parser lxml is installed
   
 Method of installation: 
    
    $ sudo apt-get install python-lxml
     
           or
     
     $ sudo pip install lxml  


FILES CREATED POST EXECUTION:

--The images from the given URL are downloaded to a new folder which is named based on the URL, under the current directory
--The folder includes the downloaded image files
--The file UrlsFile.txt which includes the URLs to all images is included in the current directory


DEBUGLOG:
WebImagesDownload.log is created in current directory

Unit tests:
Sample unittests have been included for the script. Some test scenarios from the functions check_url_error, create_url_file & create_images_director
have been tested in the unittests. The test scripts are located in the folder tests. Further functional test scenarios have been provided in the Test plan.

USAGE of UNITTEST:
$ python -m unittest tests.TestImageScraper

INFORMATION :
Python version : 2.7.12
External library used:BeautifulSoup
OS: UBUNTU 16

SOURCE FOLDER CONTAINS:
webimages_downloader.py
README
Test_Plan.txt

/tests
TestImageScraper.py
__init__.py

Additional information:
Given more time, I would like to add some authetication measures to the script, where the user would be prompted to enter authentication where required. Currently, the script exits if there are no permissions to download. 
