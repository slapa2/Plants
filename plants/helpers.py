from functools import wraps

from flask import redirect, url_for, flash
from flask_login import current_user

def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            user = current_user
            roles = [role.name for role in user.roles]
            print(roles)
            if not set(roles) & set(access_level):
                flash('Nie masz dostępu do tej strony!', 'danger')
                return redirect(url_for('auth.account'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
