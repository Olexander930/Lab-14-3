import re
import json
import matplotlib.pyplot as plt

# Ініціалізація початкових даних
file = "data.json"
initial_students = {
    "Vitaly_Prikhodko": 203,
    "Dmytro_Kropyvnytskyi": 196,
    "Mikhail_Romanenko": 193,
    "Maxim_Derizemlya": 188,
    "Victoria_Zhuk": 182,
    "Andrey_Kuryanov": 177,
    "Oksana_Dubovets": 175,
    "Nikita_Stroganov": 173,
    "Karina_Nikolaenko": 169,
    "Eugenia_Dron": 167
}

# Ініціалізація даних
def initialize_data():
    try:
        with open(file, "x") as f:
            json.dump(initial_students, f, indent=4, ensure_ascii=False)
            print("Файл з початковими даними створено.")
    except FileExistsError:
        pass  

# Завантаження даних
def load_data():
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не знайдено. Створюю новий.")
        return {}

# Функція для визначення статі за іменем
def is_boy(name):
    boy_names = ["Vitaly", "Dmytro", "Mikhail", "Maxim", "Andrey", "Nikita"]
    return any(re.match(boy, name) for boy in boy_names)

def is_girl(name):
    girl_names = ["Victoria", "Oksana", "Karina", "Eugenia"]
    return any(re.match(girl, name) for girl in girl_names)

# Розрахунок сумарного зросту
def calculate_heights_by_gender(data):
    boys_height = sum(height for name, height in data.items() if is_boy(name))
    girls_height = sum(height for name, height in data.items() if is_girl(name))
    return boys_height, girls_height

# Побудова кругової діаграми
def plot_pie_chart(boys_total, girls_total):
    labels = ['Хлопці', 'Дівчата']
    sizes = [boys_total, girls_total]
    colors = ['skyblue', 'pink']
    explode = (0.1, 0)  # Відокремлення сектора хлопців

    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors
    )
    plt.title("Розподіл зросту між хлопцями і дівчатами")
    plt.axis('equal')  # Забезпечення круглої форми
    plt.show()

# Основна функція
if __name__ == "__main__":
    initialize_data()
    data = load_data()

    if data:
        boys_total, girls_total = calculate_heights_by_gender(data)

        print(f"Загальний зріст хлопців: {boys_total} см")
        print(f"Загальний зріст дівчат: {girls_total} см")

        if girls_total > boys_total:
            print("Сумарний зріст дівчат перевищує зріст хлопців.")
        else:
            print("Сумарний зріст хлопців перевищує зріст дівчат.")

        # Побудова кругової діаграми
        plot_pie_chart(boys_total, girls_total)
    else:
        print("Дані відсутні.")