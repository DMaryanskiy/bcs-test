# BLockchain Solutiuons test task.

## Installation

1. clone repository and enable virtual environment
For Windows:
```
python -m venv venv
./venv/Scripts/activate.bin
```
For Linux:
```
python3 -m venv venv
. /venv/Scripts/activate
```
2. Install requirements
```
pip install -r requirements.txt
```
3. Make and run migrations
```
python manage.py makemigrations
python manage.py migrate
```
4. Collect static
```
python manage.py collectstatic
```
5. Run server
```
python manage.py runserver
```