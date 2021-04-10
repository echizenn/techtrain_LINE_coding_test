from dataclasses import dataclass
import math
import sys

from infrastructure import settings

@dataclass
class Distance():
    """
    距離を表すクラス

    Attributes:
        value: 距離*1000
    """
    value: int

    def add(self, dist, is_midnight):
        """
        距離を加える、深夜かどうかにも対応
        """
        if is_midnight:
            return Distance(self.value+dist.value*settings.MIDNIGHT_ADDITIONAL_DISTANCE_RATE/100)
        
        if not is_midnight:
            return Distance(self.value+dist.value)

        print("予期せぬエラー")
        sys.exit(1)

    def get_charge(self):
        """
        料金計算
        """
        if self.value <= 1052*1000:
            return 410
        return (math.ceil((self.value-1052*1000)/237000))*80+410