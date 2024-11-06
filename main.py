import csv

INPUT_FILE = 'Data.csv'
OUTPUT_FILE = 'result.csv'

def read_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = [row for row in reader if row]
            return headers, data
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return None, []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None, []

def display_data(headers, data):
    if headers:
        print("Заголовки стовпців:", headers)
    for row in data:
        print(row)

def find_min(data):
    min_value = float('inf')
    min_year = None
    for row in data:
        year = None
        if len(row) > 1:
            year = row[2]  
        for value in row[1:]:
            try:
                num_value = float(value)
                if num_value < min_value and not (1991 <= num_value <= 2019):  
                    min_value = num_value
                    min_year = year
            except ValueError:
                continue
    return (min_value, min_year) if min_value != float('inf') else (None, None)

def find_max(data):
    max_value = float('-inf')
    max_year = None
    for row in data:
        year = None
        if len(row) > 1:
            year = row[2]  
        for value in row[1:]:
            try:
                num_value = float(value)
                if num_value > max_value:
                    max_value = num_value
                    max_year = year
            except ValueError:
                continue
    return (max_value, max_year) if max_value != float('-inf') else (None, None)

def write_results(output_file, min_value, min_year, max_value, max_year):
    try:
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Statistic', 'Value', 'Year'])
            writer.writerow(['Minimum', min_value, min_year])
            writer.writerow(['Maximum', max_value, max_year])
        print(f"Результати збережено у файл '{output_file}'.")
    except Exception as e:
        print(f"Помилка при запису у файл: {e}")

# Основна програма
headers, data = read_csv(INPUT_FILE)

if headers is not None and data:
    display_data(headers, data)
    min_value, min_year = find_min(data)
    max_value, max_year = find_max(data)
    if min_value is not None and max_value is not None:
        print(f'Найменше значення населення України: {min_value} в  {min_year} році')
        print(f'Найбільше значення населення Украхни : {max_value} в {max_year} році')
        write_results(OUTPUT_FILE, min_value, min_year, max_value, max_year)
    else:
        print("Не вдалося знайти числові значення в файлі.")
else:
    print("Файл порожній або не містить даних.")