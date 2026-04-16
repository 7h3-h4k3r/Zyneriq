from lib.userClass import User
from flask import render_template, redirect, url_for, flash, request ,session
from flask import Blueprint
from lib.SessionClass import Session
from lib.groupClass import Group
from lib.apiKeyClass import APIKey
from uuid import uuid4
from lib.errorClass import DuplicateUserError, NotFoundUserError, PasswordError
from . import auth

'''user must validate the input before sending to backend, 
but we will also validate it here for security reasons.'''

@auth.route('/create/group', methods=['POST'])
def create_group():
    
    data = {
        'name': request.form.get('name'),
        'description': request.form.get('description')
    }
    if 'name' not in data or 'description' not in data:
        return {'error': 'Name and description are required'}, 400
    if not session.get('authenticated'):
        return {'error': 'Authentication required'}, 401
        
    group_name = data['name']
    group_desc = data['description']
    if not group_name or not group_desc:
        return {'error': 'Name and description cannot be empty'}, 400
    try:        
        Group.register_group(group_name, group_desc)
        return {'message': 'Group created successfully'}, 201
    except Exception as e:
        return {'error': 'An error occurred while creating the group: ' + str(e)}, 500  
    
@auth.route('/create/apikey', methods=['POST'])
def create_apikey():
    if not session.get('authenticated'):
        return {'error': 'Authentication required'}, 401
    
    name = request.form.get('name')
    group = request.form.get('group')
    remark = request.form.get('remark')
    
    if not name or not group:
        return {'error': 'Name and group are required'}, 400
    
    try:
        api_key = APIKey.create_api_key(session, name, group, remark, request=request)
        return {'message': 'API key created successfully', 'api_key': api_key.collection.id , 'api_key_hash': api_key.collection.hash}, 201
    except Exception as e:
        print(str(e))
        return {'error': 'An error occurred while creating the API key: ' + str(e)}, 500

@auth.route('/signin', methods=['POST'])
def authenticate():
    if session.get('authenticated'):
        sess = Session(session['session_id'])
        if sess.is_valid():
            return {'message': 'Already authenticated', 'username': session['username'],'authenticated': True}, 200
        session['authenticate'] = False
        sess.collection.active = False
        return {
            'message' : 'Session Expired',
            'authenticated' : False
        },401
    else:  
        user = request.get_json()
        try:
            sessid = User.login(user,request)
            session['authenticated'] = True
            session['session_id'] = sessid
            session['username'] = user['username']
            session['type'] = 'web'
            if 'redirect' in request.form and request.form['redirect'] == True:
                return redirect(url_for('dashboard'))
            return {'message': 'Login successful', 'username': session['username']}, 200
        except:
            return {'error': 'Invalid username or password'}, 401

@auth.route('/register', methods=['POST'])
def register():
    
    user = request.get_json()
   
    try:
        User.signup(user)
        return {'message': 'Signup successful',
    
        }, 201

    except DuplicateUserError as e:
        return {'error': str(e)}, 409
    except Exception as e:
        return {'error': 'An unexpected error occurred: ' + str(e)}, 500