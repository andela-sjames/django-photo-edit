django-migrations:
	echo "Entering Docker conatianer and creating migrations/running migrate..."
	docker exec photo_edit_web bash -c 'python manage.py makemigrations && python manage.py migrate'
