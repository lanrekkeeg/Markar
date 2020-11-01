# tests/runner.py
import unittest
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()
import test
# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test))


# initialize a runner, pass it your suite and run it
#runner = unittest.TextTestRunner(verbosity=3)
#result = runner.run(suite)
#print(type(result))
# initialize a runner, pass it your suite and run it
#runner = unittest.TextTestRunner(verbosity=3)
#result = runner.run(suite)

kwargs = {
    "output": "reports",
    "report_name": "sub_2",
    "failfast": True
}
runner = HTMLTestRunner(**kwargs)
runner.run(suite)