from lib.userClass import User
from flask import render_template, redirect, url_for, flash, request ,session
from flask import Blueprint
from lib.apiKeyClass import APIKey
from lib.groupClass import Group
from . import api






@api.route("/apikey/row") 
def apikey_row():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    api_key_hash = request.args.get('hash')
    if not api_key_hash:
        return {'error': 'API key hash is required'}, 400  
    api_keys_ob = APIKey(api_key_hash)
    if api_keys_ob.collection._data is None:
        return {'error': 'API key not found'}, 404
    # print(api_keys_ob.collection._data)  # Debugging line to check API key data
    groups = Group.get_groups()
    return render_template("apikey/api-table.html", api_key=api_keys_ob.collection._data, groups=groups)
@api.route("/delete",methods=['POST'])
def delete_apikey():
    if not session.get('authenticated'):
        return {'error': 'Authentication required'}, 401 
    hash = request.form.get('hash')
    if not hash:
        return {'error': 'API key hash is required'}, 400
    api_key = APIKey(hash)
    if not api_key:
        return {'error': 'API key not found'}, 404
    try:
        api_key.collection.delete()
        return {'message': 'API key deleted successfully'}, 200
    except Exception as e:  
        print(str(e))
        return {'error': 'An error occurred while deleting the API key: ' + str(e)}, 500    
@api.route("/update/status",methods=['POST'])
def api_active():

    if not session.get('authenticated'):
        return {'error': 'Authentication required'}, 401 
    hash = request.form.get('hash')
    status = request.form.get('status')
    if not hash or status is None:
        return {'error': 'Hash and status are required'}, 400
    api_key = APIKey(hash)
    if not api_key:
        return {'error': 'API key not found'}, 404
    try:
        if status.lower() == 'true':
             api_key.collection.active = 1
        else:   
            api_key.collection.active = 0
        return {'message': 'API key status updated successfully'}, 200
    except Exception as e:  
        print(str(e))
        return {'error': 'An error occurred while updating the API key status: ' + str(e)}, 500
    