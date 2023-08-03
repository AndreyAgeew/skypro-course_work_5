import csv
import json


class MixinFileOperations:
    """
        Миксин, предоставляющий методы для работы с файлами: удаление таблиц из базы данных,
        запись данных о вакансиях в JSON и CSV файлы.
    """

    def clear_tables(self) -> None:
        """
            Выполняет запрос на удаление всех таблиц базы данных.

            Примечание:
            Метод `_execute_query` должен быть реализован в классе, использующем данный миксин.
        """
        query = self.sql_queries["Удаление всех таблиц"]
        self._execute_query(query)

    def write_vacancies_to_json(self, filename) -> bool:
        """
            Записывает данные о вакансиях в JSON файл.

            Аргументы:
                filename (str): Имя файла для записи данных о вакансиях в формате JSON.

            Возвращает:
                bool: True, если запись прошла успешно, иначе False.
        """
        vacancies = self._get_all_vacancies()
        if vacancies is None or vacancies.empty:
            print("No vacancies found to write to the JSON file.")
            return False
        try:
            vacancies_list = vacancies.to_dict(orient='records')
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(vacancies_list, json_file, indent=4, ensure_ascii=False)
            print(f"Vacancies are successfully written to {filename}.")
            return True
        except Exception as e:
            print(f"Error occurred while writing vacancies to {filename}: {e}")
            return False

    def write_vacancies_to_csv(self, filename) -> bool:
        """
            Записывает данные о вакансиях в CSV файл.

            Аргументы:
                filename (str): Имя файла для записи данных о вакансиях в формате CSV.

            Возвращает:
                bool: True, если запись прошла успешно, иначе False.
        """
        vacancies = self._get_all_vacancies()
        if vacancies is None or vacancies.empty:
            print("No vacancies found to write to the CSV file.")
            return False
        try:
            vacancies.to_csv(filename, index=False, quoting=csv.QUOTE_NONNUMERIC, encoding='windows-1251')
            print(f"Vacancies are successfully written to {filename}.")
            return True
        except Exception as e:
            print(f"Error occurred while writing vacancies to {filename}: {e}")
            return False
