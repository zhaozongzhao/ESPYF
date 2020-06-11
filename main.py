import unittest

from Common import config
from Common import logger2

#测试套件
s = unittest.TestSuite()
ts = unittest.TestLoader()
print(config.base_dir + "TestCases")
s.addTests(ts.discover(config.base_dir + "TestCases"))

