"""
1. ある数がその桁数の各桁をその桁数の累乗で足し合わせたとき、その合計が元の数と一致する場合、その数はアームストロング数です
2. 三桁の桁数がアームストロング数の場合(「スイセンの花」（Narcissus flower）)

水仙の花が、**「完全な調和」や「自分を見つめること」**を象徴する花としてよく描かれています。ギリシャ神話におけるナルシスの話（自分を愛しすぎて池の中の自分の姿に魅了されてしまう話）と関連して、ナルシス（Narcissus）という名前が「水仙花」と結びつけられています。

アームストロング数は、まさにその数が「自己に忠実である」かのように、自分自身をその桁数の累乗で再現するため、ナルシス（自分を映し出す）との関連から「水仙花数」と名付けられたとも考えられます。


学べること
1. 桁の数字を抽出 例えば、１０で割って、０以上の場合は、その１０のあまりで最後の桁の数を取得し、さらに１０で徐算、０以下になるまで、次の桁の値を取り出す。
2. 文字列変換やリスト変換で、簡潔に記載、また、繰り返し処理箇所は、リスト内包表記でリストに直接格納できる。
3. リストに変換することで、インデックス番号・フィルターリングなど拡張しやすくなる。例：odds = [i for i in range(10) if i % 2 == 1]

"""


def arm_num(N):
    temp = N
    list = []
    while temp / 10 > 0:
        s = temp % 10
        list.append(s)
        temp = temp // 10

    sum = 0
    digits = len(list)
    for item in list:
        sum += item**digits

    return sum == N


def arm_str(N):
    tempStr = str(N)
    sum = 0
    for item in tempStr:
        sum += int(item) ** len(tempStr)
    return sum == N


def arm_str_refactor(N):
    h = list(str(N))
    r = 0
    for i in range(len(h)):
        r += int(h[i]) ** len(h)
    return r == N


print(arm_str_refactor(153))
