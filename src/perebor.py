import itertools

# Функция проверяет является ли расстановка корректной
def correct_placement(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Проверка на главную диагональ
            if abs(board[i] - board[j]) == abs(i - j):
                return False
            # Проверка на побочную диагональ
            if board[i] + i == board[j] + j:
                return False
    return True

n = int(input())
count = 0
# Перебор всех возможных расстановок
for permutation in itertools.permutations(range(n)):
    if correct_placement(permutation):
        count += 1
print(count)
