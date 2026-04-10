
from flask import Blueprint , render_template
from . import dialog
from flask import session, redirect, url_for
from lib.groupClass import Group

@dialog.route('/api_keys_t', methods=['GET'])
def get_api_keys_html():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    try:
        groups = Group.get_groups()
    except Exception as e:
        return {'error': 'An error occurred while fetching groups: ' + str(e)}, 500 
    
    return render_template('dialog/api_keys_dialog.html',session=session,groups=groups)