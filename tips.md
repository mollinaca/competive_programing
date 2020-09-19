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
a,b = map(str,input().split()) # str
a,b = map(int,input().split()) # int
```

* 複数単語（リスト） ※個数がわからない
```
l = input().split() # list 
l = list(map(int,input().split())) # list
```

### 複数行

* 1行で複数で個数が指定される文字列、数値

* 1行で複数で個数がわからない、list で受け取る文字列、数値
```
l = input().split()
l = list(map(int,input().split()))
```

* 何行か事前に分からない標準入力
```
import sys
s = []
for line in sys.stdin:
    s.append (list(line.rstrip()))
```

stdinのEOFを検知して終了するため、CLI実行でキーボード入力だと入力の終了ができない（たぶん）。
入力する文字列をテキストファイルに出力して、リダイレクトで実行する。
```
./input.py < input.txt
```

* 要素数の決まってる二次元配列（grid）
```
grid = [list(input()) for i in range(h)]
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
d_sorted = sorted(d.items(), key=lambda x:x[0])
 => [('suugaku', 60), ('kokugo', 65), ('butsuri', 80), ('kagaku', 90)]
```
1要素がタプルのリストになることに注意
