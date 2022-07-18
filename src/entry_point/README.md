# RUN

        ros2 launch entry_point demo.launch.py
        ros2 launch entry_point demo.record.xml

# SQLite to MySQL
        pip install sqlite3-to-mysql

## to local mySQL server
        sqlite3mysql -f test.db3 -d myDB -u root -p 

## dump the local sql
        mysqldump -h 127.0.0.1 -u root -p myDB > myDB.sql

## load from dump to local/remote SQL
- local

        mysql -h 127.0.0.1 -u root -p myDB1 < myDB.sql

- remote

        mysql -h database-1.ccw5fkifii2t.us-east-1.rds.amazonaws.com -u root -p myDB < myDB.sql
