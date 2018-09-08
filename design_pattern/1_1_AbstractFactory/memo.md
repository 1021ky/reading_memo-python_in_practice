# memo

## AbstractFactoryデザインパターン

### 利用するケース
複数のオブジェクトで構成されるオブジェクトを生成する必要がある。
生成するものは複数種類あるが、構成されるオブジェクトのインターフェイスは同じ。
生成されたもの使う側は詳細なクラス構成を知らなくても適切なインスタンスを簡単に生成して使えるようにしたい。
例として、何らかの処理をして結果を画面に表示するプログラムを作りたい。画面はボタンやテキストやいろんな部品で構成される。画面の部品の構成は同じだがWindowsやMacやAndroidなどのOSごとに部品生成の詳細なロジックはわからなくとも、画面を構築できるようにしたいとき。

## pythonicな点

インスタンス生成に必要なクラスをFactoryクラスのインナークラスにしている。
Factoryの基底クラスにはオブジェクト生成時に使うインナークラス名を指定している。Factoryの基底クラスを継承していれば、Factoryが生成するのに必要なクラスのクラス名やインターフェイスが自然と同じになる。Factoryが生成するのに必要なクラスの基底クラスをいくつも作る必要がない。


## その他

### 読書メモ

デザインパターンは主にC++言語を対象として設計されたもの。
Pythonにとっては必要ないものもある。

### Pythonのメモ

ループを回す時に参照しない変数は_にすることがある

`for _ in range(10)`

ローカルスコープに定義されているシンボルとその値の辞書を返す。
https://docs.python.org/3/library/functions.html#locals
`locals()`

```python

# /usr/bin/env python3

a = 1
print('global')

print(locals())

def test_func():
    b = 1
    print('in func')
    print(locals())

class TestClass():

    def __init__(self):
        c = 1
        self.d = 1
        print('in class')
        print(locals())

    def test(self):
        e = 1
        print('in method')
        print(locals())

test_func()
t = TestClass()
t.test()

# 結果
# global
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10efd1358>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'test_local.py', '__cached__': None, 'a': 1}
# in func
# {'b': 1}
# in class
# {'c': 1, 'self': <__main__.TestClass object at 0x10f183588>}
# in method
# {'e': 1, 'self': <__main__.TestClass object at 0x10f183588>}
```

### 用語

パイソニック(Pythonic): Pythonらしい、きれいでよみやすいという意味で使われる。もともとは「ニシキヘビのような」の意味。