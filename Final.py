'''
import os
import winreg

def check_autorun_entries():
    # Открываем ключ реестра, содержащий информацию об автозагрузке
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)

    # Получаем количество подключей (записей) в ключе
    num_entries = winreg.QueryInfoKey(key)[0]

    # Перебираем все записи в ключе автозагрузки
    for i in range(num_entries):
        # Получаем имя подключа (записи)
        entry_name = winreg.EnumValue(key, i)[0]

        # Получаем путь к файлу, указанному в автозагрузке
        file_path = os.path.expandvars(entry_name)

        # Проверяем, существует ли файл по указанному пути
        if os.path.isfile(file_path):
            # В данном месте можно провести дополнительные проверки на предмет вредоносной активности файла
            print("Файл в автозагрузке:", file_path)
        else:
            print("Недействительный путь к файлу в автозагрузке:", file_path)

    # Закрываем ключ реестра
    winreg.CloseKey(key)

# Вызываем функцию для проверки записей автозагрузки
check_autorun_entries()
'''