set FLASK_APP=project_name
set FLASK_ENV=development
flask db init
flask db migrate
flask db upgrade