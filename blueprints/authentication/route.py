from lib.userClass import User
from flask import render_template, redirect, url_for, flash, request ,session
from flask import Blueprint
from lib.SessionClass import Session
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
        sess = Session(session['session_id'])
        if sess.is_valid():
            return redirect(url_for('dashboard'))
        session['authenticate'] = False
        sess.collection.active = False
        return {
            'message' : 'Session Expired',
            'authenticated' : False
        },401
    else:  
        user = request.get_json()
        try:
            user_name = User.login(user,request)
            sess = Session.register_session(user_name, request)
            session['authenticated'] = True

            session['session_id'] = sess.id
            session['username'] = sess.collection.username
            
            return {'message': 'Login successful', 'username': session['username'], 'session_id': sess.id,'session_username':sess.collection.username}, 200
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
        return {'error': str(e)}, 400
    except DuplicateUserError as e:
        return {'error': str(e)}, 409
    except Exception as e:
        return {'error': 'An unexpected error occurred: ' + str(e)}, 500