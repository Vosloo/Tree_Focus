import re
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLCDNumber


class TimeArgException(Exception):
    pass


class TreeTimer(QLCDNumber):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.setFixedSize(160, 80)
        self.time_ms = 0

    def initialize(self, time):
        self.time = time.rstrip().lower()

        self.timer = QTimer(self.parent)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timer_timeout)

        self.custom_text = 'custom: '
        self.possible_times = ['m', 'min', 'h']

        self.parse_time()
        self.get_set_time()
        self.start_counting()

    def parse_time(self):  # TODO: Add multiple times (1h and 20 min)
        """Parsing time selected by user.
            In custom time there are three options:
            seconds: s, sec; minutes: m, min; hours: h"""

        if self.custom_text in self.time:
            time_splitted = [text for text in self.time.split(' ')[1:]
                             if text != '']
        else:
            time_splitted = [text for text in self.time.split(' ')
                             if text != '']

        if len(time_splitted) < 1 or len(time_splitted) > 2:
            # Not enough or too much args
            raise TimeArgException
        else:
            if len(time_splitted) == 1:
                repeating_nums = re.findall(r"([0-9]+)", *time_splitted)
                if len(repeating_nums) == 0 or len(repeating_nums) > 1:
                    raise TimeArgException

                repeating_text = re.findall(r"([a-z]+)", *time_splitted)
                if len(repeating_text) == 0 or len(repeating_text) > 1:
                    raise TimeArgException

                good_time = all([time in self.possible_times for
                                time in repeating_text])

                if not good_time:
                    raise TimeArgException
                else:
                    num = int(*repeating_nums)
                    [time_unit] = repeating_text
            else:
                num, time_unit = time_splitted

                try:
                    num = int(num)
                except ValueError:
                    raise TimeArgException

                if time_unit not in self.possible_times:
                    raise TimeArgException

        self.time = [num, time_unit]
        print(self.time)

    def get_set_time(self):
        self.set_time = self.get_milis()

    def get_milis(self):
        """Returns time in miliseconds"""
        num, unit = self.time

        if unit in ['m', 'min']:
            multiplier = 60 * 1000
        elif unit in ['h']:
            multiplier = 60 * 60 * 1000

        tmp_time = num * multiplier
        return tmp_time

    def start_counting(self):
        self.timer.start(2000)

        human_time = self.get_display_time()

        self.setDigitCount(8)
        self.display(human_time)

    def get_display_time(self):  # TODO: implement human getting readable time
        print("Human readable time")

    def timer_timeout(self):
        self.time_ms += 1
        self.start_counting()
