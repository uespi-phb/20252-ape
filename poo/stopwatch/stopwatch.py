
from datetime import datetime


class Stopwatch:
    
    def __init__(self):
        self.__start_time = None
        self.__end_time = None
        
    
    def start(self):
        self.__start_time = datetime.now()

        
    def stop(self):
        if self.__start_time is None:
            raise Exception('Cannot stop without start the stopwatch')
        self.__end_time = datetime.now()

        
    def enlapsed(self):
        if self.__start_time is None:
            raise Exception('Cannot calculate enlapsed time without start the stopwatch')

        if self.__end_time is None:
            end_time = datetime.now()
        else:
            end_time = self.__end_time

        delta = end_time - self.__start_time
        return delta.total_seconds()
