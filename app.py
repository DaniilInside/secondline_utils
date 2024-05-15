from flask import Flask, render_template, request, flash
from database import connect_db_rnis_to, connect_db_avtovokzal
from user_operations import check_user, copy_user, check_new_user

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/copy_user', methods=['POST'])
def copy_user_route():
    choice = int(request.form['choice'])
    username = request.form['username']
    new_username = request.form['new_username']

    if choice == 1:
        connection = connect_db_rnis_to()
    elif choice == 2:
        connection = connect_db_avtovokzal()
    else:
        return 'Неверный выбор!'

    check = check_user(connection, username)
    check_new = check_new_user(connection, new_username)

    if check and not check_new:
        clone_success = copy_user(connection, username, new_username)
        if clone_success:
            return 'Копирование успешно!'
        else:
            return 'Ошибка при копировании!'
    else:
        return 'Такого пользователя не существует или такая копия уже есть'

if __name__ == "__main__":
    app.run(debug=True)
