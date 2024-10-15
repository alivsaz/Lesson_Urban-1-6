# Задание "Свой YouTube"
from time import sleep

class UrTube:
    users = {}
    videos = {}
    current_user = None

    def log_in(self, nickname, password):
        if nickname in self.current_user and self.users[nickname] == hash(password):
            self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.current_user = nickname
            self.users[nickname] = [nickname, hash(password), age]
        else:
            print(f'Пользователь {nickname} уже существует')
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for video in other:
            self.videos[video.title] = [video.title, video.duration, video.time_now, video.adult_mode]

    def get_videos(self, video_title):
        list_video = []
        for key_video, val_video in self.videos.items():
            if video_title.lower() in val_video[0].lower():
                list_video.append(val_video[0])
        return list_video

    def watch_video(self, video_title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        else:
            for key_user, val_user  in self.users.items():
                if self.current_user == key_user and val_user[2] < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
        for key_video, val_video in self.videos.items():
            if video_title == val_video[0]:
                for i in range(val_video[1]):
                    sleep(1)
                    print(i+1, end=' ')
                print('Конец видео')
                return


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:

    def __init__(self, name, password, age):
        self.nickname = name
        self.password = hash(password)
        self.age = int(age)

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

print(f'\nВывод на консоль:\n')

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
