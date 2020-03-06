class TimeLog:
    __task_id: int = 0
    __start_time = None
    __end_time = None
    __submitted: bool = None

    def __init__(self, task_id, start_time, end_time, submitted):
        self.__task_id = task_id
        self.__start_time = start_time
        self.__end_time = end_time
        self.__submitted = submitted


    def get_task_id(self):
        return self.__task_id

    def set_task_id(self, task_id):
        self.__task_id = task_id

    def get_start_time(self):
        return self.__start_time

    def set_start_time(self, start_time):
        self.__start_time = start_time

    def get_end_time(self):
        return self.__end_time

    def set_end_time(self, end_time):
        self.__end_time = end_time

    def get_submitted(self):
        return self.__submitted

    def set_submitted(self, submitted):
        self.__submitted = submitted
