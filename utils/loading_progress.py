import sys


def show_loading_progress(completed_items, total_items) -> None:
    """
        Выводит индикатор прогресса загрузки данных на консоль.

        Аргументы:
            completed_items (int): Количество завершенных элементов.
            total_items (int): Общее количество элементов.

        Примечание:
            Для корректной работы функции, требуется импорт модуля `sys`.
    """
    animation_chars = "|/-\\"
    progress = (completed_items / total_items) * 100
    sys.stdout.write(
        f"\rЗагрузка данных... [{animation_chars[completed_items % len(animation_chars)]}] {int(progress)}%")
    sys.stdout.flush()
