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

# 相対インポートは実行ディレクトリが決まっている前提となるためよくないけど、Qtrac importのため使う
from sys import path
path.append("../../common_src")

from PIL import Image, ImageColor, ImageDraw
import re
import os
import tempfile
import Qtrac


class BarCharter:
    """棒グラフ描画クラス"""

    def __init__(self, renderer):
        self.__renderer = renderer

    def render(self, caption, pairs):
        maximum = max(value for _, value in pairs)
        # 描画処理。
        # 描画クラスがもつインタフェースは以下の4つとなる
        self.__renderer.initialize(len(pairs), maximum)
        self.__renderer.draw_caption(caption)
        for name, value in pairs:
            self.__renderer.draw_bar(name, value)
        self.__renderer.finalize()


# デコレータで必要なインタフェースを具象クラスがもっていることを示す
@Qtrac.has_methods("initialize", "draw_caption", "draw_bar", "finalize")
class TextBarRenderer:
    """テキスト形式で棒グラフを描画するクラス"""
    def __init__(self, scaleFactor=40):
        self.scaleFactor = scaleFactor

    def initialize(self, bars, maximum):
        assert bars > 0 and maximum > 0
        self.scale = self.scaleFactor / maximum

    def draw_caption(self, caption):
        print("{0:^{2}}\n{1:^{2}}".format(caption, "=" * len(caption),
                                          self.scaleFactor))

    def draw_bar(self, name, value):
        print("{} {}".format("*" * int(value * self.scale), name))

    def finalize(self):
        pass

@Qtrac.has_methods("initialize", "draw_caption", "draw_bar", "finalize")
class ImageBarRenderer:
    """画像形式で棒グラフを描画するクラス"""
    COLORS = [
        ImageColor.getrgb(name)
        for name in ("red", "green", "blue", "yellow", "magenta", "cyan")
    ]

    def __init__(self, stepHeight=10, barWidth=30, barGap=2):
        self.stepHeight = stepHeight
        self.barWidth = barWidth
        self.barGap = barGap

    def finalize(self):
        self.image.save(self.filename)
        print("wrote", self.filename)

    def initialize(self, bars, maximum):
        assert bars > 0 and maximum > 0
        self.index = 0
        color = ImageColor.getrgb("white")
        self.image = Image.new(
            mode="RGB",
            size=(bars * (self.barWidth + self.barGap),
                  maximum * self.stepHeight),
            color=color)

    def draw_caption(self, caption):
        self.filename = os.path.join(tempfile.gettempdir(),
                                     re.sub(r"\W+", "_", caption) + ".png")

    def draw_bar(self, name, value):
        color = ImageBarRenderer.COLORS[self.index % len(
            ImageBarRenderer.COLORS)]
        _, height = self.image.size
        x0 = self.index * (self.barWidth + self.barGap)
        x1 = x0 + self.barWidth
        y0 = height - (value * self.stepHeight)
        y1 = height - 1
        draw = ImageDraw.Draw(self.image)
        draw.rectangle(xy=[(x0, y0), (x1, y1)], fill=color)
        self.index += 1


def main():
    pairs = (("Mon", 16), ("Tue", 17), ("Wed", 19), ("Thu", 22), ("Fri", 24),
             ("Sat", 21), ("Sun", 19))
    textBarCharter = BarCharter(TextBarRenderer())
    textBarCharter.render("Forecast 6/8", pairs)
    imageBarCharter = BarCharter(ImageBarRenderer())
    imageBarCharter.render("Forecast 6/8", pairs)


if __name__ == '__main__':
    main()