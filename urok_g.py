# Реляционные бд
# СУБД - Система управление базами данных
# Сурогатные и естественные ключи
# типы связей - М - М, М - 1, 1 - 1
# Внешние ключи для связей таблиц
# декларативный язык программирования при помощи которого происходит управление базами данных
# Select - получение информации
# SELECT (ЧТО) FROM (ТАБЛИЦА) - SELECT * FROM Товар
# WHERE - условие
# SELECT * FROM Товар WHERE price <= 1000;
# SELECT DISTINCT NAME FROM ToBap WHERE PRICE - выборка уникальных данных с фильтрацией
# INSERT (INTO)
# INSERT (INTO) НАЗВАНИЕ ТАБЛИЦЫ (ПОЛЯ ТАБЛИЦЫ) VALUES (ЗНАЧЕНИЯ)
# INSERT INTO Товар (id, name, price) VALUES (4, 'Телефон', 3000) можно и без id
# чтобы вписать все значения можно не указывать куда указывать например:
# INSERT INTO ToBap VALUES (ЗНАЧЕНИЯ)
# DELETE FROM
# DELETE FROM НАЗВАНИЕ ТАБЛИЦЫ WHERE УСЛОВИЕ
# DELETE FROM PC WHERE PC.hd = (SELECT MIN(hd) FROM PC) OR PC.ram = (SELECT MIN(ram) FROM PC)
# UPDATE НАЗВАНИЕ ТАБЛИЦЫ SET НАЗВАНИЕ СТОЛБЦА = НОВОЕ ЗНАЧЕНИЕ WHERE УСЛОВИЕ
# CREATE TABLE IF NOT EXISTS
#
#
#
#
#
#
#
#
#
# import sqlite3
# from sqlite3 import SQLITE_SELECT
#
# connection = None
# try:
#     connection = sqlite3.connect('data_1.db')
#     cursor = connection.cursor()
#     pass
# except sqlite3.DatabaseError:
#     print('error: WATAHELL OMG NO WAAYAYAYAY')
# finally:
#     connection.close()
# the_amongus = True
# sus = True
# if the_amongus is sus:
#     print('NOWAY')
# import sqlite3
#
# with sqlite3.connect('data_1.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute('CREATE TABLE IF NOT EXISTS users ('
#                    'id INTEGER PRIMARY KEY,'
#                    'name TEXT,'
#                    'age INTEGER)')
# import sqlite3
#
# class Database:
#     def __init__(self, db):
#         self.connection = sqlite3.connect(db)
#         self.cursor = self.connection.cursor()
#
#     def create_table(self):
#         with self.connection:
#             self.cursor.execute('CREATE TABLE IF NOT EXISTS users ('
#                                'id INTEGER PRIMARY KEY,'
#                                'name TEXT,'
#                                'age INTEGER,'
#                                 'gender TEXT)')
#
#     def add_user(self, name, age, gender):
#         with self.connection:
#             self.cursor.execute('INSERT INTO users (name, age, gender) VALUES (?, ?, ?)', (name, age, gender))
#     def get_users_info(self):
#         with self.connection:
#             return self.cursor.execute('SELECT * FROM users').fetchall()
#     def get_user_info(self, user_id):
#         with self.connection:
#             return self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
#
#     def update_user_age(self, user_id, age):
#         with self.connection:
#             return self.cursor.execute('UPDATE users SET age = ? WHERE id = ?', (age, user_id)).fetchone()
#     def delete_all_users(self):
#         with self.connection:
#             self.cursor.execute('DELETE FROM users')
#     def delete_user(self, user_id):
#         with self.connection:
#             self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id, ))
#     def get_users_based_on_gender(self, gender):
#         with self.connection:
#             return self.cursor.execute('SELECT * FROM users WHERE gender = ?', (gender, )).fetchall()
#
#
# if __name__ == '__main__':
#     db = Database('users1.db')
#     db.create_table()
#     db.add_user('Alice', 14, 'woman')
#     db.add_user('Dima', 18, 'man')
#     db.add_user('Mike', 19, 'man')
#     db.add_user('Nadya', 15, 'woman')
#     db.add_user('Masha', 31, 'woman')
#     db.add_user('Mike', 19, 'man')
#     print('Мужчины:', db.get_users_based_on_gender('man'))
#     print('Женщины:', db.get_users_based_on_gender('woman'))
# dir /b /o(d, n, s) ///// type - чтение содержмиого /// del - удалить /mkdir - создать дирекуторию //// /rmdir /s удалить директорию





#     db.delete_all_users()
# import os
# current_path = os.path.abspath(__file__)
# parrent_path = os.path.join(current_path, '..')
#
# print(current_path)
# print(parrent_path)
# def f(n):
#     if n == 1:
#         return n
#     else:
#         return f(n - 1) + n
# print(f(3))


# import sys
# sys.setrecursionlimit(3000)
#
# def f(n):
#     if n == 0:
#         return 1
#     if n > 0:
#         return f(n - 1) * 4
#
# print(f(2300) / f(2290))

# import os
# def get_all_files(path, st):
#     for my_file in os.listdir(path):
#         new_path = os.path.join(path, my_file)
#         if os.path.isdir(new_path):
#             print(f'{st}Папка: {my_file}')
#             get_all_files(new_path, st + ' ')
#
#         else:
#             print(f'{st} - {my_file}')
#
# get_all_files('D:\pyprojects\AiProject', '')
import time
def counter_str(name):
    start = time.time()
    with open(name, encoding='utf-8') as f:
        text = f.read()
        print(text)
        my_list = text.split('\n')
        for i in my_list:
            symbols_list = set()
            for f in i:
                symbols_list.add(f)
            symbols_list_count = []
            for f in symbols_list:
                symbols_list_count.append(f'{f} - {i.count(f)}')
            print(symbols_list_count)
    exit = time.time()
    return exit - start

print(counter_str('alo.txt'))
# O (N ** 2)

def str_counter(s):
    for sym in set(s):
        start = time.time()
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
            print(f'{sym} - {counter}')
        exit = time.time()
        return exit - start

l1 = str_counter('zxcvbzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxzcvxcbcvbcvbzxcvsdgfsddfgdhfghjghkjk;l')
# O (2 * N)
def strcounter(s):
    start = time.time()
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, '-', count)
    exit = time.time()
    return exit - start
l2 = strcounter('zxcvbzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxzcvxcbcvbcvbzxcvsdgfsddfgdhfghjghkjk;l')
print(l1, l2)
print(l1 - l2)

#git status
#git init
#git add . - добавить всё
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#