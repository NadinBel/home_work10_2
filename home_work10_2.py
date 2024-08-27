from threading import Thread
import time
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)
    def run(self):
        print(f'{self.name}, на нас напали!')
        count_enemy = 100
        day_combat = 0
        while count_enemy > 0:
            count_enemy -= self.power
            day_combat += 1
            print(f'{self.name}, сражается {day_combat} день(дня)..., осталось {count_enemy} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day_combat} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thread = first_knight
thread_2 = second_knight
thread.start()
thread_2.start()
thread.join()
thread_2.join()
