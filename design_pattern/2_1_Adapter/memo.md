# memo

## Adapter

### 利用するケース

> あるクラスが、互換性のないインタフェースを持つ別のクラスを利用したい場合、そのどちらのクラスも変更することなしに利用する。

Mark Summerfield　著、斎藤 康毅　訳 2015年 O'Reilly Japan, Inc.

クラスの変更をなくすためにAdapterには移譲を使ったり、
継承を使う。

## pythonicな点


## その他
pythonでAdapterパターンを継承で実現しようとすると、
書籍に書かれている通りPageクラス内でレンダラークラスがAdapterクラスを継承しているか確認するロジックを書く必要がある。
大規模なプログラムを書くのならば、それもいいけど、
ちょっと気軽に書きたいときは、今回みたいに移譲で書いたほうが楽。

### 読書メモ

### Pythonのメモ
> ユーザーが -O オプション(optimize つまり 最適化)を指定してプログラムを実行した場合、assert が無視される
Mark Summerfield　著、斎藤 康毅　訳 2015年 O'Reilly Japan, Inc.

__subclasshook__() という特殊メソッドはisinstance()で使われる

あるクラスの属性がプロパティかメソッドか判別したい場合はcallableメソッドで判定できる

文字列フォーマットを指定する方法の1つで、^[minimum field width]と指定すると、[minimum field width]の長さになるまで文字列を空白で埋めて、
かつフォーマット対象の文字列が中央になる。
```
>>> '{:^30}'.format('centered')
'           centered           '
```
### 用語
