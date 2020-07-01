""" This module can be used to create users for initial setup. Run
`cat docs/project_deps/data_creation/user_creator.py | python manage.py shell`
to use this. Remember to change USERNAME_LIST to change usernames. """

from django.contrib.auth.models import User

def main():
	USERNAME_LIST = ['testuser1', 'testuser2', 'testuser3', 'randomusername']
	
	for username in USERNAME_LIST:
	    User.objects.create_user(
	        username=username,
	        password='test-pass'
	    )

if __name__=='__main__':
	main()