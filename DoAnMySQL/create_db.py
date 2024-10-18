import mysql.connector
import db_config as guiConf

GUIDB = 'test'

#unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)

cursor = conn.cursor()

try : 
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(GUIDB))
except mysql.connector.Error as err:
    print("Failed to create DB : {}".format(err))

conn.close()