export FLASK_APP=project_name FLASK_ENV=development
flask db init
flask db migrate
flask db upgrade