# memo

## Builderパターン

### 利用するケース
複数のオブジェクトで構成されるオブジェクトを生成する必要がある。
生成するものは複数種類あるが、構成されるオブジェクトのインターフェイスは同じ。
生成されたもの使う側は詳細なクラス構成を知らなくても適切なインスタンスを簡単に生成して使えるようにしたい。

## pythonicな点


## その他

### 読書メモ

### Pythonのメモ

実践Python3によるとabc.ABCMetaを与えると実行時にわずかなオーバーヘッドが発生するらしい。
> When the class definition is read, if __metaclass__ is defined then the callable assigned to it will be called instead of type(). This allows classes or functions to be written which monitor or alter the class creation process:
https://docs.python.org/2/reference/datamodel.html#customizing-class-creation
上記ドキュメントを読むと、通常はtype関数を使ってクラスが生成される。しかしmetaclassを設定するとtype関数以外のものを割り当てることができる。
このことからabc.ABCMetaで行っている処理がtype関数よりもオーバーヘッドがかかるのだろう。
そのためか、ドキュメントで抽象基底クラスとして使用することと書くだけにする場合もあるらしい。

Pythonのreモジュールはコンパイルされた正規表現をキャッシュに保持しているため、
その関数を呼び出しても2回目以降は正規表現のコンパイルは行われない。

### 用語


