from dataclasses import dataclass

from infrastructure import user

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
    user_repository = user.create(input_db)
    db = DB(user_repository)
    return db

@dataclass
class DB():
    """
    dbインスタンス

    Attributes:
        _db: インフラ層のあるドメインのレポジトリ
    """
    _db: user.Repository
