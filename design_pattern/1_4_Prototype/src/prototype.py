# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""新しいオブジェクトをクローンによって生成するパターン

pythonだと特になにか考えて設計する必要はない。
やり方はいくつかある。
"""
from copy import deepcopy

class Point:
    """複製対象のシンプルなクラス"""    

    def __init__(self, x, y):
        self.x = x
        self.y = y

# クラスからインスタンスを生成する(通常の手段)
p = Point(1, 2)

# 汎用的な複製関数を用意する
def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)

point1 = make_object(Point, 5, 10)
# copyモジュールのdeepcopyを使う
point2 = deepcopy(p)
# インスタンスのクラスオブジェクトを参照して生成する
point3 = p.__class__(7, 14)
