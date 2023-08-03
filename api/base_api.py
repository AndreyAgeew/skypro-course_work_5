from abc import ABC, abstractmethod


class BaseAPI(ABC):
    def __init__(self, base_url: str, number_of_vacancies: int = 100) -> None:
        """
        Инициализация базового класса для API.

        :param base_url: Базовый URL для API.
        :param number_of_vacancies: Количество вакансий для получения.
        """
        self._base_url = base_url
        self._number_of_vacancies = number_of_vacancies

    @abstractmethod
    def _search_vacancies(self, employer_id) -> list:
        """
        Поиск вакансий на HeadHunter API.

        :param employer_id: Id компании для поиска.
        :return: Список найденных вакансий компании.
        """
        pass
