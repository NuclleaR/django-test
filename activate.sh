ENV=$1
source $ENV/bin/activate

run() {
  echo "Start Django server..."
  python manage.py runserver 0.0.0.0:8080
}

migrate() {
  echo "Start migrating..."
  python manage.py migrate
  echo "Done"
}

makemigrations() {
  echo "Making migrations..."
  python manage.py makemigrations
  echo "Done"
}

createsuperuser() {
  echo "Create super user"
  python manage.py createsuperuser
  echo "Done"
}

collectstatic() {
  echo "Collecting all static..."
  python manage.py collectstatic
  echo "Done"
}

startapp() {
  APP=$1
  echo "Starting app" $APP
  python manage.py startapp $APP
  echo "Done"
}

reset_migrations() {
  file=$(find . -path "**/db.sqlite3")
  # echo $file
  echo "Delete all migrations..."
  find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
  find . -path "*/migrations/*.pyc" -delete
  echo "Done"
  if [ ! -e "$file" ]; then
      echo "Please make sure that you drop DataBase"
      echo "and run 'python manage.py makemigrations && python manage.py migrate'"
  else
    find . -path "**/db.sqlite3" -delete
    # echo "File exists"
    echo "Make new migrations..."
    python manage.py makemigrations
    echo "Done"
    echo "Migrating..."
    python manage.py migrate
    echo "Done"
  fi 
}

reinstall() {
  pip install --upgrade --force-reinstall -r requirements.txt
}