# TIPS

あるいは毎回ググらないようにするためのメモ

# 標準入出力

## 標準入力

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

