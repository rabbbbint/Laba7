def count_ways_to_climb(n):

    if n <= 1:
        return 1

    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


def print_ways_to_climb(n):
    """
    Функция, которая возвращает список строк, описывающих все возможные
    способы, которыми пользователь может подняться на n ступеней.
    """
    if n <= 1:
        return [str(n)]

    ways = [[] for _ in range(n + 1)]
    ways[0] = ['']
    ways[1] = ['1']

    for i in range(2, n + 1):
        for way in ways[i - 1]:
            ways[i].append(f'1 {way}')
        for way in ways[i - 2]:
            ways[i].append(f'2 {way}')

    return ways[n]


stairs = int(input("Введите количество ступенек: "))
print(f"Количество способов подняться на {stairs} ступеньку(и): {count_ways_to_climb(stairs)}")
print("Способы подняться:")
for g in print_ways_to_climb(stairs):
    print(g)
