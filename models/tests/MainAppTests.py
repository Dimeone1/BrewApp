import unittest
import NameStorage

class TestMethods(unittest.TestCase):
    def test_search_key_s(self):
        #Arrange
        key = "drink"
        searchdata = "cola"
        searchlist = [{"name":"Nathan", "drink":"cola"}] 
        #Act
        result = NameStorage.search_for_key(key, searchdata, searchlist)
        #Assert
        assert result == [{"name":"Nathan", "drink":"cola"}]
        print("search key found case success")

    def test_search_key_f(self):
        #Arrange
        key = "drink"
        searchdata = "cola"
        searchlist = [{"name":"Nathan", "drink":"Cola"}] 
        #Act
        result = NameStorage.search_for_key(key, searchdata, searchlist)
        #Assert
        assert result == None
        print("search key fail case success")