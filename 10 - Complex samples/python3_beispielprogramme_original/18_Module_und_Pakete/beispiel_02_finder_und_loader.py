#!/usr/bin/env python

import sys
import os
import types

class TextLoader:
    def __init__(self, path):
        pass
    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.modules[fullname]
        module = types.ModuleType(fullname, "Docstring")
        module.__file__ = fullname + ".txt"
        module.__package__ = None
        module.__loader__ = self
        try:
            with open(fullname + ".txt") as f:
                module.text = f.read()
            sys.modules[fullname] = module
            return module
        except FileNotFoundError:
            raise ImportError


class TextFinder:
    def __init__(self, path):
        if path != "#":
            raise ImportError
    def find_module(self, fullname, path=None):
        if os.path.exists(fullname + ".txt"):
            return TextLoader(path)
        else:
            return None


if __name__ == "__main__":
    sys.path_hooks.append(TextFinder)
    sys.path.append("#")

    import testdatei
    print(testdatei.text)
    print(testdatei)
