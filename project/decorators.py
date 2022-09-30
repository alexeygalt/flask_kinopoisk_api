from flask import current_app, request, abort
import jwt


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401, "Authorization not found")
        token = request.headers['Authorization'].split('Bearer ')[-1]
        try:
            jwt.decode(token, current_app.config.get('JWT_SECRET'),
                       algorithms=[current_app.config.get('JWT_ALGORITHM')])
        except Exception:
            abort(401, "JWT Decode Exception")
        return func(*args, **kwargs)

    return wrapper
