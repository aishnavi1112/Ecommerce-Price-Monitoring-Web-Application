from flask import Blueprint, flash, request, render_template, session, redirect, url_for
from models import *
notification_bp = Blueprint(
    'notifications', __name__, url_prefix='/notifications')


def notifications():
    email = session['email']
    user = User.query.filter_by(email=email).first()
    notifications = Notification.query.filter_by(user_id=user.id).all()
    return render_template("website/notifications.html", notifications=notifications)


def mark_read():
    notification_id = request.args.get("notification_id")

    Notification.query.filter_by(id=notification_id).delete()
    db.session.commit()
    return redirect(url_for('notifications.notification'))


notification_bp.add_url_rule('/mark_read', 'mark_read', mark_read , methods=['GET', 'POST'])


notification_bp.add_url_rule('/', 'notification', notifications, methods=['GET', 'POST'])
