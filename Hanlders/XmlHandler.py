import xml.etree.ElementTree as et
from Hanlders.Handler import Handler, filenamexml


class XmlHandler(Handler):

    # Функция для красивых отступов (не статический метод)
    def indent(self, elem, level=0) -> None:
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                self.indent(subelem, level + 1)
            if not subelem.tail or not subelem.tail.strip():
                subelem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    # Функция сохранения информации в xml
    def save_to(self, data) -> None:
        root = et.Element('data')

        movies = et.SubElement(root, 'movies')
        for movie in data['movies']:
            movie_element = et.SubElement(movies, 'movie')
            for key, value in movie.items():
                child = et.SubElement(movie_element, key)
                child.text = str(value)

        tvseries = et.SubElement(root, 'serials')
        for series in data['serials']:
            series_element = et.SubElement(tvseries, 'serial')
            for key, value in series.items():
                child = et.SubElement(series_element, key)
                child.text = str(value)

        # Добавляем отступы для красивого форматирования
        self.indent(root)

        # Создаем дерево XML и записываем его в файл
        tree = et.ElementTree(root)
        tree.write(filenamexml, encoding='utf-8', xml_declaration=True)

        print(f"Данные успешно сохранены в файл '{filenamexml}'")

    # Функция чтения информации из xml
    def load_from(self) -> dict:
        try:
            tree = et.parse(filenamexml)
            root = tree.getroot()
        except FileExistsError:
            return {"movies": [], "serials": []}

        data = {"movies": [], "serials": []}

        for movie in root.find("movies"):
            movie_data = {}
            for child in movie:
                movie_data[child.tag] = child.text
            data["movies"].append(movie_data)

        for serial in root.find("serials"):
            serial_data = {}
            for child in serial:
                serial_data[child.tag] = child.text
            data["serials"].append(serial_data)

        return data

    def print_data(self, data):
        print("\nДанные из XML:")

        print("\nФильмы:")
        for movie in data['movies']:
            print(f"Название: {movie['title']}, Длительность: {movie['duration']} мин, Рейтинг: {movie['rating']}")

        print("\nСериалы:")
        for series in data['serials']:
            print(f"Название: {series['title']}, Эпизодов: {series['num_of_ep']}, Рейтинг: {series['rating']}")

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
