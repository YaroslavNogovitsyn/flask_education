import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        query = """SELECT * FROM mainmenu"""
        try:
            self.__cur.execute(query)
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error:
            print('Ошибка чтения из БД')
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print(f"Ошибка получения статьи из БД {e}")
            return False

        return True

    def getPost(self, post_id):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE id = {post_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print(f"Ошибка получения статьи из БД {e}")

        return False, False

    def getPostsAnonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print(f"Ошибка получения статьи из БД {e}")

        return []
