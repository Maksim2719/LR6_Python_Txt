import json

students_data = {
    "Гарькавий": ["Назар", "Русланович", 2004],
    "Дяченко": ["Олексій", "Олегович", 2003],
    "Косянчук": ["Сергій", "Владиславович", 2005],
    "Максименко": ["Сергій", "Сергійович", 2004],
    "Малиновський": ["Борис", "Сергійович", 2003],
    "Морщ": ["Владислав", "Олександрович", 2005],
    "Морщ_2": ["Дмитрій", "Олександрович", 2004],
    "Сергієнко": ["Дмитро", "Андрійович", 2003],
    "Терновий": ["Дмитро", "Станіславович", 2005],
    "Чупилка": ["Максим", "Вікторович", 2004]
}

filename = "students.json"


def write_json_file():
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(students_data, file, ensure_ascii=False, indent=4)

    print(f"Файл {filename} успішно записано.")


def read_json_file():
    with open(filename, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)

    print("\nДАНІ, ПРОЧИТАНІ З JSON-ФАЙЛУ:\n")
    for surname, info in loaded_data.items():
        name, patronymic, birth_year = info
        if surname == "Морщ_2":
            print(f"Морщ {name} {patronymic}, {birth_year} р.н.")
        else:
            print(f"{surname} {name} {patronymic}, {birth_year} р.н.")


def main():
    write_json_file()
    read_json_file()


if __name__ == "__main__":
    main()