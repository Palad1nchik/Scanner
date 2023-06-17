'''
import os
import winreg

def check_autorun_entries():
    # ��������� ���� �������, ���������� ���������� �� ������������
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)

    # �������� ���������� ��������� (�������) � �����
    num_entries = winreg.QueryInfoKey(key)[0]

    # ���������� ��� ������ � ����� ������������
    for i in range(num_entries):
        # �������� ��� �������� (������)
        entry_name = winreg.EnumValue(key, i)[0]

        # �������� ���� � �����, ���������� � ������������
        file_path = os.path.expandvars(entry_name)

        # ���������, ���������� �� ���� �� ���������� ����
        if os.path.isfile(file_path):
            # � ������ ����� ����� �������� �������������� �������� �� ������� ����������� ���������� �����
            print("���� � ������������:", file_path)
        else:
            print("���������������� ���� � ����� � ������������:", file_path)

    # ��������� ���� �������
    winreg.CloseKey(key)

# �������� ������� ��� �������� ������� ������������
check_autorun_entries()
'''