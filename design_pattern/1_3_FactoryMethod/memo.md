# memo

## FactoryMethod

### 利用するケース

あるオブジェクトが要求されたときに、どのクラスをインスタンス化させればよいかは前もってわからない場合。

## pythonicな点

抽象メソッドであることを表すためにサブクラスとして再実装してほしいメソッドは、
NotImplemetedErrorを発生させるようにしている。このアプローチだと、`abc.ABCMeta`を与えると乗ってしまうオーバーヘッドはない。また、ドキュメントを見落としてしまって抽象メソッドだと気づかれないこともなくなる。ただし、クラスのインスタンス化はできてしまう。

駒クラスの定義をいちいち書かなくてもtype関数でサクッと書ける。継承させたいときは、__new__メソッドで継承するように定義してやればよい。
```python
    new = (lambda c: lambda Class: Piece.__new__(Class, c))(char)
    new.__name__ = "__new__"
    Class = type(name, (Piece,), dict(__slots__=(), __new__=new))
```

## その他

### 読書メモ

### Pythonのメモ

`sys.intern()`
https://docs.python.org/3.7/library/sys.html#sys.intern
引数で渡された文字列をinterned stringとして辞書に入れる。辞書に入っている文字列はその文字列を参照するパフォーマンスが少し早くなる。
代わりにその文字列はメモリに保持されつつける。

`itertools.cycle()`
> iterable から要素を取得し、そのコピーを保存するイテレータを作成します。iterable の全要素を返すと、セーブされたコピーから要素を返します。これを無限に繰り返します。
> cycle() は大きなメモリ領域を使用します。使用するメモリ量は iterable の大きさに依存します。

### 用語
