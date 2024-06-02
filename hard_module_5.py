import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"Пользователь: {self.nickname}, Возраст: {self.age}"

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __str__(self):
        return f"Название фильма: {self.title}"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == hash(password):
                self.current_user = user
                print(f"Пользователь {user.nickname} вошел в систему")
                return
        print("Неверное имя пользователя или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему")

    def log_out(self):
        self.current_user = None
        print("Пользователь вышел из системы")

    def add(self, *videos):
        for new_video in videos:
            found = False
            for video in self.videos:
                if new_video.title == video.title:
                    found = True
                    print(f"Видео с названием '{new_video.title}' уже существует")
                    break

            if found != True:
                self.videos.append(new_video)
                print(f"Видео '{new_video.title}' добавлено")

    def __contains__(self, title):

        for video in self.videos:
            if video.title == title:
                return True
        return False

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode == True and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    return
                print(f"Воспроизведение видео '{title}':")
                for i in range(video.duration):
                    print(f"{i + 1} - cекунда воспроизведения")
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return
        print("Видео не найдено")


# Пример использования программы
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

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
