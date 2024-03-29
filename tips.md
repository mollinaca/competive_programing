# TIPS

あるいは毎回ググらないようにするためのメモ

# 標準入出力

## 標準入力

https://qiita.com/kyuna/items/8ee8916c2f4e36321a1c

### 1行

* 1文字, 1単語
```
S = input() # str
N = int(input()) # int
F = float(input()) # float
```

* 1単語の1文字を1要素ずつ（リスト）
```
l = list(input()) # list
```

* 複数単語（変数） ※個数があらかじめわかる場合
```
a,b = input().split() # str
a,b = map(int,input().split()) # int
```

* 複数単語（リスト） ※個数がわからない
```
l = input().split() # list 
l = list(map(int,input().split())) # list
```

* 1行で複数で個数がわからない、list で受け取る文字列、数値
```
l = list(input().split())
l = list(map(int,input().split()))
```
リストで可変長で受け取る

### 複数行

* n行で入力される1行1要素をリストで受け取る
```
l = [input() for x in range(n)]
l = [int(input()) for x in range(n)]
```

* 何行か事前に分からない標準入力(AOJででてくる、AtCoderでは見ない)
```
import sys
S = []
for line in sys.stdin:
    S.append (line.rstrip())
```

stdinのEOFを検知して終了するため、CLI実行でキーボード入力だと入力の終了ができない（たぶん）。
入力する文字列をテキストファイルに出力して、リダイレクトで実行する。
```
./input.py < input.txt
```

* 要素数の決まってる2点の座標
```
n = int(input())
p = [tuple(map(int, input().split())) for i in range(n)]
```
要素数nのtuple  
別に2点じゃなくてもOK


* 要素数の決まってる二次元配列（grid）
```
grid = [list(input()) for i in range(h)] # 文字列
grid = [[int(s) for s in list(input())] for i in range(h)] # 数値
```
高さh、幅は未定義

## 標準出力

* 1行
```
print (ans)
```

* 複数行（リスト）
```
for ans in l:
    print (ans)
```

* リストの要素をスペース区切りで出力する
```
print(' '.join(map(str, l)))
```


# イテレータ

## 数列の生成

`range()` を使う

```
for i in range(10):
    print(i, end=' ')
# 0 1 2 3 4 5 6 7 8 9

for i in reversed(range(10)):
    print(i, end=' ')
# 9 8 7 6 5 4 3 2 1 0 
```

## リストの初期化

```
l = [0] * 10
 => [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

```
l = list(map(lambda x: x, range(10)))
l = [x for x in range(10)]
 => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```
squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
 => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

2次元リストの初期化
```
l_2d = [[0] * 4 for i in range(3)]
 => [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```


### 文字列として受け取ったリストを数値のリストへ変換する

```
l_si = ['-10', '0', '100']
l_si_i = [int(s) for s in l_si]
```
配列の1要素目が文字列、以降が数字列といった入力を受け取るときに、まず1行の配列（文字列型）で受け取り、1要素目を切り出し、残りを再度配列に入れ直す、という処理に使う。  
※これもっと効率的に受け取る方法ありそう、 order, *args みたいな感じで  

## 辞書の初期化

```
d = {}
l = [x for x in range(10)]
for i in l:
    d[i] = 0

 => {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
```

### dict の ソート

https://note.nkmk.me/python-dict-list-sort/  
https://qiita.com/yousuke_yamaguchi/items/23014a3c8d8beb8ba073  

* key でソート
```
d = {'kokugo':65, 'suugaku':60, 'kagaku':90, 'butsuri':80}
d_sorted = sorted(d.items(), key=lambda x:x[0])
 => [('butsuri', 80), ('kagaku', 90), ('kokugo', 65), ('suugaku', 60)]
```

* value でソート
```
d = {'a':1, 'c':3, 'b':2, 'e':6, 'd':4}
d_sorted = sorted(d.items(), key=lambda x:x[1])
 => [('suugaku', 60), ('kokugo', 65), ('butsuri', 80), ('kagaku', 90)]
```
1要素がタプルのリストになることに注意

### dictが格納されたリストを複数のキーでソート

https://yucatio.hatenablog.com/entry/2020/01/05/145417  

```
list1 = [
    {'name': 'ぶどう',   'price': 5000, 'weight': 1000},
    {'name': 'もも',     'price': 3000, 'weight': 2000},
    {'name': 'りんご',   'price': 5000, 'weight': 5000},
    {'name': 'バナナ',   'price': 1500, 'weight': 1000},
    {'name': 'メロン',   'price': 5000, 'weight': 1200},
    {'name': 'マンゴー', 'price': 10000, 'weight': 900},
    {'name': 'みかん',  'price': 1500, 'weight': 5000},
]
```

#### key に `itemgetter` を使用する

```
from operator import itemgetter
sorted_list1 = sorted(list, key=itemgetter(第1キー, 第2キー, 第3キー))
```

#### lamda 関数を使用する

```
sorted_list = sorted(list1, key=lambda item: (item['price'] / item['weight'], item['price']))
sorted_list2 = sorted(list1, key=lambda item: (item['price'] / item['weight'], item['price']))
```


## 文字列の生成

```
import string
print(string.ascii_letters)   # -> a-zA-Z
print(string.ascii_lowercase) # -> a-z
print(string.ascii_uppercase) # -> A-Z
```

# HxWのグリッド

## gridを取得する ※少なくともhが指定される
```
h,w = map(int,input().split())
grid = [list(input()) for i in range(h)]
```

## すべてのマスを調査する

```
def grid_judge (y:int, x:int) -> bool:
    if x == 0 and y == 0: # 左上
        return True
    elif x == w-1 and y == 0: # 右上
        return True
    elif x == 0 and y == h-1: # 左下
        return True
    elif x == w-1 and y == h-1: # 右下
        return True
    elif y == 0: # 一番上列の端っこ以外
        return True
    elif y == h-1: # 一番下列の端っこ以外
        return True
    elif x == 0: # 一番左列の端っこ以外
        return True
    elif x == w-1: # 一番右列の端っこ以外
        return True
    else: # それ以外
        return True

    return False
```
※ grid はグローバル変数として扱う

# bit全探索

* bit-fullsearch
```
n = int(input())
for i in range(2**n):
    l = [0]*n
    for j in range(n):
        if ((i>>j)&1):
            l[n-1-j] = 1

    # 処理
    # print (i,l)
```
n桁のbit列を全パターン列挙し、条件を満たすかどうか調査する  

参考:  
https://qiita.com/gogotealove/items/11f9e83218926211083a  
https://qiita.com/conf8o/items/ba024813b9d9ce934d58  
https://qiita.com/conf8o/items/548d0baaf505f9bee91f  
