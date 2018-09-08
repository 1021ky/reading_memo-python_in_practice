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

"""
AbstractFactoryパターンのサンプル
"""


class DiagramFactory():
    """図形ファクトリクラスの基底クラス"""

    @classmethod
    def make_diagram(Class, width, height):
        return Class.Diagram(width, height)

    @classmethod
    def make_rectangle(Class, x, y, width, height, fill="white", stroke="black"):
        return Class.Rectangle(x, y, width, height, fill, stroke)

    @classmethod
    def make_text(Class, x, y, text, fontsize=12):
        return Class.Text(x, y, text, fontsize)


    # デフォルトの設定値
    BLANK = " "
    CORNER = "+"
    HORIZONTAL = "-"
    VERTICAL = "|"


    class Component():
        """図形の構成要素基底クラス"""
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Rectangle(Component):
        """四角形クラス"""
        
        def __init__(self, x, y, width, height, fill, stroke):
            super().__init__(x, y)
            self.width = width
            self.height = height
            self.fill = DiagramFactory.BLANK if fill == "white" else "%"
            self.stroke = stroke
            self.rows = self._create_rows()

        def _create_rows(self):
            rows = [[self.fill for _ in range(self.width)] for _ in range(self.height)]
            for x in range(1, self.width - 1):
                rows[0][x] = DiagramFactory.HORIZONTAL
                rows[self.height - 1][x] = DiagramFactory.HORIZONTAL
            for y in range(1, self.height - 1):
                rows[y][0] = DiagramFactory.VERTICAL
                rows[y][self.width - 1] = DiagramFactory.VERTICAL
            for y, x in ((0, 0), (0, self.width - 1), (self.height - 1, 0),
                    (self.height - 1, self.width -1)):
                rows[y][x] = DiagramFactory.CORNER
            return rows


    class Text(Component):
        """テキストクラス"""
        
        def __init__(self, x, y, text, fontsize):
            super().__init__(x, y)
            self.text = text
            self.fontsize = fontsize
            self.rows = [list(text)]


    class Diagram():
        """図形クラス"""
        
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.diagram = DiagramFactory.Rectangle(0, 0, width, height, DiagramFactory.BLANK, None).rows
        
        def add(self, component):
            for y, row in enumerate(component.rows):
                for x, char in enumerate(row):
                    self.diagram[y + component.y][x + component.x] = char

        def save(self, filename):
            with open(filename, "w", encoding="utf-8") as file:
                for row in self.diagram:
                    print("".join(row), file=file)


class SvgDiagramFactory(DiagramFactory):

    # The make_* class methods are inherited

    SVG_START = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
    "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"
    width="{pxwidth}px" height="{pxheight}px">"""

    SVG_END = "</svg>\n"

    SVG_RECTANGLE = """<rect x="{x}" y="{y}" width="{width}" \
height="{height}" fill="{fill}" widthe="{width}"/>"""

    SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
font-family="sans-serif" font-size="{fontsize}">{text}</text>"""

    SVG_SCALE = 20


    class Diagram:

        def __init__(self, width, height):
            pxwidth = width * SvgDiagramFactory.SVG_SCALE
            pxheight = height * SvgDiagramFactory.SVG_SCALE
            self.diagram = [SvgDiagramFactory.SVG_START.format(**locals())]
            outline = SvgDiagramFactory.Rectangle(0, 0, width, height,
                    "lightgreen", "black")
            self.diagram.append(outline.svg)


        def add(self, component):
            self.diagram.append(component.svg)


        def save(self, filename):
            with open(filename, "w", encoding="utf-8") as file:
                file.write("\n".join(self.diagram))
                file.write("\n" + SvgDiagramFactory.SVG_END)


    class Rectangle:

        def __init__(self, x, y, width, height, fill, stroke):
            x *= SvgDiagramFactory.SVG_SCALE
            y *= SvgDiagramFactory.SVG_SCALE
            width *= SvgDiagramFactory.SVG_SCALE
            height *= SvgDiagramFactory.SVG_SCALE
            self.svg = SvgDiagramFactory.SVG_RECTANGLE.format(**locals())


    class Text:

        def __init__(self, x, y, text, fontsize):
            x *= SvgDiagramFactory.SVG_SCALE
            y *= SvgDiagramFactory.SVG_SCALE
            fontsize *= SvgDiagramFactory.SVG_SCALE // 10
            self.svg = SvgDiagramFactory.SVG_TEXT.format(**locals())


def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram

def main():
    textFilename = "./diagram.txt"
    txtDiagram = create_diagram(DiagramFactory)
    txtDiagram.save(textFilename)
    print("wrote", textFilename)

    svgFilename = "./diagram.svg"
    svgDiagram = create_diagram(SvgDiagramFactory)
    svgDiagram.save(svgFilename)
    print("wrote", svgFilename)

if __name__ == '__main__':
    main()
    create_diagram(DiagramFactory)
