number_one = list(map(int, input('data start: ').split()))
number_two = list(map(int, input('data end: ').split()))


def time_difference(number_one: number_one, number_two: number_two):
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
    }

    # для вычисления дней в году

    year1 = number_one[0]
    year2 = number_two[0]
    different_year = 0
    if year1 != year2:
        different_year += year2 - year1
        different_year *= 365

    # считаем дни в месяцах

    selected_values = [days_in_month.get(key) for key in range(number_one[1] + 1, number_two[1]) if
                       key in days_in_month]
    keys = days_in_month.keys()  # в эту переменную мы заключаем все ключи словаря days_in_month
    start_month = 0
    end_month = 0

    for i in keys:  # потом проходимся по всем ключам чтобы потом получить значение соответствующего ключа
        if number_two[1] == i:
            values1 = days_in_month.get(i)  # <--здесь мы получаем значение ключа
            start_month += values1 - number_one[2]
        end_month = number_two[2]

    a = sum(selected_values) + start_month + end_month
    all_days = a + different_year

    # для преобразования минуты и часов в секунды

    hour_in_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    min_in_hour = []
    if number_one[3] != number_two[3]:
        for i in hour_in_day:
            if i == number_one[3]:
                min_in_hour += hour_in_day[i - 1:]
            if i == number_two[3]:
                min_in_hour += hour_in_day[:i]
        if len(min_in_hour) <= 23:
            all_days -= 1
    min1 = [number_one[4]]
    min2 = [number_two[4]]
    bb = int(min2[0]) - int(min1[0])
    sec1 = number_one[5]
    sec2 = number_two[5]
    cc = sec2 - sec1
    sec_in_min = abs(int(bb)) * 60
    all_sec = len(min_in_hour) * 3600 + (cc + sec_in_min)
    result = all_days, all_sec

    return result


print(time_difference(number_one, number_two))
