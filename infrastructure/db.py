from dataclasses import dataclass
import datetime
import sys

from infrastructure import settings
from domain import distance

def create(input_db):
    """
    dbインスタンスの作成(標準入力のパース)

    Args:
        input_db:
            初期設定に関する部分の標準入力
    
    Returns:
        dbインスタンス
    """
    cumulative_distance = distance.Distance(0)
    cumulative_time = datetime.timedelta()

    hhmmssfff, dist = input_db[0].split()

    if dist != "0.0":
        print("1行目の走行距離が0ではありません")
        sys.exit(1)
    
    hour, minute, secondfff = hhmmssfff.split(":")
    hour = int(hour)
    minute = int(minute)
    second, fff = map(int, secondfff.split("."))

    last_record_time = datetime.datetime(
        year=settings.THIS_YEAR,
        month=settings.THIS_MONTH,
        day=settings.TODAY+hour//settings.HOURS_A_DAY,
        hour=hour%settings.HOURS_A_DAY,
        minute=minute,
        second=second,
        microsecond=fff*1000
        )

    db = DB(cumulative_distance, last_record_time, cumulative_time)
    return db

@dataclass
class DB():
    """
    dbインスタンス

    Attributes:
        cumulative_distance: 現在までの走行距離*1000
        last_record_time: 前回の記録時間(datetime.microsecondを使って管理)
        cumulative_time: 現在までの低速走行時間(microsecond(10**6microsecond = 1second))
    """
    cumulative_distance: distance.Distance
    last_record_time: datetime.datetime
    cumulative_time: datetime.timedelta

