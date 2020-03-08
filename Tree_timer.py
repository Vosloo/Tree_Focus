import re
from time import monotonic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLCDNumber


class TimeArgException(Exception):
    pass


class TreeTimer(QLCDNumber):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.set_LCDNumber()

    def set_LCDNumber(self):
        """Sets initial parameters for the class"""
        self.hide()

        self.setStyleSheet(
            "background-color:rgb(180,213,78);"
            "border-style: inset;"
            "border-width: 1px;"
            "border-radius: 6px;"
            "border-color: black;"
        )
        self.setFixedSize(160, 80)

        self.setDigitCount(8)
        self.display("00:00:00")

    def initialize(self, selected_time):
        """Initlialize parsing and timer"""

        self.selected_time = selected_time.rstrip().lower()

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.start_time = None
        self.timer.timeout.connect(self.timer_timeout)

        self.custom_text = 'custom: '
        self.possible_times = ['m', 'min', 'h']

        self.parse_time()
        self.show()  # If parsing succeded shows LCDNumber
        self.get_set_time()
        self.start_counting()

    def parse_time(self):
        """Parsing time selected by user.
            In custom time there are two options:
            minutes: m, min; hours: h"""

        if self.custom_text in self.selected_time:
            time_splitted = [text for text in self.selected_time.split(' ')[1:]
                             if text != '']
        else:
            time_splitted = [text for text in self.selected_time.split(' ')
                             if text != '']

        time_splitted = self._split_num_chars(time_splitted)

        if len(time_splitted) < 2 or len(time_splitted) > 4:
            # Not enough or too much args (max is for example: 1 h 20 min)
            raise TimeArgException
        else:
            tmp_time = []
            last_num = False
            for text in time_splitted:
                match = re.match(r"([0-9]+)", text)
                if match and last_num is False:
                    [tmp_num] = match.groups()
                    tmp_time.append(int(tmp_num))
                    last_num = True
                elif len(tmp_time) != 0 and last_num is True:
                    if text in self.possible_times:
                        tmp_time.append(text)
                        last_num = False
                    else:
                        raise TimeArgException
                else:
                    raise TimeArgException

            self.selected_time = time_splitted

    def _split_num_chars(self, time_splitted):
        """Seperates num from characters and
        makes them seperate items in list"""

        tmp_splitted = []
        for text in time_splitted:
            while True:
                match = re.match(r"([0-9]+)", text)

                if match:  # Nums at start
                    [num] = match.groups()

                    tmp_splitted.append(num)

                    try:
                        text = text[text.index(num)+len(num):]
                        if text == '':
                            raise IndexError
                    except IndexError:
                        break
                else:  # Text at start
                    match = re.match(r"([a-z]+)", text)
                    if match is None:  # Shouldnt occur
                        raise TimeArgException

                    [match] = match.groups()
                    tmp_splitted.append(match)

                    try:
                        text = text[text.index(match)+len(match):]
                        if text == '':
                            raise IndexError
                    except IndexError:
                        break

        return tmp_splitted

    def get_set_time(self):
        """Gets time set by user in milliseconds"""
        self.time_set = self._get_millis()

    def _get_millis(self):
        """Returns time set by user in milliseconds"""
        num = None
        unit = None
        time_set = 0
        for text in self.selected_time:
            if self.is_num(text):
                num = int(text)
            else:
                unit = text

            if num is not None and unit is not None:
                if unit in ['m', 'min']:
                    multiplier = 60 * 1000
                elif unit in ['h']:
                    multiplier = 60 * 60 * 1000

                time_set += num * multiplier
                num, unit = None, None

        return time_set

    def is_num(self, text) -> bool:
        """Simple check if text is a num"""
        try:
            int(text)
            return True
        except ValueError:
            return False

    def start_counting(self):
        """Start counting and updates clock once per second"""
        self.timer.start(1000)
        if self.start_time is None:
            self.start_time = monotonic()

    def get_human_time(self, time):
        """Get human readable time to display onto screen"""
        hours = time // (1000 * 60 * 60)
        left_time = time % (1000 * 60 * 60)
        minutes = left_time // (1000 * 60)
        left_time = minutes % (1000 * 60) if minutes != 0 else left_time
        seconds = left_time // (1000)

        return '0' * (2 - len(str(hours))) + str(hours) + ':' + \
               '0' * (2 - len(str(minutes))) + str(minutes) + ':' + \
               '0' * (2 - len(str(seconds))) + str(seconds)

    def timer_timeout(self):
        """Update timer on screen once per second"""
        elapsed = int(monotonic() - self.start_time) * 1000

        human_readable = self.get_human_time(elapsed)

        self.display(human_readable)

        if elapsed >= self.time_set:
            print('Koniec')
        else:
            self.start_counting()
