# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# Copyright © 2012-13 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
import sys
from cgi import escape

class Page:
    """ページ描画クラス
    
    コンストラクタで渡されるRendererクラスについて知っているのは、
    ページ描画のためのインターフェイスを提供していること
    """

    def __init__(self, title, renderer):
        self.title = title
        self.renderer = renderer
        self. paragraphs = []

    def add_paragraph(self, paragraph):
        self.paragraphs.append(paragraph)

    def render(self):
        self.renderer.header(self.title)
        for paragraph in self.paragraphs:
            self.renderer.paragraph(paragraph)
        self.renderer.footer()

class TextRenderer:

    def __init__(self, width=80, file=sys.stdout):
        self.width = width
        self.file = file
        self.previous = False

    def header(self, title):
        self.file.write("{0:^{2}}\n{1:^{2}}\n"
        .format(title,"=" * len(title), self.width))

    def paragraph(self, text):
        if self.previous:
            self.file.write("\n")
            self.file.write(textwrap.fill(text, self.width))
            self.file.write("\n")
            self.previous = True
    
    def footer(self):
        pass

class HtmlRenderer:

    def __init__(self, htmlWriter):
        self.htmlWriter = htmlWriter

    def header(self, title):
        self.htmlWriter.header()
        self.htmlWriter.title(title)
        self.htmlWriter.start_body()

    def paragraph(self, text):
        self.htmlWriter.body(text)

    def footer(self):
        self.htmlWriter.end_body()
        self.htmlWriter.footer()

class HtmlWriter:
    """TextRendererと同じインタフェースで扱いたいクラス"""
    def __init__(self, file=sys.stdout):
        self.file = file

    def header(self):
        self.file.write("<!doctype html>\n<html>\n")

    def title(self, title):
         self.file.write("<head><title>{}</title></head>\n"
         .format(escape(title)))
    
    def start_body(self):
        self.file.write("<body>\n")

    def body(self, text):
        self.file.write("<p>{}</p>\n".format(escape(text)))

    def end_body(self):
        self.file.write("</body>\n")

    def footer(self):
        self.file.write("</html>\n")



def main():
    title = 'test'
    paragraph1 = 'para1'
    paragraph2 = 'para2'
    textPage = Page(title, TextRenderer(22))
    textPage.add_paragraph(paragraph1)
    textPage.add_paragraph(paragraph2)
    textPage.render()

    htmlPage = Page(title, HtmlRenderer(HtmlWriter()))
    htmlPage.add_paragraph(paragraph1)
    htmlPage.add_paragraph(paragraph2)
    htmlPage.render()

if __name__ == "__main__":
    main()
