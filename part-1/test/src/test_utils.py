import unittest
import src.utils as utils

class TestUtils(unittest.TestCase):
  def test_getdictkeys(self):
    input_test = {
      'c': 'test',
      'a': 'test',
      'b': 'test',
    }

    self.assertEqual(['a', 'b', 'c'], utils.getdictkeys(input_test))
    self.assertEqual(['a', 'b', 'c'], utils.getdictkeys(input_test))
    self.assertEqual([], utils.getdictkeys({}))
    self.assertEqual([], utils.getdictkeys(True))
    self.assertEqual([], utils.getdictkeys(''))
    self.assertEqual([], utils.getdictkeys(1))
    self.assertEqual([], utils.getdictkeys(1.4))

  def test_sortlist(self):
    value = ['x', 'b','a', True, 1, {}, [], 1, 2.5]
    expected = [{}, [], 2.5, True, 1, 1, 'a', 'b', 'x']
    self.assertEqual(expected, utils.sortlist(value))

  def test_sortdict(self):
    value = {'z': True, 'a': 't', 'b': 1}
    expected = {'a': 't', 'b': 1, 'z': True}
    self.assertEqual(expected, utils.sortdict(value))

  def test_gethash(self):
    self.assertEqual(40, len(utils.gethash('test')))
    self.assertEqual('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3', utils.gethash('test'))
    self.assertEqual('bf21a9e8fbc5a3846fb05b4fa0859e0917b2202f', utils.gethash({}))
    self.assertEqual('97d170e1550eee4afc0af065b78cda302a97674c', utils.gethash([]))
    self.assertEqual('88b33e4e12f75ac8bf792aebde41f1a090f3a612', utils.gethash(True))
    self.assertEqual('97cdbdc7feff827efb082a6b6dd2727237cd49fd', utils.gethash(False))
    self.assertEqual('356a192b7913b04c54574d18c28d46e6395428ab', utils.gethash(1))
    self.assertEqual('b6589fc6ab0dc82cf12099d1c2d40ab994e8410c', utils.gethash(0))
