import time


def elevator():
        while True:
            try:
                floor_count = int(input('Введите этажность дома от 5 до 20: '))
                if 5 <= floor_count <= 20:
                    break
                else:
                    print('Ошибка ввода')

            except Exception as e:
                print('Ошибка ввода ' + e.__str__())

        while True:
            try:
                floor_height = float(input('Введите высоту одного этажа (метры) более 1 метра: '))
                if floor_height >= 1:
                    break
                else:
                    print('Ошибка ввода')

            except Exception as e:
                print('Ошибка ввода ' + e.__str__())

        while True:
            try:
                elevator_speed = float(input('Введите скорость лифта при движении (в метрах в секунду) от 0 до %s: '
                                             % str(floor_height)))
                if 0 < elevator_speed <= floor_height:
                    break
                else:
                    print('Ошибка ввода')

            except Exception as e:
                print('Ошибка ввода ' + e.__str__())

        while True:
            try:
                doors_time = int(input('Введите время между отрытием и закрытием дверей от 4 до 60 секунд: '))
                if 3 < doors_time < 60:
                    break
                else:
                    print('Ошибка ввода')

            except Exception as e:
                print('Ошибка ввода ' + e.__str__())

        start_run(floor_count, floor_height, elevator_speed, doors_time)
        # start_run(9, 2.2, 0.9, 4)


def start_run(floor_count, floor_height, elevator_speed, doors_time):
    while True:
        try:
            elevator_position = int(input('Введите на каком этаже находится лифт: '))
            if 0 < elevator_position <= floor_count:
                break
            else:
                print('Введённого этажа не сущетствует')

        except Exception as e:
            print('Ошибка ввода ' + e.__str__())
    user_position = 1
    user_quit = False
    # При необходимости можно при запуске также запрашивать с какого этажа будет ехать первоначально пользователь
    # Это не было сделано, т.к. пользователь может кататься на лифте, при этом отправка выполняется не только с 1 этажа
    elevator_latency = 0
    while True:
        while not user_quit:
            while True:
                try:
                    user_position = int(input('Введите на каком этаже вы находитесь: '))
                    if 0 < user_position <= floor_count:
                        break
                    else:
                        print('Введённого этажа не сущетствует')

                except Exception as e:
                    print('Ошибка ввода ' + e.__str__())
            print('Вы находитесь на %s этаже. Что делать?' % user_position)
            user_status = int(input('Введите 1 чтобы вызвать лифт, 2 чтобы уйти: '))
            if user_status == 2:
                user_quit = True
            else:
                print('Вы вызвали лифт. Ожидайте.')
                print('Лифт на %s.' % elevator_position)
                if elevator_position <= user_position:
                    for floor in range(elevator_position+1, user_position+1):
                        time.sleep(floor_height/elevator_speed)
                        print(u'Лифт на %s этаже ↑' % floor)
                elif elevator_position >= user_position:
                    for floor in range(elevator_position-1, user_position-1, -1):
                        time.sleep(floor_height / elevator_speed)
                        print(u'Лифт на %s этаже ↓' % floor)
                elevator_position = user_position
                print('Двери открылись.')
                time.sleep(doors_time/2)
                while True:
                    try:
                        user_nextposition = int(input('Введите этаж, на который вы хотите отправиться: '))
                        if 0 < user_nextposition <= floor_count:
                            break
                        else:
                            print('Введённого этажа не сущетствует')

                    except Exception as e:
                        print('Ошибка ввода ' + e.__str__())
                time.sleep(doors_time / 2)
                print('Двери закрылись.')
                if elevator_position <= user_nextposition:
                    for floor in range(elevator_position + 1, user_nextposition + 1):
                        time.sleep(floor_height / elevator_speed)
                        print(u'Лифт на %s этаже ↑' % floor)
                elif elevator_position >= user_nextposition:
                    for floor in range(elevator_position - 1, user_nextposition - 1, -1):
                        time.sleep(floor_height / elevator_speed)
                        print(u'Лифт на %s этаже ↓' % floor)
                elevator_position = user_nextposition
                print('Вы прибыли на %s этаж.' % elevator_position)
                print('Двери открылись.')
                time.sleep(doors_time)
                print('Двери закрылись.')
                break
        status = int(input('Введите 1 чтобы воспользоватся лифтом, или 2 чтобы завершить программу: '))
        if status == 1:
            user_quit = False
        else:
            break


elevator()