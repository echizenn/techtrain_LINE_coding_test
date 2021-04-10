from sys import stdin
from typing import List

from application import application
from infrastructure import db

def main(input_db: List[str], input_queries: List[str]):
    """
    アプリの実行

    Args:
        input_db:
            初期設定に関する部分の標準入力
        input_query:
            クエリ部分の標準入力
    """
    db = db.create(input_db)

    app = application.App(db)

    for input_query in input_queries:
        app.execute(input_query)


if __name__=='__main__':
    input = stdin.readline

    # 入力を受け付ける
    db = [input()[:-1]]

    queries = list()
    while True:
        input_query = input()
        if input_query == "":
            break
        queries.append(input_query[:-1])

    main(db, queries)