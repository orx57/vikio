#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Document here.
"""

from __future__ import (unicode_literals, absolute_import, print_function,
                        division)

import codecs

import CommonMark
import yaml

from bottle import error, route, run, static_file, template, view


parser = CommonMark.DocParser()
renderer = CommonMark.HTMLRenderer()


@error(404)
@view('error')
def error404(error):
    return dict(error=error)


@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='./static/img', mimetype='image/png')


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/pub')


@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='./static/pub', download=filename)


@route('/')
@route('/<name>')
def index(name='Stranger'):
    ast = parser.parse("Hello **{{name}}**, how are you?")
    html = renderer.render(ast)
    return template(html, name=name)


@route('/page/<name>')
@view('default')
def hello(name='index'):
    document = codecs.open("pages/{}.md".format(name), 'r', encoding='utf-8')
    ast = parser.parse(document.read())
    html = renderer.render(ast)
    return dict(content=html, name=name)


def main():
    """ Run the whole program """
    run(host='localhost', port=8080, debug=True, reloader=False)


if __name__ == '__main__':
    main()

# vim: ai et ts=4 sts=4 sw=4 tw=79 cc=80 wrap wb nu sm
