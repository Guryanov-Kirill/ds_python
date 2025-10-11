# help вспомогательная функция, чтобы не вводить глобальную переменную
def help(n):   

    count = 0
    
    def queen(n, row, column, diagonal1, diagonal2):

        nonlocal count

        if n == row:
            count += 1
            return

        for col in range(n):

            # Проверяем можно ли поставить ферзя
            if (col not in column) and ((row - col) not in diagonal1) and ((row + col) not in diagonal2):

                # Если да, то добавляем ферзя в словари
                column[col] = True
                diagonal1[row - col] = True
                diagonal2[row + col] = True

                # Проверяем куда в следующей строке можно поставить ферзя (рекурсия)
                queen(n, row + 1, column, diagonal1, diagonal2)

                # Удаляем ферзя, чтобы проверить остальные варианты
                del column[col]
                del diagonal1[row - col]
                del diagonal2[row + col]

    queen(n, 0, {}, {}, {})
    return count


n = int(input())
print(help(n))


    