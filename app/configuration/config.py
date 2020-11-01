import os
MysqlAddress=os.environ.get("MYSQL_ADDRR","localhost")
PORT=os.environ.get("MYSQL_PORT",3306)
USER=os.environ.get("MYSQL_USER","root")
PASS=os.environ.get("MYSQL_PASS","root")
DBName=os.environ.get("MYSQL_DB","autograder")
storage=os.environ.get("MARKAR_STORAGE","/Users/khan/autograder-storage/")
passwordfile=os.environ.get("ADMIN_EMAIL_PASS","/Users/khan/password.txt")