from dataclasses import dataclass
import datetime
import sys

from infrastructure import settings

def create(input_db):
    """
    dbインスタンスの作成(標準入力のパース)

    Args:
        input_db:
            初期設定に関する部分の標準入力
    
    Returns:
        dbインスタンス
    """
    # 入力を受け取り、それぞれレポジトリを作成し、dbインスタンスに格納する
    # 定数はレポジトリにせずにインスタンス変数としていい
    cumulative_distance = 0
    cumulative_time = 0

    hhmmssfff, dist = input_db[0].split()

    if dist != "0.0":
        print("1行目の走行距離が0ではありません")
        sys.exit(1)
    
    hour, minute, secondfff = hhmmssfff.split(":")
    hour = int(hour)
    minute = int(minute)
    second, fff = map(int, secondfff.split("."))

    last_record = datetime.datetime(
        year=settings.THIS_YEAR,
        month=settings.THIS_MONTH,
        day=hour//settings.HOURS_A_DAY+settings.TODAY,
        hour=hour%settings.HOURS_A_DAY,
        minute=minute,
        second=second,
        microsecond=fff*1000
        )

    db = DB(cumulative_distance, last_record, cumulative_time)
    return db

@dataclass
class DB():
    """
    dbインスタンス

    Attributes:
        cumulative_distance: 現在までの走行距離*1000
        last_record: 前回の記録時間(datetime.microsecondを使って管理)
        cumulative_time: 現在までの低速走行時間(microsecond(10**6microsecond = 1second))
    """
    cumulative_distance: int
    last_record: datetime.datetime
    cumulative_time: int

