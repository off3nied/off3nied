import os
from datetime import datetime

def update_readme_time(readme_file):
    # Открываем файл README.md для чтения
    with open(readme_file, 'r') as file:
        lines = file.readlines()

    # Ищем строку с временем обновления (если она есть)
    for i, line in enumerate(lines):
        if line.startswith("Последнее обновление:"):
            # Обновляем строку с текущим временем
            lines[i] = "Последнее обновление: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            break
    else:
        # Если строка не найдена, добавляем новую строку с текущим временем
        lines.append("Последнее обновление: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

    # Записываем обновленные строки обратно в файл README.md
    with open(readme_file, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    # Имя файла README.md
    readme_file = "README.md"
    
    # Проверяем существование файла README.md
    if os.path.exists(readme_file):
        update_readme_time(readme_file)
        print("Время в файле README.md обновлено.")
    else:
        print("Файл README.md не найден.")
