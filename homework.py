class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: int,
                 speed: float,
                 calories: float 
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Вывести результат тренировки"""
        return (
            f'Тип тренировки: {self.training_type};'
            f'Длительность: {self.duration} ч.;'
            f'Дистанция: {self.distance} км;'
            f'Ср. скорость: {self.speed} км/ч;'
            f'Потрачено ккал: {self.calories}.') 

class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    TIME_IN_MIN: int = self.duration * 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = (self.action * LEN_STEP) / M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('Определите функцию в классах Running, SportsWalking, Swimming')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage()


class Running(Training):
    """Тренировка: бег."""
    coeff_calorie_1: int = 18
    coeff_calorie_2: int = 20
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        spent_calories = (coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2) * self.weight / M_IN_KM * Training.TIME_IN_MIN
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    WLK_coeff_calorie_1: float = 0.035
    WLK_coeff_calorie_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (WLK_coeff_calorie_1 * self.weight + (self.get_mean_speed**2 // self.height) 
                *WLK_coeff_calorie_2 * self.weight) * Training.TIME_IN_MIN


class Swimming(Training):
    """Тренировка: плавание."""
    SWM_coeff_calorie_1: float = 1.1
    SWM_coeff_calorie_2: float = 2.0 
    LEN_STEP: float = 1.38
    
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 lenght_pool: int,
                 count_pool: int
                 ) -> None:
        super(). __init__(action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        swim_mean_speed = self.lenght_pool * self.count_pool / M_IN_KM / self.duration
        return swim_mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        swim_spent_calories = (self.get_mean_speed + SWM_coeff_calorie_1) * SWM_coeff_calorie_2 * self.weight
        return swim_spent_calories

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        swim_distance = (self.action * LEN_STEP) / Training.M_IN_KM
        return swim_distance



def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

