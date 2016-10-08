import unittest
from algorithm import search

class TestSearch(unittest.TestCase):
	def setUp(self):
         self.array = [5,6,44,3,3,2,3,7,5]

	def test_succesfull(self):
         self.assertTrue(search(self.array,3,3))

	def test_failed(self):
         self.assertFalse(search(self.array,5,5))

	def test_emptyArray(self):
         self.assertFalse(search([],2,10))

	def test_whenArrayIsNone(self):
         self.assertFalse(None,5)

	def test_searchingNoneFailed(self):
  	 self.assertFalse(search(self.array,2,None))
	def test_searchingNoneNumberFailed(self):
         self.assertFalse(search(self.array,None,5))



if __name__ =='__main__':
 unittest.main()
