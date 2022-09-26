Model of Realtime Cataloguing Statistics

GitHub repository : https://github.com/rudysant/catstat.git 

Python & Django based

Feature :
- General statistics
- Detailed statistics
- Search by date

Statistics :
- Daily
- Weekly
- Monthly
- Annual
- By cons number

Model / DB :
- ID
- Entrydate (auto current date)
- Fulltitle :
- Title original
- Title translation
- Title adaptation


Multi volume? Y/N
Cons number
Copycatmod? Y/N

ISBN :
Yes
No

Series :
Yes
No

Authorship :
Single 
Collaboration
Compilation

Language :
English
Indonesian
Local Javanese
Local Sundanese

Publisher :
Commercial
Government department
Government non department
Government local
Universities state
Universities private
Personal
NGO foundation
Unknown


Subject :
000 General works
100 Philosophy
200 Religion
300 Social sciences
400 Languages
500 Science
600 Applied science
700 Arts
800 Literature
900 History

Genre :
Literature fiction novel
Literature fiction short stories
Literature poetry
Literature folk
Literature criticism
Biography single
Biography collective
General

Size :
YY
YYq
YYp
YYf


Format :
Book monograph
Book serial
Non book electronic document
Non book video
Non book ephemera
Non book audio


Steps:
Create environment
Create environment folder : nlacat
Go to nlacat folder
> Python -m venv .venv
> source .venv/bin/activate

Open VS Code software
Open nlacat folder
Select command palette from menu : Ctrl Shift P
Select python interpreter
Select .venv as recommended
From menu select Terminal > New terminal
Install django
> python -m pip install django
Create project: 
> django-admin startproject catreport .
Create app
> python manage.py startapp catstat



 



