# Q2-JaneSmithDoe

# DEMO / USAGE
Visit http://52.40.255.86/
You should see "Jane Smith Doe"

Visit http://52.40.255.86/getAFirstName
This implies a GET request for the RESTful endpoint
Yous should see "Jane"

You can also try the other two endpoints:
getAMiddleName and getALastName

# Software Architecture

Your
Web Client                      AWS EC2 Ubuntu Server
                                   52.40.255.86:80
                 --------------------------------------------------
                 |                                                |
                 | --------------------      -------------------- |
                 | |   52.40.255.86:80|      |  127.0.0.1:6347  | |
                 | | WebServer        |      |  Redis           | |
     =======>    | | --------------   |      |                  | |
                 | | (Python Flask)   |      |                  | |
                 | |                  |      |                  | |
                 | | q2-server.py     | <==> | HashTable TheName| |
                 | --------------------      -------------------- |
                 |                                                |
                 --------------------------------------------------


# How to deploy the system on your own PC:
Linux OS:

1: Install Python Package Via Pip

sudo install python-pip
sudo pip install flask-restful
sudo pip install redis

2: Install Redis
wget http://download.redis.io/releases/redis-5.0.7.tar.gz
tar -xzv -f redis-5.0.7.tar.gz
cd redis-5.0.7.tar.gz
make
sudo make install
sudo ldconfig

3. Run Redis Server
redis-server

4. Run Redis Client and set the table
redis-client
HSET TheName FirstName  "Jane"
HSET TheName MiddleName "Smith"
HSET TheName MiddleName "Doe"

5. Run the Web Server
sudo ./q2-server.py

6. Test via 127.0.0.1
