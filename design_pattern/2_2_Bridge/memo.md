# memo

## Bridge

### 利用するケース

> 機能と実装を分離したい場合、Bridge パターンが用いられる。

Mark Summerfield　著、斎藤 康毅　訳 2015年 O'Reilly Japan, Inc.

分離した実装は特定のインターフェイスを持っているようにして、
実装を追加しやすくする。

## pythonicな点
汎用的に使えるかはわからないが、特定のinterfaceを持っているかは、デコレータで実現している。

## その他


### 読書メモ

### Pythonのメモ
複数のsetから新たにsetを作りたいとき, |=で論理和をとっていけばよい。
```
>>> a = set([1,2,3])
>>> b = set([2,3,4])
>>> a | b
{1, 2, 3, 4}
```
普段あんまり論理和を使わず、|=ってなんだ？ってなったのでメモ。

Pillowライブラリはpythonで画像処理をするためのライブラリ。
もともと存在したPIL(Python Image Library)のフォーク版。
画像の読み込み、加工、作成に使える。

作成例
```
'''PILで画像を出力するサンプル'''

from PIL import Image, ImageColor

width = 192  # 画像の横幅
height = 120  # 画像の縦幅
size = (width, height)
image = Image.new(
    mode='RGBA', size=size, color=ImageColor.getrgb('red'))
image.save('./sample_red.png')
```

### 用語
