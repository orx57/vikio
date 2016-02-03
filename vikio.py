#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Vikio
    Yet another simple Wiki based on Bottle (Python micro web-framework)
    https://github.com/orx57/vikio
"""

from __future__ import (unicode_literals, absolute_import, print_function,
                        division)

import codecs

import CommonMark
import frontmatter
import yaml

from bottle import abort, error, redirect, route, run, static_file, template, view

parser = CommonMark.Parser()
renderer = CommonMark.HtmlRenderer()


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


def config(config_path='config.yml'):
    """Get configuration parameters
    Get data from YAML configuration file
    Return 
    """

    # Retrieve configuration data from configuration file
    try:
        vikio_config = yaml.load(file(config_path, 'r'))
    except yaml.YAMLError, exc:
        print('Error in configuration file: %s', exc)

    site = Struct(**vikio_config['site'])
    return site


@error(404)
@view('error')
def error_page(error):
    return dict(error=error, name=error.status, site=site)


@route('/css/<filename:path>')
def send_css(filename):
    return static_file(filename, root='./static/css')


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
def index():
    redirect("/page/index")


@route('/page')
@route('/page/')
@route('/page/<name>')
@view('default')
def page(name='index'):
    try:
        with codecs.open("pages/{}.md".format(name),
                         'r',
                         encoding='utf-8') as document:
            firstline = document.read(3)
            if firstline == '---':
                document.seek(0)
                data = frontmatter.load(document)
                title = data['title']
                ast = parser.parse(data.content)
            else:
                document.seek(0)
                title = name
                ast = parser.parse(document.read())
    except IOError:
        abort(404, "Requested page not found!")
    html = renderer.render(ast)
    return dict(content=html, name=title, site=site)


def main():
    """ Run the whole program """
    global site
    site = config()
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)


if __name__ == '__main__':
    main()

# vim: ai et ts=4 sts=4 sw=4 tw=79 cc=80 wrap wb nu sm
