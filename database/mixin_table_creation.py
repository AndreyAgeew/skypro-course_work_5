class MixinTableCreation:
    """
        Миксин, предоставляющий методы для создания таблиц в базе данных.

        Примечание:
        Метод `_execute_query` должен быть реализован в классе,
        использующем данный миксин, для выполнения SQL-запросов к базе данных.
    """

    def _create_company_table(self, company_name) -> None:
        """
            Создает таблицу вакансий компании с указанным именем.

            Аргументы:
                company_name (str): Имя компании, используется для формирования имени таблицы.
        """
        query = self.sql_queries["Создание таблицы вакансий компании с внешним ключом"].replace("{company_name}",
                                                                                                company_name)
        self._execute_query(query)

    def _create_all_vacancies_table(self) -> None:
        """Создает таблицу всех вакансий."""
        query = self.sql_queries["Создание таблицы всех вакансий"]
        self._execute_query(query)
