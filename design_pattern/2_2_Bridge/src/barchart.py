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
path.insert("../../")

import Qtrac


class BarCharter:
    """棒グラフ描画クラス"""

    def __init__(self, renderer):
        if not isinstance(renderer, BarRenderer):
            raise TypeError(
                "Expected object of type BarRenderer, got {}".format(
                    type(renderer).__name__))
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
    pass

@Qtrac.has_methods("initialize", "draw_caption", "draw_bar", "finalize")
class ImageBarRenderer:
    pass


def main():
    pairs = (("Mon", 16), ("Tue", 17), ("Wed", 19), ("Thu", 22), ("Fri", 24),
             ("Sat", 21), ("Sun", 19))
    textBarCharter = BarCharter(TextBarRenderer())
    textBarCharter.render("Forecast 6/8", pairs)
    imageBarCharter = BarCharter(ImageBarRenderer())
    imageBarCharter.render("Forecast 6/8", pairs)