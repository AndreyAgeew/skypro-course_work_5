class MixinMenuAPP:
    """
        Миксин, предоставляющий главное меню для взаимодействия с функциональностью, предоставленной в других классах и миксинах.

        Примечание:
        Методы, которые используются в меню (например, _get_companies_and_vacancies_count, _get_top_vacancies и т.д.),
        должны быть определены в классе, использующем этот миксин.
    """

    @classmethod
    def main_menu(cls):
        """
            Основное меню приложения.

            Бесконечный цикл, который выводит список доступных опций
            для взаимодействия с функциональностью и обрабатывает выбор пользователя.
        """
        while True:
            print("\nДля получения списка всех компаний и количество вакансий у каждой компании (1)")
            print("Для получения списка топ 300 вакансий с указанием названия компании,"
                  " названия вакансии и зарплаты и ссылки на вакансию (2)")
            print("Для получения средней зарплаты по вакансиям (3)")
            print("Для получения списка всех вакансий, у которых зарплата выше средней по всем вакансиям (4)")
            print("Для получения списка всех вакансий, в названии которых содержатся слово (5)")
            print("Для загрузки всех вакансий в файл csv (6)")
            print("Для загрузки всех вакансий в файл json (7)")
            print("Для выхода (0)")
            user_input = int(input())
            if user_input == 1:
                cls._get_companies_and_vacancies_count()
            elif user_input == 2:
                cls._get_top_vacancies()
            elif user_input == 3:
                print("Средня зарплата в рублях:", end=" ")
                cls._get_avg_salary()
            elif user_input == 4:
                cls._get_vacancies_with_higher_salary()
            elif user_input == 5:
                keyword = str(input("Введите поисковое слово: "))
                cls._get_vacancies_with_keyword(keyword)
            elif user_input == 6:
                cls.db_manager.write_vacancies_to_csv('vacancies.csv')
            elif user_input == 7:
                cls.db_manager.write_vacancies_to_json('vacancies.json')
            elif user_input == 0:
                break
            else:
                print("Введено неверное значение!")
