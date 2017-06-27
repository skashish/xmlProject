# xmlProject

Written in Django Framework, xmlProject is an app which takes the path of a folder as input and returns a well formed directory structure in xml format.

The xml file contains all the files and directories inside the given directory recursively.
All the files also have their md5sum along with their names.

# how to install

1. Make sure python3 is installed.
   If not installed, install using `sudo apt-get install python3` (on debian/Ubuntu)

2. Install python package maqnager pip.
   `sudo apt-get install python-pip`

3. Install Django
   `sudo pip3 install django`

4. Download the repository `https://github.com/skashish/xmlProject.git`

5. Change Working Directory. `cd ./xmlProject/mysite`.

6. Run the server using `python3 manage.py runserver`.

At this point, hopefully the server should be up and running. Visit http://127.0.0.1:8000 
on your browser to visit the website.
