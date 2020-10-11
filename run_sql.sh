docker run --name autograder-DB -p 3306:3306 -v DB:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
