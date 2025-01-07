from app.models.client import ClientModel

class ClientService:
    @staticmethod
    def get_all_clients():
        return ClientModel.get_all_clients()

    @staticmethod
    def create_client(client: dict):
        return ClientModel.add_client(client)

    @staticmethod
    def update_client(client: dict):
        return ClientModel.update_client(client)

    @staticmethod
    def delete_client(client_id: int):
        return ClientModel.delete_client(client_id)