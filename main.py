import unittest
# from test01 import TestDemo,TestDemo1
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
# suite.addTest(TestDemo("test_01"))
# suite.addTest(TestDemo("test_02"))
# suite.addTest(TestDemo1("test_01"))
# suite.addTest(TestDemo1("test_02"))

# unittest.TestLoader() #不常用

case = unittest.defaultTestLoader.discover(start_dir='.',pattern="test*.py")  #从那个文件夹寻找文件
suite.addTest(case)

with open("测试报告.html","wb") as f:
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=f,title="测试报告",description="这是项目的描述、测试的描述等信息")
    runner.run(suite)