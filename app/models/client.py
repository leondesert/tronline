from app.db import get_connection

class ClientModel:
    @staticmethod
    def get_all_clients():
        query = """
        SELECT 
            id,
            full_name,
            YEAR(birth_date) as birth_date,
            phone,
            balance
        FROM clients
        """
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    @staticmethod
    def get_client_by_id(client_id: int):
        query = """
        SELECT 
            id,
            full_name,
            YEAR(birth_date) as birth_date,
            phone,
            balance
        FROM clients
        WHERE id = %s
        """
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (client_id,))
                return cursor.fetchone()

    @staticmethod
    def add_client(client: dict):
        query = """
        INSERT INTO clients (
            full_name, phone, gender, birth_date, address, email,
            contract_number, contract_type, start_date, `group`, sport_rank, photo, comment
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        with get_connection() as conn:
            with conn.cursor() as cursor:
                # Передаем данные клиента в запрос
                cursor.execute(query, (
                    client.get('full_name'),
                    client.get('phone'),
                    client.get('gender'),
                    client.get('birth_date'),
                    client.get('address'),
                    client.get('email'),
                    client.get('contract_number'),
                    client.get('contract_type'),
                    client.get('start_date'),
                    client.get('group'),
                    client.get('sport_rank'),
                    client.get('photo_filename'),
                    client.get('comment')
                ))

                # Проверяем, был ли добавлен хотя бы один клиент
                if cursor.rowcount > 0:
                    conn.commit()
                    return {"message": "Client successfully added!"}
                else:
                    # Если строка не была добавлена, выбрасываем исключение
                    raise Exception("Failed to add client.")


    @staticmethod
    def update_client(client: dict):
        query = """
        UPDATE clients
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
                    client.get('full_name'),
                    client.get('phone'),
                    client.get('gender'),
                    client.get('birth_date'),
                    client.get('address'),
                    client.get('email'),
                    client.get('contract_number'),
                    client.get('contract_type'),
                    client.get('start_date'),
                    client.get('group'),
                    client.get('sport_rank'),
                    client.get('photo_filename'),
                    client.get('comment'),
                    client.get('id'),
                ))

                # Проверяем, был ли добавлен хотя бы один клиент
                if cursor.rowcount > 0:
                    conn.commit()
                    return {"message": "Данные клиента обновлены!"}
                else:
                    # Если строка не была добавлена, выбрасываем исключение
                    raise Exception("Ошибка при обновлении данных.")

    @staticmethod
    def delete_client(client_id: int):
        query = "DELETE FROM clients WHERE id = %s"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (client_id,))
                conn.commit()

                # Проверяем, было ли удалено хотя бы одно совпадение
                if cursor.rowcount == 0:
                    return "Клиент не найден"

                return "Клиент удален!"

    @staticmethod
    def delete_client_bulk(client_id: int):
        query = "DELETE FROM clients WHERE id = %s"
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (client_id,))
                conn.commit()

                # Проверяем, было ли удалено хотя бы одно совпадение
                if cursor.rowcount == 0:
                    return "Клиент не найден"

                return "Клиент удален!"
