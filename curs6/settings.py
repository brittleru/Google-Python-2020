DB_HOST = "localhost"
DB_NAME = "desktop_app_db"
DB_USER = "root"
DB_PASS = ""
DB_PORT = 3306
DB_CONNECTION = "mysql+mysqldb://%s:%s@%s:%s/%s" % (
    DB_USER,
    DB_PASS,
    DB_HOST,
    DB_PORT,
    DB_NAME,
)
