# Voting Application 
Voting is a django based app.Includes the following functionalites

  - Parties
  - Candidates
  - Voting
  - 
 ## To run the app:
  - Clone the Repository
  - Create the virtualenv for the project
### Install  dependencies for the  project
 ```bash
$ pip  install virtualenvwrapper 
$ mkvirtualenv --python=python3.6  voting
$ workon voting
$ pip install  -r  requirments/development.txt
```
  ### Migrations
 ```
$ python  manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver 
```
