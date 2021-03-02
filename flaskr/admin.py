from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('admin', __name__)


@bp.route('/admin')
def admin():
    db = get_db()
    users = db.execute(
        "SELECT * FROM user"
    ).fetchall()
    
    if users is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    return render_template('admin/admin.html', users=users)






