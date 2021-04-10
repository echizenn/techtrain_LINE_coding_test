from dataclasses import dataclass
import datetime

from domain import distance, speed, time
from infrastructure import db, settings

@dataclass
class App():
    """
    アプリケーションクラス
    入力を受けて実行をする

    Attributes:
        db: dbインスタンス
    """
    db: db.DB

    def execute(self, input_query):
        """
        標準入力のクエリ一つを受けて実行する関数

        Attributes:
            input_query: 標準入力のクエリ
        """
        hhmmssfff, dist = input_query.split()
        
        hour, minute, secondfff = hhmmssfff.split(":")
        hour = int(hour)
        minute = int(minute)
        second, fff = map(int, secondfff.split("."))

        current_time = datetime.datetime(
            year=settings.THIS_YEAR,
            month=settings.THIS_MONTH,
            day=settings.TODAY+hour//settings.HOURS_A_DAY,
            hour=hour%settings.HOURS_A_DAY,
            minute=minute,
            second=second,
            microsecond=fff*1000
        )

        dist_int_part, dist_float_part = dist.split(".")

        dist = distance.Distance(int(dist_int_part)*1000+int(dist_float_part)*100)

        self.update_cumulative_time(current_time, dist)
        self.update_cumulative_distance(current_time, dist)

        self.db.last_record_time = current_time

    def update_cumulative_distance(self, current_time, dist):
        """
        累積走行距離を更新する
        """
        times = time.Times(self.db.last_record_time, current_time)
        is_midnight = times.is_midnight()

        cumulative_distance = self.db.cumulative_distance.add(dist, is_midnight)

        self.db.cumulative_distance = cumulative_distance


    def update_cumulative_time(self, current_time, dist):
        """
        累積低速走行時間を更新する
        """
        t = current_time-self.db.last_record_time
        s = speed.Speed(t, dist)
        is_slow = s.is_slow()
        if not is_slow:
            return

        times = time.Times(self.db.last_record_time, current_time)
        is_midnight = times.is_midnight()

        if is_midnight:
            cumulative_time = self.db.cumulative_time + t*settings.MIDNIGHT_ADDITIONAL_TIME_RATE/100
        if not is_midnight:
            cumulative_time = self.db.cumulative_time + t

        self.db.cumulative_time = cumulative_time

    def require_charge(self):
        distance_charge = self.db.cumulative_distance.get_charge()

        slow_time_charge = (self.db.cumulative_time//datetime.timedelta(seconds=90))*80

        return distance_charge+slow_time_charge

        
    