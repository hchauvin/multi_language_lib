#!/usr/bin/env python

import example

assert example.split("foo\tbar qux") == ["foo", "bar", "qux"]
