import zeep
from pyrussianpost.utils import response_handler


class Tracking:
    def __init__(self, login, password):
        """
        Инициализация объекта Tracking.

        Parameters:
        - login (str): Логин для доступа к API Сервиса отслеживания.
        - password (str): Пароль для доступа к API Сервиса отслеживания.
        """
        self.login = login
        self.password = password
        self.wsdl_url = "https://tracking.russianpost.ru/rtm34?wsdl"
        self.client = zeep.Client(self.wsdl_url)
        self.ns0 = '{http://russianpost.org/operationhistory/data}'
        self.ns_data = '{http://russianpost.org/operationhistory/data}'

    def get_operation_history(self, barcode, message_type=0, language="RUS"):
        """
        Получает историю операций над почтовым отправлением.

        Parameters:
        - barcode (str): Идентификатор регистрируемого почтового отправления.
        - message_type (int): Тип сообщения. 0 - история операций для отправления.
        - language (str): Язык, на котором возвращаются названия операций/атрибутов и сообщения об ошибках.

        Returns:
        - response: Ответ от сервиса отслеживания с информацией об операциях.
        """
        operation_history_request = {
            'OperationHistoryRequest': {
                'Barcode': barcode,
                'MessageType': message_type,
                'Language': language,
            },
            'AuthorizationHeader': {
                'login': self.login,
                'password': self.password,
            }
        }

        response = self.client.service.getOperationHistory(**operation_history_request)

        return response

    def get_waypoints(self, barcode):
        tracking_data = self.get_operation_history(barcode=barcode)
        waypoints = response_handler.waypoints_handler(tracking_data)
        return waypoints
