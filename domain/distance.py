from dataclasses import dataclass

@dataclass
class Distance():
    """
    距離を表すクラス

    Attributes:
        value: 距離*1000
    """
    value: int
