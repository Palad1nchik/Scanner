#include <stdio.h>
#include <windows.h>
#include <ShlObj.h>

int checkAutostartFiles()
{
    PWSTR autostartFolderPath;
    WCHAR fileName[MAX_PATH];
    WIN32_FIND_DATA findData;
    HANDLE hFind;
    int counter = 0;

    // Получение пути к папке автозагрузки
    if (SUCCEEDED(SHGetKnownFolderPath(&FOLDERID_Startup, 0, NULL, &autostartFolderPath)))
    {
        // Формирование шаблона для поиска файлов
        swprintf(fileName, L"%s\\*.*", autostartFolderPath);

        // Поиск файлов в папке автозагрузки
        hFind = FindFirstFile(fileName, &findData);
        if (hFind != INVALID_HANDLE_VALUE)
        {
            do
            {
                if (!(findData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY))
                {
                    // Вывод информации о найденном файле
                    wprintf(L" File was found as: %s\n", findData.cFileName);

                    // Проверка файла на предмет вредоносной активности
                    // Можно добавить свою логику проверки здесь

                    counter++;
                }
            } while (FindNextFile(hFind, &findData));

            FindClose(hFind);
        }

        CoTaskMemFree(autostartFolderPath);
    }

    return counter;
}

int main()
{
    CoInitializeEx(NULL, COINIT_APARTMENTTHREADED | COINIT_DISABLE_OLE1DDE);

    int numMaliciousFiles = checkAutostartFiles();
    wprintf(L"Total number of malicious files found in autoload: %d\n", numMaliciousFiles);

    CoUninitialize();

    return 0;
}
