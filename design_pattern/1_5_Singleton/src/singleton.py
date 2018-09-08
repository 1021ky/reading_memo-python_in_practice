# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""Singletonパターン"""

def get(refresh=False):
    """インスタンスが一つだけ必要でそのインスタンスにプログラム全体からアクセスできるようにする関数"""    
    if refresh:
        get.data = {}
    if get.data:
        return get.data
    # refresh=Trueか初めて呼ばれたときのみ行う処理
    # サンプルなので簡単な処理にしている
    get.data = {'data': 'hoge'}

    return get.data
    
# モジュールインポートのときに初期化しておく
get.data = {}