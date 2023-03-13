
import os


def get_base_url():

    env = os.environ.get('ENV', 'test')
    if env.lower() == 'test':
        return 'http://localhost/quicksite/index.php'
    else:
        raise Exception(f"Unknown Environment: {env}")


def get_database_credentials():

    env = os.environ.get('ENV', 'test')
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")

    if not (db_user or db_password):
        raise Exception("Environment variables 'DB_USER' AND 'DB_PASSWORD' must be set. ")

    if env == 'test':
        db_host = '127.0.0.1'
        db_port = 3306
    elif env == 'prod':
        db_host = 'demostore.supersqa.com'
        db_port = '3306'
    else:
        raise Exception(f"Unknown Environment variable:- {env}")

    db_info = {"db_host": db_host, "db_port": db_port,
               "db_user": db_user, "db_password": db_password}
    return db_info
