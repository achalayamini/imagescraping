# -*- coding: utf-8 -*-
import unittest
import shutil
import os
from webimages_downloader import check_url_error, create_images_directory 

class TestImageScraper(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        pass
    
    @classmethod
    def teardownClass(cls):
        pass

    def setUp(self):
	pass

    def tearDown(self):
        pass
    
    def test_1_verify_url_validity_success_case(self):
        url_obj = check_url_error("https://www.f-secure.com")
	assert url_obj != None, "Expected connection object, but observed None" 

    
    def test_2_verify_url_validity_failure_case(self):
        url_obj = check_url_error("http.f-secure.com")
	assert url_obj == None, "Error thrown due to invalid URL " 
    
    def test_3_verify_url_validity_timeout_case(self):
        url_obj = check_url_error("http://www.hm.com/fi")
        assert url_obj == None, "Expected No connection object, but observed server failure"

    def test_4_verify_image_downloaded(self):
	imgs_dir = os.path.join(os.getcwd(), "www.f-secure.com")
        if os.path.exists(imgs_dir):
	   shutil.rmtree(imgs_dir)
	create_images_directory("https://www.f-secure.com",  "https://www.f-secure.com/documents/10192/1661219/total_box_left_en_131x200.png")
	assert os.path.exists(imgs_dir), "failed to create a images directory to save files"
	no_of_files = os.listdir(imgs_dir) # dir is your directory path
	expected_no_of_images = 1
        assert expected_no_of_images == len(no_of_files), 'Number of images to be downloaded mismatched expected:%s observed:%s'%(expected_no_of_images, len(no_of_files))

def run_unit_tests():
  suite = unittest.TestLoader().loadTestsFromTestCase(TestImageScraper)
  unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_unit_tests()		        
        
