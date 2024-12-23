# Одна куча демоверсия Егэ 2025
def game(s, m):
    if s <= 19: return m % 2 == 0
    if m == 0: return 0
    else:
        if m% 2 == 1:
            return game(s-2, m-1) or game(s-5, m-1) or game(s//3, m-1)
        else:
            return game(s - 2, m - 1) and game(s - 5, m - 1) and game(s // 3, m - 1)


s19 = []; s20 = []; s21 = []

for s in range(100, 19, -1):
    if game(s, 2) == 1: s19.append(s)
    if not(game(s, 1))  and game(s, 3):
        s20.append((s))
    if not(game(s, 2))  and game(s, 4):
        s21.append(s)
print('19', s19)
print('20', s20)
print('21', s21)

#Две кучи вариант на дз 23.12.24

def game2(a, s, m):
    if a+s >= 231: return m % 2 == 0
    if m == 0: return 0
    else:
        if m% 2 == 1:
            return game2(a + 1, s, m - 1) or game2(a * 2, s, m - 1) or game2(a, s + 1, m - 1) or game2(a, s * 2, m - 1)
        else:
            # return game(a+1, s, m-1) or game(a*2, s, m-1) or game(a, s+1, m-1) or game(a, s*2, m-1) при неудачном ходе
            return game2(a + 1, s, m - 1) and game2(a * 2, s, m - 1) and game2(a, s + 1, m - 1) and game2(a, s * 2, m - 1)


s19 = []; s20 = []; s21 = []

for s in range(1, 231-17):
    if game2(17, s, 2) == 1: s19.append(s)
    if not(game2(17, s, 1))   and game2(17, s, 3):
        s20.append(s)
    if not(game2(17, s, 2))  and game2(17, s, 4):
        s21.append(s)
#print('19', s19)
print('20', s20)
print('21', s21)
