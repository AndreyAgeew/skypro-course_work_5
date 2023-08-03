import psycopg2

from config import DB_CONNECTION_STRING


class MixinDBConnection:
    """
        Миксин, предоставляющий методы для подключения и отключения от базы данных PostgreSQL.
    """

    def connect(self) -> None:
        """
            Подключается к базе данных PostgreSQL с использованием значения `DB_CONNECTION_STRING`.

            В случае успешного подключения, устанавливает атрибут `connection` для экземпляра класса.
        """
        try:
            self.connection = psycopg2.connect(DB_CONNECTION_STRING)
            print("Connected to the database.")
        except Exception as e:
            print("Error connecting to the database:", e)

    def disconnect(self) -> None:
        """
            Отключается от базы данных PostgreSQL, если соединение установлено.

            В случае успешного отключения, закрывает соединение и выводит сообщение об успешном отключении.
        """
        if self.connection:
            self.connection.close()
            print("Disconnected from the database.")
