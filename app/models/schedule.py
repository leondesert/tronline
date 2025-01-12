from app.db import get_connection

class ScheduleModel:
    @staticmethod
    def get_all_classes():
        query = """
        SELECT *
        FROM schedule
        """
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    @staticmethod
    def get_classes_by_weekday(weekday: int):
        query = """
        SELECT 
            id,
            start_time,
            end_time,
            group_id,
            coaches,
            comment
        FROM schedule
        WHERE weekday = %s
        """
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (weekday,))
                return cursor.fetchone()

    @staticmethod
    def update_class(classes: dict):
        query = """
        UPDATE schedule
        SET
            
            group_id = %s,
            start_time = %s,
            end_time = %s,
            coaches = %s,
            weekday = %s,
            comment = %s,
        WHERE id = %s
        """

        with get_connection() as conn:
            with conn.cursor() as cursor:
                # Передаем данные клиента в запрос
                cursor.execute(query, (
                    classes.get('start_time'),
                    classes.get('end_time'),
                    classes.get('coaches'),
                    classes.get('weekday'),
                    classes.get('comment'),
                    classes.get('id')  # id клиента для обновления
                ))

                conn.commit()  # Фиксация изменений

                if cursor.rowcount > 0:
                    return "Данные занятия обновлены!"
                else:
                    raise Exception("Занятие с таким ID не найдено или данные не были изменены.")

    @staticmethod
    def delete(class_id: int):
        query = "DELETE FROM schedule WHERE id = %s"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (class_id,))
                conn.commit()

                # Проверяем, было ли удалено хотя бы одно совпадение
                if cursor.rowcount == 0:
                    raise "Занятие не найдено"

                return "Занятие удалено!"

    @staticmethod
    def delete_selects(classes_ids):
        if not classes_ids:  # Проверка, что список не пустой
            raise Exception("Список ID не может быть пустым.")

        format_strings = ', '.join(['%s'] * len(classes_ids))
        query = f"DELETE FROM schedule WHERE id IN ({format_strings})"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, tuple(classes_ids))
                conn.commit()

                # Проверяем, было ли удалено хотя бы одно совпадение
                if cursor.rowcount == 0:
                    raise Exception("Не найдено записей для удаления.")

                return "Занятия удалены!"