from lib.userClass import User
from flask import render_template, redirect, url_for, flash, request ,session
from flask import Blueprint
from lib.errorClass import DuplicateUserError, NotFoundUserError, PasswordError
from . import auth

'''user must validate the input before sending to backend, 
but we will also validate it here for security reasons.'''

@auth.route('/', methods=['POST'])
def alreaduyLogin():
    if session.get('authenticated'):
        return {'username': session.get('username')}, 200
    else:
        return {'message': 'Not authenticated'}, 401
@auth.route('/login', methods=['POST'])
def login():
    if session.get('authenticated'):
        return redirect(url_for('dashboard'))
    user = request.get_json()
    try:
        user_name = User.login(user)
        return {'message': 'Login successful', 'username': user_name}, 200
    except NotFoundUserError as e:
        return {'error': str(e)}, 404
    except PasswordError as e:
        return {'error': str(e)}, 401
    except ValueError as e:
        return {'error': str(e)}, 401

@auth.route('/signup', methods=['POST'])
def signup():
    
    user = request.get_json()
    try:
        User.signup(user)
        return {'message': 'Signup successful'}, 201
    except ValueError as e:
        return {'message': str(e)}, 400
    except DuplicateUserError as e:
        return {'message': str(e)}, 409
    except Exception as e:
        return {'message': 'An unexpected error occurred: ' + str(e)}, 500