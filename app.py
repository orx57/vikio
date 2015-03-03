#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Document here.
"""

from __future__ import (unicode_literals, absolute_import,
                        print_function, division)

from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


def main():
    """ Run the whole program """
    run(host='localhost', port=8080)


if __name__ == '__main__':
    main()
