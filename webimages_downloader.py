# import libraries
# /usr/bin/env python
"""This script downloads all images from a given link"""
import os
import urllib2
import urlparse
import logging
from urllib import urlretrieve
from bs4 import BeautifulSoup

URLS_FILE = "UrlsFile.txt"
LOG_FILE = "WebImagesDownload.log"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def check_url_error(input_url):
    """Checks if input URL is valid"""
    conn = None
    try:
        req = urllib2.Request(input_url)
        conn = urllib2.urlopen(req)
    except urllib2.HTTPError, er1:
        print 'Exception:Error: Page cannot be reached %s' %er1.code
        logging.info('Exception:Page cannot be reached %s', er1.code)
    except urllib2.URLError:
        print "Exception:URL Error Observed"
        logging.info('Exception:URL Error Observed')
    except ValueError:
        print 'Exception:Error: Invalid URL'
        logging.info('Exception:Invalid URL was entered: %s', input_url)
    return conn


def create_url_file(url_link):
    """writes URL list to file"""
    url_link = url_link + "\n"
    url_files = os.path.join(OUTPUT_DIR, URLS_FILE)
    with open(URLS_FILE, "a") as f_variable:
        f_variable.write(url_link)

def create_images_directory(url, img_src_url):
    """Creates new directory"""
    obj = urlparse.urlparse(url)
    new_dir = "%s"%obj.hostname
    directory = os.path.join(OUTPUT_DIR, new_dir)
    if not os.path.exists(directory):
        os.makedirs(directory)
    img_name = img_src_url.split("/")[-1]
    filename = os.path.join(directory, img_name)
    try:
        urlretrieve(img_src_url, filename)
        print "Successfully Downloaded %s"%img_src_url
        logging.info('Successfully Downloaded %s', img_src_url)
    except Exception, exc:
        print 'Exception: Failed to download image from url %s, exception :%s'%(img_src_url, exc)
        logging.debug('Exc:Failed to download image from url %s, exception :%s'%(img_src_url, exc))

def start_logging():
    """Creates log file and starts logging"""
    log_format = '%(asctime)s:%(message)s'
    logging.basicConfig(filename=LOG_FILE, format=log_format, level=logging.DEBUG)
    logging.getLogger(LOG_FILE)


def start_image_scraping(urlconn, input_url):
    """Scrapes images from the web page"""
    soup_url = BeautifulSoup(urlconn, "lxml")
    logging.info('Link is parsed')
    #Find img tags from the parsed URL
    img_html_tags = soup_url.findAll("img", {"alt":True, "src":True})
    logging.info('Looking for images')
    for each_img_tag in img_html_tags:
        img_url_path = urlparse.urljoin(input_url, each_img_tag['src'])
        create_url_file(img_url_path)
        create_images_directory(input_url, img_url_path)
    print 'All images are downloaded.The links are available in %s file'%URLS_FILE

if __name__ == "__main__":
    #Take URL input from user
    start_logging()
    URL = raw_input("Enter url :")
    logging.info('URL is input: %s', URL)
    P_RESPONSE = urlparse.urlparse(URL)
    if P_RESPONSE.scheme == '' and P_RESPONSE.netloc == '':
        print 'http:// or https:// scheme is not defined. please prefix URL with appropriate scheme'
        logging.debug('http:// or https:// scheme not defined.Prefix URL with appropriate scheme')
        exit(1)
    URL_CONN = check_url_error(URL)
    if URL_CONN is None:
        print "URL cannot be authenticated, exiting the program"
        logging.debug("URL cannot be validated.Exiting program")
        exit(1)
    start_image_scraping(URL_CONN, URL)
