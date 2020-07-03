from jira_time_assist.entities.time_log import TimeLog


class Task:
    __ticket_number: str = ""
    __description: str = ""
    __time_logs: [TimeLog] = []
    __total_time_logged: int = 0
    __removed: bool = 0

    def __init__(self, ticket_number, description, time_logs, removed):
        self.__ticket_number = ticket_number
        self.__description = description
        self.__time_logs = time_logs
        self.__removed = removed

    def get_ticket_number(self):
        return self.__ticket_number

    def set_ticket_number(self, ticket_number):
        self.__ticket_number = ticket_number

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_time_logs(self):
        return self.__time_logs

    def set_time_logs(self, time_logs):
        self.__time_logs = time_logs

    def get_total_time_logged(self):
        total: int = 0

        if self.__time_logs:
            for log in self.__time_logs:
                total += log.get_end_time() - log.get_start_time()

        return total
