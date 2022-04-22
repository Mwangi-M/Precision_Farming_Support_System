# Precision Farming Support System (Django Project Template)

## Link to deployed site
https://Mwangi-M/

## Setup and installations
* git clone 'https://github.com/Mwangi-M/Precision_Farming_Support_System.git'
* Open the README.md file under the .github folder in your terminal with your favourite Text Editor.



## Technologies Used
1. PYTHON
2. HTML/CSS
3. JAVASCRIPT


### Prerequisites
1. Python              - 3.10.2
2. Pip                 - 22.0.3
3. Virtual Environment.


### Packages         -  Version 
1. arabic-reshaper      2.1.3
2. asgiref              3.5.0
3. Django               4.0.2
4. django-crispy-forms  1.14.0
5. future               0.18.2
6. html5lib             1.1
7. numpy                1.22.2
8. opencv-python        4.5.5.62
9. Pillow               9.0.1
10. pip                 21.2.4
11. PyPDF2              1.26.0
12. python-bidi         0.4.2
13. reportlab           3.6.6
14. setuptools          58.1.0
15. six                 1.16.0
16. sqlparse            0.4.2
17. tzdata              2021.5
18. webencodings        0.5.1
19. xhtml2pdf           0.2.5



## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r "https://github.com/Mwangi-M/Precision_Farming_Support_System/blob/master/Requirements.txt"

# You may want to change the name `projectname`.
$ django-admin startproject --template "https://github.com/Mwangi-M/Precision_Farming_Support_System/archive/refs/heads/master.zip" projectname

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```



## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.



## Contributing

I love contributions to my repositories, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.



## [LICENSE](LICENSE)
This project is licensed under the MIT License.

Copyright (c)2022 [Mwangi-M]
