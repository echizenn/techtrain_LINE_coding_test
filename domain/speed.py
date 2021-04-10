from dataclasses import dataclass
import datetime
import sys

from domain import distance
from infrastructure import settings

@dataclass
class Speed():
    """
    速度を表すクラス

    Attributes:
        time: 移動時間
        distance: 移動距離
    """
    time: datetime.timedelta
    distance: distance.Distance

    def get(self):
        """
        速度を得る
        """
        microsecond_time = self.time/datetime.timedelta(microseconds=1)
        return self.distance.value*settings.MICROSECONDS_A_HOURS/microsecond_time

    def is_slow(self):
        """
        低速かどうか判定
        """
        value = self.get()
        return value <= 10