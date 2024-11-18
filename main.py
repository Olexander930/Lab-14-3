import csv
import matplotlib.pyplot as plt

# Функція для зчитування даних з CSV-файлу
def read_csv(file_path):
    years = []
    ukraine_data = []
    usa_data = []

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                years.append(int(row["Year"]))
                ukraine_data.append(int(row["Ukraine"]))
                usa_data.append(int(row["USA"]))
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")

    return years, ukraine_data, usa_data

# Функція для побудови лінійного графіка
def plot_line_graph(years, ukraine_data, usa_data):
    plt.figure(figsize=(10, 6))
    plt.plot(years, ukraine_data, marker='o', label='Україна')
    plt.plot(years, usa_data, marker='s', label='США')
    plt.title("Динаміка показника світового розвитку: Україна та США")
    plt.xlabel("Рік")
    plt.ylabel("Значення")
    plt.legend()
    plt.grid(True)
    plt.show()

# Функція для побудови стовпчастої діаграми
def plot_bar_chart(years, data, country_name):
    plt.figure(figsize=(10, 6))
    plt.bar(years, data, color='skyblue')
    plt.title(f"Динаміка показника світового розвитку для {country_name}")
    plt.xlabel("Рік")
    plt.ylabel("Значення")
    plt.show()

# Основна програма
if __name__ == "__main__":
    file_path = "Data.csv"
    years, ukraine_data, usa_data = read_csv(file_path)

    # Перевірка, чи вдалося зчитати дані
    if years and ukraine_data and usa_data:
        # Побудова лінійного графіка
        plot_line_graph(years, ukraine_data, usa_data)

        # Запит користувача для вибору країни
        country = input("Введіть країну для побудови діаграми (Україна/США): ").strip().lower()
        if country == "україна":
            plot_bar_chart(years, ukraine_data, "Україна")
        elif country == "сша":
            plot_bar_chart(years, usa_data, "США")
        else:
            print("Введено некоректну назву країни.")
    else:
        print("Не вдалося завантажити дані з файлу.")