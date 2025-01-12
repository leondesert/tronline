from app.models.schedule import ScheduleModel

class ScheduleService:
    @staticmethod
    def get_all_classes():
        return ScheduleModel.get_all_classes()

    @staticmethod
    def get_classes_by_weekday(weekday: int):
        return ScheduleModel.get_classes_by_weekday(weekday)

    @staticmethod
    def update_class(class_data: dict):
        return ScheduleModel.update_class(class_data)

    @staticmethod
    def delete_client(class_id: int):
        return ScheduleModel.delete_class(class_id)

    @staticmethod
    def delete_selects(classes_ids):
        return ScheduleModel.delete_selects(classes_ids)