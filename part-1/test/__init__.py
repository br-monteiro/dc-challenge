import unittest

import test.src.test_utils as test_utils

def load_tests(loader, tests, pattern):
  suite = unittest.TestSuite()
  suite.addTests(loader.loadTestsFromModule(test_utils))

  return suite
