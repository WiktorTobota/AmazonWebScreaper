# AmazonWebScreaper
dependencies

virtualenv

http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html

sudo pip install vitualenvwrapper

in .bash_profile add (or create)

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

then create a virtualenv

which python3

mkvirtualenv --python=/usr/local/bin/python3 <project>

it will create a new python install in the ~/.virtualenv/<project directory>
you can switch to that by using the command

workon <project>

Now we will use cookiecutter to create a skeleton python package

https://cookiecutter.readthedocs.io/en/latest/readme.html

pip install cookiecutter

cookiecutter https://github.com/DuaneNielsen/specs-cookiecutter.git

you will be prompted for the package details, after which the project boilerplate will be created
* dont use hyphens in the project name, python does not like that *

example below..

(manic_entropy_typhoon) niedu02mac1454:PycharmProjects niedu02$ cookiecutter https://github.com/openstack-dev/specs-cookiecutter
module_name [replace with the name of the python module]: manic_entropy_typhoon
repo_group [openstack]: duanenielsen
repo_name [replace with the name for the git repo]: manic_entropy_typhoon
project_short_description [OpenStack Boilerplate contains all the boilerplate you need to create an OpenStack package.]: Test of the pbr packaging system using cookiecutter
project_name [replace with the lp project used for the specs in the repo]: manic_entropy_typhoon

commit to git before doing anything else

cd <project>
git init
git add .
git commit -m 'first commit'

install the requirements using pip

delete oslosphinx from the requirements.. it sucks anway

pip install -r requirements.txt

create your python file in the <project>/<project> directory, eg: hello.py

Then commit the project to git



tests are in the <project>/tests directory

to run tests use

cd <project>
python setup.py test


create repository of <project> on github

ensure your ssh private keys for github are installed on ssh-agent

git remote add origin git@github.com:DuaneNielsen/<project>.git
git push -u origin master

register an account on pypi.python.org

vi ~/.pypirc

[distutils]
index-servers=pypi

[pypi]
username=<userid>
password=<password>

build your distributions (source and wheel)

cd <project>
python setup.py sdist
python setup.py bdist_wheel

upload the sdist to pypi

pip install twine
twine upload dist/*

to iterate

if on another machine install the dependencies after checking out...

mkvirtualenv <project>

git clone <project url>

cd <project>

python setup.py develop

python setup.py test
