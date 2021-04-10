from dataclasses import dataclass
import datetime

@dataclass
class Times():
    last_time: datetime.datetime
    current_time: datetime.datetime

    def is_midnight(self):
        # TODO できれば単独のTimeクラス作る
        is_midnight_last_time = 0 <= self.last_time.hour%24 < 5
        is_midnight_current_time = 0 <= self.current_time.hour%24 < 5
        return is_midnight_last_time and is_midnight_current_time