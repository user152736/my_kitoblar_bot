from os import getenv
from dotenv import load_dotenv

load_dotenv()
HOST = getenv('HOST')
DATABASE = getenv('DATABASE')
PORT = getenv('PORT')
USER_NAME = getenv('USER_NAME')
PASSWORD = getenv('PASSWORD')


if __name__ == '__main__':
    print(HOST)
    print(DATABASE)
    print(PORT)
    print(USER_NAME)
    print(PASSWORD)