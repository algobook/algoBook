# algoBook

[![Build Status](https://travis-ci.org/algobook/algoBook.svg?branch=master)](https://travis-ci.org/algobook/algoBook)
[![Heroku](https://heroku-badge.herokuapp.com/?app=algobook)](http://algobook.herokuapp.com)


Objective:
To Develop a community based platform where people can learn and share algorithms of any language and platform.

algoBook is focused to curated list of algorithms, solutions and their explanations on the basis of community feedback. It is an open platform for users to come and submit solutions to various algorithms in any language and of any platform.

## Installation
## Steps

Make sure you have the dependencies mentioned above installed before proceeding further.

* **Step 0** - Clone the Open Event Orga Server repository (from the development branch) and ```cd ``` into the directory.
```sh
git clone -b development https://github.com/algobook/algobook.git
cd algobook
```


* **Step 1** - Install python requirements. You need to be present into the root directoryt  of the project.

```sh
sudo -H pip install -r requirements.txt
```
* **Step 2** - Algobook expect two enviroment variables for sending email. You can set them to dummy for testing.

```sh
 export DJANGO_EMAIL='dummy'
 export DJANGO_EMAIL_PASSWORD='dummy'
```
* **Step 3** - Run Migration, create database

```sh
python manage.py migrate
```
* **Step 4** - Install bower and frontend requirements. For this you need to be present in the root directory of the project. The root directory contains the file ```bower.json```. When you write ```bower install```, it finds bower.json and installs the libraries on the system.

```sh
npm install bower -g
bower install
```

if error
```sh
sudo npm install bower -g
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo bower install
```

for mac user:
```sh
sudo npm install bower -g
bower install
```
# run app
python manage.py runserver
