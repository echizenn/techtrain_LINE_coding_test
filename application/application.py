from dataclasses import dataclass

from infrastructure import db

@dataclass
class App():
    """
    アプリケーションクラス
    入力を受けて実行をする

    Attributes:
        db: dbインスタンス
    """
    db: db.DB

    def execute(input_query):
        """
        標準入力のクエリ一つを受けて実行する関数

        Attributes:
            input_query: 標準入力のクエリ
        """
        pass
    