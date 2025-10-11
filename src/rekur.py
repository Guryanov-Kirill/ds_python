def is_safe(board, row, col):
    # Функция проверяет безопасность места, возвращает 1 если безопасно и 0 если не безопасно
    for i in range(row):
        # Проверка столбца
        if board[i] == col:
            return 0
        # Проверка главной диагонали
        if board[i] - i == col - row:
            return 0
        # Проверка побочной диагонали
        if board[i] + i == col + row:
            return 0
    return 1

def number_of_arrangements(n, row, board):
    # Функция для подсчета количества возможных расстановок ферзей
    
    # Обозначения:
    # n: размер доски
    # row: строки
    # col: столбцы
    # board: текущая расстановка ферзей
    # count: счетчик правильных(безопасных) расстановок
    
    # Если все ферзи расставлены успешно возвращаем 1
    if row == n:
        return 1
    
    count = 0

    for col in range(n):
        if is_safe(board, row, col) == 1:
            board[row] = col
            count += number_of_arrangements(n, row + 1, board)
            board[row] = -1  # После перебора вариантов с данным столбцом приравниваем к -1, чтобы перебрать остальные варианты
    
    return count

n = int(input())
print(number_of_arrangements(n, 0, [-1] * n))
