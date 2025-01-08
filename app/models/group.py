from app.db import get_connection

class GroupModel:
    @staticmethod
    def get_all_groups():
        query = """
        SELECT *
        FROM groups
        """
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    @staticmethod
    def get_group_by_id(group_id: int):
        query = """
        SELECT 
            id,
            full_name,
            YEAR(birth_date) as birth_date,
            phone,
            balance
        FROM groups
        WHERE id = %s
        """
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (group_id,))
                return cursor.fetchone()

    @staticmethod
    def add_group(group: dict):

        query = """
        INSERT INTO groups (
            name, sport_type, coaches, start_date, position, schedule
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """

        with get_connection() as conn:
            with conn.cursor() as cursor:
                # Передаем данные клиента в запрос
                cursor.execute(query, (
                    group.get('name'),
                    group.get('sport_type'),
                    group.get('coaches'),
                    group.get('start_date'),
                    group.get('position'),
                    group.get('schedule')
                ))

                # Проверяем, был ли добавлен хотя бы один клиент
                if cursor.rowcount > 0:
                    conn.commit()
                    return {"message": "group successfully added!"}
                else:
                    # Если строка не была добавлена, выбрасываем исключение
                    raise Exception("Failed to add group.")


    @staticmethod
    def update_group(group: dict):
        query = """
        UPDATE groups
        SET
            full_name = %s,
            phone = %s,
            gender = %s,
            birth_date = %s,
            address = %s,
            email = %s,
            contract_number = %s,
            contract_type = %s,
            start_date = %s,
            `group` = %s,
            sport_rank = %s,
            photo = %s,
            comment = %s
        WHERE id = %s
        """

        with get_connection() as conn:
            with conn.cursor() as cursor:
                # Передаем данные клиента в запрос
                cursor.execute(query, (
                    group.get('full_name'),
                    group.get('phone'),
                    group.get('gender'),
                    group.get('birth_date'),
                    group.get('address'),
                    group.get('email'),
                    group.get('contract_number'),
                    group.get('contract_type'),
                    group.get('start_date'),
                    group.get('group'),
                    group.get('sport_rank'),
                    group.get('photo_filename'),
                    group.get('comment'),
                    group.get('id')  # id клиента для обновления
                ))

                conn.commit()  # Фиксация изменений

                if cursor.rowcount > 0:
                    return "Данные клиента обновлены!"
                else:
                    raise Exception("Клиент с таким ID не найден или данные не были изменены.")

    @staticmethod
    def delete(group_id: int):
        query = "DELETE FROM groups WHERE id = %s"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (group_id,))
                conn.commit()

                # Проверяем, было ли удалено хотя бы одно совпадение
                if cursor.rowcount == 0:
                    raise "Группа не найдена"

                return "Группа удалена!"

    @staticmethod
    def delete_selects(group_ids):
        if not group_ids:  # Проверка, что список не пустой
            raise Exception("Список ID не может быть пустым.")

        format_strings = ', '.join(['%s'] * len(group_ids))
        query = f"DELETE FROM groups WHERE id IN ({format_strings})"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, tuple(group_ids))
                conn.commit()

                # Проверяем, было ли удалено хотя бы одно совпадение
                if cursor.rowcount == 0:
                    raise Exception("Не найдено записей для удаления.")

                return "Группы удалены!"
