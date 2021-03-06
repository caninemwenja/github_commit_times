#!/usr/bin/env python

__author__ = "Canine Mwenja"

import unittest
import os

from mock import Mock
from lib.fetcher import Fetcher

class FetcherTest(unittest.TestCase):
	""" testing for success of Fetcher functions """

	def get_data_file(self, filename):
		""" returns the content of a test data file in ./data"""
		test_data = os.path.join(os.path.dirname(__file__), "data")
		f = open(os.path.join(test_data,filename))
		data = f.read()
		f.close()
		return data

	def setUp(self):
		self.fetcher = Fetcher()

	def test_get_full_url(self):
		control_data = "https://api.github.com/helloworld"
		result_url = self.fetcher.get_full_url("helloworld")
		self.assertEqual(control_data, result_url, "Full URL does not match: "+control_data+" vs "+result_url)

	def test_process_repo_single_repo(self):
		self.fetcher.get_from_net = Mock(return_value=self.get_data_file("octocat.Spoon-Knife.json"))
		result = self.fetcher.process_repo("")

		self.assertIsInstance(result, type(list()), "Result was not a list")
		self.assertNotEqual(len(result), 0, "List is empty")
		self.assertEqual(len(result), 1, "List has extra items")
		self.assertIsInstance(result[0], type(dict()), "List item is not a dictionary: "+repr(result[0]))

		# testing membership
		self.assertIn("full_name", result[0], "Full name missing from dictionary: "+ repr(result[0]))
		self.assertIn("name", result[0], "Name missing from dictionary: "+ repr(result[0]))
		self.assertIn("fork", result[0], "Fork missing from dictionary: "+ repr(result[0]))
		self.assertIn("url", result[0], "URL missing from dictionary: "+ repr(result[0]))
		self.assertIn("language", result[0], "Language missing from dictionary: "+ repr(result[0]))
		self.assertIn("created", result[0], "Created missing from dictionary: "+ repr(result[0]))

		# testing values
		self.assertEqual(result[0]["full_name"], "octocat/Spoon-Knife", "Full name does not match, Fullname: "+ repr(result[0]["full_name"]))
		self.assertEqual(result[0]["name"], "Spoon-Knife", "Name does not match, Name: "+ repr(result[0]["name"]))
		self.assertEqual(result[0]["fork"], False, "Fork does not match, Fork: "+ repr(result[0]["fork"]))
		self.assertEqual(result[0]["url"], "https://api.github.com/repos/octocat/Spoon-Knife", "URL does not match, URL: "+ repr(result[0]["url"]))
		self.assertEqual(result[0]["language"], None, "Langauge does not match, Language: "+ repr(result[0]["language"]))
		self.assertEqual(result[0]["created"], "2011-01-27T19:30:43Z", "Created does not match, Created: "+ repr(result[0]["created"]))

	def test_process_repo_multiple_repo(self):
		self.fetcher.get_from_net = Mock(return_value=self.get_data_file("octocat.json"))
		result = self.fetcher.process_repo("", True)

		self.assertIsInstance(result, type(list()), "Result was not a list")
		self.assertNotEqual(len(result), 0, "List is empty")
		self.assertEqual(len(result), 3, "List has extra items")
		self.assertIsInstance(result[0], type(dict()), "List item is not a dictionary: "+repr(result[0]))
		self.assertIsInstance(result[1], type(dict()), "List item is not a dictionary: "+repr(result[0]))
		self.assertIsInstance(result[2], type(dict()), "List item is not a dictionary: "+repr(result[0]))

		# testing membership - first item
		self.assertIn("full_name", result[0], "Full name missing from dictionary: "+ repr(result[0]))
		self.assertIn("name", result[0], "Name missing from dictionary: "+ repr(result[0]))
		self.assertIn("fork", result[0], "Fork missing from dictionary: "+ repr(result[0]))
		self.assertIn("url", result[0], "URL missing from dictionary: "+ repr(result[0]))
		self.assertIn("language", result[0], "Language missing from dictionary: "+ repr(result[0]))
		self.assertIn("created", result[0], "Created missing from dictionary: "+ repr(result[0]))

		# testing membership - second item
		self.assertIn("full_name", result[1], "Full name missing from dictionary: "+ repr(result[1]))
		self.assertIn("name", result[1], "Name missing from dictionary: "+ repr(result[1]))
		self.assertIn("fork", result[1], "Fork missing from dictionary: "+ repr(result[1]))
		self.assertIn("url", result[1], "URL missing from dictionary: "+ repr(result[1]))
		self.assertIn("language", result[1], "Language missing from dictionary: "+ repr(result[1]))
		self.assertIn("created", result[1], "Created missing from dictionary: "+ repr(result[1]))

		# testing values - third item
		self.assertEqual(result[2]["full_name"], "octocat/ThisIsATest", "Full name does not match, Fullname: "+ repr(result[2]["full_name"]))
		self.assertEqual(result[2]["name"], "ThisIsATest", "Name does not match, Name: "+ repr(result[2]["name"]))
		self.assertEqual(result[2]["fork"], False, "Fork does not match, Fork: "+ repr(result[2]["fork"]))
		self.assertEqual(result[2]["url"], "https://api.github.com/repos/octocat/ThisIsATest", "URL does not match, URL: "+ repr(result[2]["url"]))
		self.assertEqual(result[2]["language"], None, "Langauge does not match, Language: "+ repr(result[2]["language"]))
		self.assertEqual(result[2]["created"], "2012-03-07T23:25:47Z", "Created does not match, Created: "+ repr(result[2]["created"]))

	def tearDown(self):
		self.fetcher = None

if __name__ == "__main__":
	unittest.main()
