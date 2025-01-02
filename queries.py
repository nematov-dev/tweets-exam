import logging

from database import execute_query

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename="logs.log"
)


def logger(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error(f"Function {func.__name__}, args: {args}, kwargs: {kwargs}, error: {e}")
    return wrapper

@logger
def create_tables() -> bool | None:
     tweets = """
               CREATE TABLE IF NOT EXISTS tweets (
               id INT AUTO_INCREMENT PRIMARY KEY,
               user_id BIGINT NOT NULL,
               full_name VARCHAR(255) NOT NULL,
               text TEXT NOT NULL,
               created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"""
     
     users = """
               CREATE TABLE IF NOT EXISTS users (
               id INT AUTO_INCREMENT PRIMARY KEY,
               full_name VARCHAR(255) NOT NULL,
               email VARCHAR(128) NOT NULL,
               password VARCHAR(128) NOT NULL,
               created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
               is_login SMALLINT NOT NULL DEFAULT 0,
               status SMALLINT NOT NULL DEFAULT 0)"""
     
     send_verification_codes = """
               CREATE TABLE IF NOT EXISTS verification_codes (
               id INT AUTO_INCREMENT PRIMARY KEY,
               email VARCHAR(128) NOT NULL,
               code INT NOT NULL,
               created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"""
     
     execute_query(query=tweets)
     execute_query(query=users)
     execute_query(query=send_verification_codes)
     
     return True

@logger
def show_tweets_query() -> list[tuple] | None:
     query = """
          SELECT * FROM tweets"""
     return execute_query(query=query,fetch="all")


@logger
def add_tweet_query(user_id: int,full_name: str,text: str) -> bool | None:
     query = """
          INSERT INTO tweets(user_id,full_name,text)
          VALUES (%s,%s,%s)"""
     execute_query(query=query,params=(user_id,full_name,text,))
     return True

@logger
def update_tweet_query(user_id: int,text_id: int,text: str) -> bool | None:
     query = "UPDATE tweets SET text = %s WHERE id = %s and user_id = %s"
     execute_query(query=query,params=(text,text_id,user_id,))
     return True

@logger
def get_tweet(user_id: int,text_id:int) -> list[tuple] | None:
     query = "SELECT * FROM tweets WHERE id = %s and user_id = %s"
     return execute_query(query=query,params=(text_id,user_id,),fetch="one")

@logger
def delete_tweet_query(user_id: int,text_id: int) -> bool | None:
     query = "DELETE FROM tweets WHERE id = %s and user_id = %s"
     execute_query(query=query,params=(text_id,user_id,))
     return True

@logger
def show_my_tweets_query(user_id: int) -> list[tuple] | None:
     query = "SELECT * FROM tweets WHERE user_id = %s"
     return execute_query(query=query,params=(user_id,),fetch="all")



@logger
def get_user_by_email(email:str):

     query = """
          SELECT * FROM users WHERE email = %s"""
     return execute_query(query=query,params=(email,),fetch="one")
    
@logger
def add_user_query(params: tuple) -> bool | None:

     query = """
     INSERT INTO users (full_name, email,password)
     VALUES (%s, %s,%s)
     """
     execute_query(query=query, params=params)
     return True

@logger
def get_user_code(email:str,code: int):
     query = """
          SELECT * FROM verification_codes WHERE email = %s and code = %s"""
     return execute_query(query=query,params=(email,code,),fetch="one")

@logger
def add_verification_code(email: str,code:int):
 
     query = """
     INSERT INTO verification_codes (email,code)
     VALUES (%s, %s)
     """
     execute_query(query=query, params=(email,code,))
     return True

@logger
def update_user_status(email:str,status:int):
          query = """
               UPDATE users SET status = %s WHERE email = %s"""
          execute_query(query=query,params=(status,email,))
          return True

@logger     
def update_user_is_login(email:str,is_login:int):
          query = """
               UPDATE users SET is_login = %s WHERE email = %s"""
          execute_query(query=query,params=(is_login,email,))
          return True

@logger     
def get_active_user():
     query = """
          SELECT * FROM users WHERE is_login = 1"""
     return execute_query(query=query,fetch="one")

@logger
def logut_all():
     query = """
          UPDATE users SET is_login = 0 WHERE is_login = 1"""
     execute_query(query=query)
     return True