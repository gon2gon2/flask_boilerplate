export FLASK_APP=project_name
export FLASK_ENV=development
flask db init
flask db migrate
flask db upgrade