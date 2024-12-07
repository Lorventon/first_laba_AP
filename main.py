from Media_classes import Media, Serial, Film
from Hanlders.JsonHandler import JsonHandler
from Hanlders.XmlHandler import XmlHandler
from Media_classes import Media, Serial, Film

# Создаём экземпляр JsonHandler
json_handler = JsonHandler()

# Создаём экземпляр XmlHandler
xml_handler = XmlHandler()

# Загрузка данных с использованием экземпляра json_handler
data = json_handler.load_from()

while True:
    choice = int(input("Здравствуйте, выберите действие: \n1-создать фильм\n2-создать сериал\
                       \n3-Считать JSON в массив\n4-Считать XML в массив\n5-Вывести JSON\n6-Вывести XML\n"))
    if choice == 1:
        # создать фильм
        film = Film()
        film.set_title()
        film.set_duration()
        film.set_rating()

        print("Вы ввели:", str(film))

        while True:
            xoj = int(input("Сохранить в JSON или в XML?\n1-JSON\n2-XML\n"))
            if xoj == 1:
                data["movies"].append(film.to_dict())
                json_handler.save_to(data)  # Используем экземпляр для сохранения
                break
            elif xoj == 2:
                data['movies'].append(film.to_dict())
                xml_handler.save_to(data)  # Используем экземпляр для сохранения
                break
            else:
                print("Неверный выбор")
        break
    elif choice == 2:
        # создать сериал
        serial = Serial()
        serial.set_title()
        serial.set_num_of_ep()
        serial.set_rating()

        print("Вы ввели: ", str(serial))

        while True:
            xoj = int(input("Сохранить в JSON или в XML?\n1-JSON\n2-XML\n"))
            if xoj == 1:
                data["serials"].append(serial.to_dict())
                json_handler.save_to(data)  # Используем экземпляр для сохранения
                break
            elif xoj == 2:
                data['serials'].append(serial.to_dict())
                xml_handler.save_to(data)  # Используем экземпляр для сохранения
                break
            else:
                print("Неверный выбор")

        break
    elif choice == 3:
        # json в массив
        res = json_handler.data_to_dict(data)
        print(res)
        break
    elif choice == 4:
        # xml в массив
        res = xml_handler.data_to_dict(data)  # Используем экземпляр для работы с XML
        print(res)
        break
    elif choice == 5:
        # вывести json
        json_handler.print_data(data)
        break
    elif choice == 6:
        # вывести xml
        xml_handler.print_data(data)  # Используем экземпляр для вывода XML
        break
    else:
        print("Неверный выбор")
