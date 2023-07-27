import streamlit as st
import mysql.connector
from mysql.connector import Error


def connect():
    try:

        connection = mysql.connector.connect(
            host = '',
            database = 'pets',
            user = 'streamUser',
            password = '123qwer@'
        )

        if connection.is_connected() :
            print('CONNECTION SUCCESS')
            db_info = connection.get_server_info()
            # print('server version: ', db_info)

            # cursor = connection.cursor(buffered=True) 
            cursor = connection.cursor()

            cursor.execute('select * from mytable;')

            # record = cursor.fetchone() 단 건의 데이터를 가져오는 경우 fetchon() 
            record = cursor.fetchall() # 복수 건의 데이터를 가져오는 경우 fetchall()

            print('CONNECTED TO DB : ', record)

            return connection

    except Error as e:
        print('CONNECTION ERROR')

    finally :
        cursor.close()
        connection.close()
        print('CONNECTION CLOSE')

# def execute(query) :

if __name__ == "__main__" :
    conn = connect()

