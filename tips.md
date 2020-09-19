# TIPS

あるいは毎回ググらないようにするためのメモ

# 標準入出力

## 標準入力

* 1行で一つの文字列、数値
```
str=input()
n=int(input())
```

* 1行で複数で個数が指定される文字列、数値
```
a, b = map(str, input().split())
a, b = map(int, input().split())
```

* 1行で複数で個数がわからない、list で受け取る文字列、数値
```
l = list(input().split())
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

## 標準出力


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

defaultdict を使う
