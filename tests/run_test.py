# coding: utf8
__author__ = 'JinXing'
import os
import unittest


def suit():
    cwd = os.getcwd()
    modnames = []
    for filename in filter(lambda s: s.startswith("test_") and s.endswith(".py"), os.listdir(cwd)):
        modnames.append(os.path.splitext(filename)[0])
    return unittest.defaultTestLoader.loadTestsFromNames(modnames)


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suit())