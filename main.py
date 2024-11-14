import json
import xml.etree.ElementTree as ET


def xml_to_json(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        json_data = {"people": []}

        for person in root.findall('person'):
            name = person.find('name').text
            age = person.find('age').text
            profession = person.find('profession').text
            city = person.find('city').text

            person_data = {
                "name": name,
                "age": age,
                "profession": profession,
                "city": city
            }
            json_data["people"].append(person_data)

        return json_data
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
        return None
    except ET.ParseError:
        print("Ошибка: Невозможно разобрать XML файл.")
        return None


def save_json_to_file(json_data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        print(f"Файл '{filename}' успешно сохранён.")
    except IOError:
        print("Ошибка: Не удалось сохранить файл.")


def main():
    xml_filename = input("Введите имя XML файла (например, 'test.xml'), или введите 'exit' для выхода: ")

    if xml_filename.lower() == 'exit':
        return

    json_data = xml_to_json(xml_filename)

    if json_data is not None:
        json_filename = xml_filename.replace('.xml', '.json')
        save_json_to_file(json_data, json_filename)
        print("Преобразование файла прошло успешно.")
    else:
        print("Преобразование файла не удалось.")

main()