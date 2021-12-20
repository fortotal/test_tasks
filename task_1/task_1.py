from fire import Fire


def cars_order(red_cars: int = 3, white_cars: int = 3) -> str:
    assert red_cars >= 1 and white_cars >= 2, 'Минимальное кол-во красных машин - 1, белых - 2, по условию задачи'

    if red_cars >= white_cars:
        return 'Нет решения!'

    answer = 'WRW'
    red_cars -= 1
    white_cars -= 2

    if red_cars == 0 and white_cars > 0:
        return 'Нет решения!'

    while (red_cars > 0) and (white_cars > 0):
        if red_cars == white_cars:
            answer += 'RW' * red_cars
            return answer
        else:
            answer += 'WRW'
            red_cars -= 1
            white_cars -= 2

        if red_cars == 0 and white_cars > 0:
            return 'Нет решения!'

    return answer


if __name__ == '__main__':
    Fire(cars_order)
