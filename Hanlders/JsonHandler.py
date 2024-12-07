import json

from Hanlders.Handler import Handler, filenamejson


class JsonHandler(Handler):

    # Функция сохранения информации в json
    def save_to(self, data) -> None:
        with open(filenamejson, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            print("Данные успешно сохранены")
        pass

    # Функция для чтения информации из json

    def load_from(self) -> dict:
        try:
            with open(filenamejson, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"movies": [], "serials": []}

    def print_data(self, data) -> None:
        print("\nДанные из JSON:")

        print("\nФильмы:")
        for movie in data['movies']:
            print(f"Название: {movie['title']}, Длительность: {movie['duration']} мин, \
Рейтинг: {movie['rating']}")

        print("\nСериалы:")
        for series in data['serials']:
            print(f"Название: {series['title']}, Эпизодов: {series['num_of_ep']}, \
Рейтинг: {series['rating']}")

        pass

    # Функция записи информации в массив
    def data_to_dict(self, data) -> dict:
        while True:
            choice = int(input("Что записать в массив?\n1-Фильмы\n2-Сериалы\n"))
            if choice == 1:
                res = []
                for movie in data['movies']:
                    res.append(movie)
                print("Данные успешно сохранены в массив \n")
                return res
            elif choice == 2:
                res = []
                for movie in data['serials']:
                    res.append(movie)
                print("Данные успешно сохранены в массив \n")
                return res
            else:
                print("Неверный выбор")
