import unittest
from unittest.mock import Mock, patch
from ..handlers import TableHandler as TH

class Test_Methods(unittest.TestCase): 
    test = TH.TableHandler()
    def test_pad_s__(self):
        string = "test_string"
        size = 10
        expected = "test_string"

        string = self.test.__padtosize__(string,size,False)

        assert expected == string
        print("pad normal S case")

    def test_pad_f__(self):
        string = "test_string"
        size = 10
        expected = "test_string "

        string = self.test.__padtosize__(string,size,False)

        assert expected != string

        print("pad normal F case")

    def test_pad_s_e__(self):
        string = "test_string"
        size = 12
        expected = "|test_string|"

        string = self.test.__padtosize__(string,size)

        assert expected == string

        print("pad edge s case")   

    def test_pad_f_e__(self):
        string = "test_string"
        size = 13
        expected = "|test_string|"

        string = self.test.__padtosize__(string,size)

        assert expected != string

        print("pad edge s case") 
    
    @unittest.mock.patch("models.handlers.TableHandler")
    def test_print_seperator(self):

        expected = None


if __name__ == "__main__":
    unittest.main()