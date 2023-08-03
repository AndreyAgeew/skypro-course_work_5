from database.mixin_db_connection import MixinDBConnection
from database.mixin_table_creation import MixinTableCreation
from database.mixin_vacancy_operations import MixinVacancyOperations
from database.mixin_file_operations import MixinFileOperations
from utils.read_sql_queries import read_sql
import pandas as pd


class DBManager(MixinDBConnection, MixinTableCreation, MixinVacancyOperations, MixinFileOperations):
    """
        Класс DBManager, который представляет собой менеджер базы данных.

        Он наследуется от следующих миксинов:
        - MixinDBConnection: предоставляет методы для подключения и отключения от базы данных.
        - MixinTableCreation: предоставляет методы для создания таблиц в базе данных.
        - MixinVacancyOperations: предоставляет методы для работы с вакансиями.
        - MixinFileOperations: предоставляет методы для работы с файлами.

        Атрибуты:
            connection: Атрибут для хранения соединения с базой данных
            sql_queries: Атрибут для хранения SQL-запросов, считанных из файла

    """
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    def __init__(self) -> None:
        """
            Конструктор класса DBManager.

            Инициализирует атрибуты:
            - connection: устанавливается значение None.
            - sql_queries: считывает SQL-запросы из файла и сохраняет их в атрибуте.
        """
        self.connection = None
        self.sql_queries = read_sql()

    def _execute_query(self, query, params=None):
        """
               Метод для выполнения SQL-запросов к базе данных.

               Аргументы:
                   query (str): SQL-запрос, который требуется выполнить.
                   params (tuple): Параметры для SQL-запроса (по умолчанию None).
        """

        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute(query, params)
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)

    def _description_query(self, query, params=None, fetch=False):
        """
               Метод для выполнения описательных SQL-запросов к базе данных.

               Аргументы:
                   query (str): SQL-запрос, который требуется выполнить.
                   params (tuple): Параметры для SQL-запроса (по умолчанию None).
                   fetch (bool): Указывает, нужно ли извлекать результаты запроса (по умолчанию False).

               Возвращает:
                   pd.DataFrame: Если параметр fetch=True, возвращает результаты запроса в виде pandas DataFrame.
                   None: Если произошла ошибка при выполнении запроса или fetch=False.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                if fetch:
                    result = cursor.fetchall()
                    columns = [desc[0] for desc in cursor.description]
                    return pd.DataFrame(result, columns=columns)
        except Exception as e:
            print("Error executing query:", e)
            return None
