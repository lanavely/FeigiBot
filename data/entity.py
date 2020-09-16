import config.database

from playhouse.postgres_ext import PostgresqlExtDatabase

psql_db = PostgresqlExtDatabase(config.database.DB_NAME, user=config.database.DB_USER,
                                password=config.database.DB_PASSWORD, host=config.database.DB_HOST,
                                port=config.database.DB_PORT, register_hstore=False)
