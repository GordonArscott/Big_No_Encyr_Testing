import os
from test_eval import Question


class Question1(Question):

    def __init__(self):
        self.name = 'fix_is_store_open'
        self.total_points = 10
        self.case_points = self.total_points / len(self.get_tests())
        self.exempted = [4]

    def solution(self, current_time, opening_times):
        current_time = current_time.replace(':', '')
        opening_time_list = opening_times.replace(':', '').split('-')
        start = opening_time_list[0]
        end = opening_time_list[1]
        # you can also explictly convert to int, strings work though:
        if current_time > '2359' or start > '2359' or end > '2359':
            return 'invalid time'
        else:
            return start <= current_time <= end

    def get_tests(self):
        return [
            ("00:00", "01:00-23:59"),
            ("07:00", "00:00-23:59"),
            ("06:34", "06:01-06:59"),
            ("01:00", "01:00-01:00"),
            ("25:00", "23:00-26:00")
        ]


