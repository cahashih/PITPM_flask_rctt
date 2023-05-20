from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Jerry')


@app.route('/admin/')
def admin():
    if not loggedin:
        return redirect(url_for('login'))  # ��������������� �� �������� �����, ���� �� ���������
    return render_template('admin.html')


@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    # ��� ��������� ������� ������������
    return f"������� ������������: {user_id}"


@app.route('/books/<genre>/')
def books(genre):
    # ��� ��������� ���� �� �����
    return f"����� �� �����: {genre}"


if __name__ == '__main__':
    app.run()