# map listの要素に対して一定の処理を行ったものを使いたい場合
# int KBから入力された値を読み込む


a, b = map(int, input().split())
if (a * b) % 2:
    print('Odd')
else:
    print('Even')