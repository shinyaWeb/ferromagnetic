import numpy as np

# 書き込みデータのパス
path = './data_mf.dat'

n = 100  # 全粒子数はn^2

# 初期状態を定義
mg = [0 for i in range(2)]
mg[0] = np.random.randint(0, 2, (n, n))
mg[1] = np.random.randint(0, 2, (n, n))
n1 = 0
n0 = 0
for i in np.arange(0, n):
    for j in np.arange(0, n):
        mg[1][i][j] = mg[0][i][j]
        if mg[0][i][j] == 1:
            n1 += 1
        elif mg[0][i][j] == 0:
            n0 += 1
text = str(n1 / (n * n)) + " " + str(n0 / (n * n)) + "\n"
with open(path, mode='a') as f:
    f.write(text)

# 状態をターミナルへ出力
print(mg[0])
print("\n")

# 平均場の重み
a = 1

# 系の遷移
for k in range(5):
    for m in [0,1]:
        # 平均場の導入
        mf = a * (n1 - n0) / (n * n)

        n1 = 0
        n0 = 0
        # 内部の振舞い
        for i in np.arange(1, n - 1):
            for j in np.arange(1, n - 1):
                s = mg[m][i][j - 1] + mg[m][i][j + 1] + mg[m][i - 1][j] + mg[m][i + 1][j] + mf
                if s >= 2:
                    mg[(m + 1) % 2][i][j] = 1
                    n1 += 1
                elif s < 2:
                    mg[(m + 1) % 2][i][j] = 0
                    n0 += 1
        # 境界端の振舞い
        # 左上
        s = mg[m][1][0] + mg[m][0][1] + mf
        if s > 1:
            mg[(m + 1) % 2][0][0] = 1
            n1 += 1
        elif s <= 1:
            mg[(m + 1) % 2][0][0] = 0
            n0 += 1
        # 右上
        s = mg[m][0][n -2] + mg[m][1][n - 1] + mf
        if s > 1:
            mg[(m + 1) % 2][0][n -1] = 1
            n1 += 1
        elif s <= 1:
            mg[(m + 1) % 2][0][n - 1] = 0
            n0 += 1
        # 左下
        s = mg[m][n - 2][0] + mg[m][n - 1][1] + mf
        if s > 1:
            mg[(m + 1) % 2][n - 1][0] = 1
            n1 += 1
        elif s <= 1:
            mg[(m + 1) % 2][n - 1][0] = 0
            n0 += 1
        # 右下
        s = mg[m][n - 1][n - 2] + mg[m][n - 2][n - 1] + mf
        if s > 1:
            mg[(m + 1) % 2][n - 1][n - 1] = 1
            n1 += 1
        elif s <= 1:
            mg[(m + 1) % 2][n - 1][n - 1] = 0
            n0 += 1
        # 境界辺の振舞い
        for i in [0, n - 1]:
            if i == 0:
                for j in np.arange(1, n - 1):
                    s = mg[m][i][j - 1] + mg[m][i][j + 1] + mg[m][i + 1][j] + mf
                    if s > 1.5:
                        mg[(m + 1) % 2][i][j] = 1
                        n1 += 1
                    elif s <= 1.5:
                        mg[(m + 1) % 2][i][j] = 0
                        n0 += 1

                    s = mg[m][j - 1][i] + mg[m][j + 1][i] + mg[m][j][i + 1] + mf
                    if s > 1.5:
                        mg[(m + 1) % 2][j][i] = 1
                        n1 += 1
                    elif s <= 1.5:
                        mg[(m + 1) % 2][j][i] = 0
                        n0 += 1

            elif i == n - 1:
                for j in np.arange(1, n - 1):
                    s = mg[m][i][j - 1] + mg[m][i][j + 1] + mg[m][i - 1][j] + mf
                    if s > 1.5:
                        mg[(m + 1) % 2][i][j] = 1
                        n1 += 1
                    elif s <= 1.5:
                        mg[(m + 1) % 2][i][j] = 0
                        n0 += 1

                    s = mg[m][j - 1][i] + mg[m][j + 1][i] + mg[m][j][i - 1] + mf
                    if s > 1.5:
                        mg[(m + 1) % 2][j][i] = 1
                        n1 += 1
                    elif s <= 1.5:
                        mg[(m + 1) % 2][j][i] = 0
                        n0 += 1

        # 書き込み
        text = str(n1 / (n * n)) + " " + str(n0 / (n * n)) + "\n"
        with open(path, mode='a') as f:
            f.write(text)

        # 状態をターミナルへ出力
        print(mg[(m + 1) % 2])
        print("\n")
