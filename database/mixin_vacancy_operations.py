class MixinVacancyOperations:
    """
        Миксин, предоставляющий методы для работы с вакансиями:
        - вставка данных о вакансиях;
        - получение списка вакансий;
        - получение списка компаний и количества вакансий у каждой компании;
        - получение топ 300 вакансий;
        - получение средней зарплаты по вакансиям;
        - получение списка вакансий с зарплатой выше средней по всем вакансиям;
        - получение списка вакансий, содержащих заданный ключевой слово в названии.

        Примечание:
        Методы `_execute_query` и `_description_query` должны быть реализованы в классе, использующем данный миксин,
        для выполнения SQL-запросов к базе данных.
    """

    def insert_vacancy_to_all(self, id, company_name, vacancy_name, vacancy_salary_from, vacancy_salary_to,
                              vacancy_currency,
                              vacancy_url):
        self._create_all_vacancies_table()  # Создаем таблицу all_vacancies, если её нет
        query = self.sql_queries["Запрос для добавления вакансии в общую таблицу"]
        params = (id, company_name, vacancy_name, vacancy_salary_from, vacancy_salary_to, vacancy_currency, vacancy_url)
        self._execute_query(query, params)

    def insert_vacancy_company(self, vacancy_id, company_name, vacancy_name, vacancy_salary_from, vacancy_salary_to,
                               vacancy_currency,
                               vacancy_url):
        self._create_company_table(company_name)
        query = self.sql_queries["Запрос для добавления вакансии в таблицу компании"].replace("{company_name}",
                                                                                              company_name)
        params = (vacancy_id, vacancy_name, vacancy_salary_from, vacancy_salary_to, vacancy_currency, vacancy_url)
        self._execute_query(query, params)

    def get_companies_and_vacancies_count(self):
        query = self.sql_queries["получает список всех компаний и количество вакансий у каждой компании"]
        return self._description_query(query, fetch=True)

    def _get_all_vacancies(self):
        query = self.sql_queries[
            "получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"]
        return self._description_query(query, fetch=True)

    def get_top_vacancies(self):
        query = self.sql_queries[
            "получает список 300 топ вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"]
        return self._description_query(query, fetch=True)

    def get_avg_salary(self):
        query = self.sql_queries["получает среднюю зарплату по вакансиям"]
        result = self._description_query(query, fetch=True)
        return f"от {result.iloc[0]['avg_salary_from']} до {result.iloc[0]['avg_salary_to']}" if not result.empty else None

    def get_vacancies_with_higher_salary(self):
        avg_salary = self.get_avg_salary()
        if avg_salary is not None:
            query = self.sql_queries["получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"]
            return self._description_query(query, fetch=True)
        return None

    def get_vacancies_with_keyword(self, keyword):
        query = self.sql_queries[
            "получает список всех вакансий, в названии которых содержатся переданные в метод слова"]
        params = ('%' + keyword + '%',)
        return self._description_query(query, params=params, fetch=True)
