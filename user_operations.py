
def check_user(connection, username):
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM auth_user WHERE username = %s;", (username,))
    check = cursor.fetchone()
    if not check:
        print('Такого пользователя не существует!')
    cursor.close()
    return check

def check_new_user(connection, new_username):
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM auth_user WHERE username = %s;", (new_username,))
    check_new = cursor.fetchone()
    if check_new:
        print('Такая копия уже есть!')
    cursor.close()
    return check_new

def copy_user(connection, username, new_username):
    cursor = connection.cursor()
    try:
        cursor.execute('''INSERT INTO auth_user
                    (username, first_name, last_name, email, password, is_staff, is_active, is_superuser, last_login, date_joined, groups, permissions, city_id, params, organization_id, position_type_id, middle_name, phone, sip, person_number, active_from, active_to, expirable, snils, deleted, last_login_esia, extra, can_edit_federal_roads, can_edit_municipal_roads, can_edit_regional_roads, can_edit_tyumen_roads, municipal_roads_all_districts, regional_roads_all_districts, can_edit_all_roads, settings, is_notificate, dispatching_id, password_datetime, password_change_next_login)
                        SELECT %s, 'Тест', last_name, email, password, is_staff, is_active, is_superuser, last_login, date_joined, groups, permissions, city_id, params, organization_id, position_type_id, middle_name, phone, sip, person_number, active_from, active_to, expirable, snils, deleted, last_login_esia, extra, can_edit_federal_roads, can_edit_municipal_roads, can_edit_regional_roads, can_edit_tyumen_roads, municipal_roads_all_districts, regional_roads_all_districts, can_edit_all_roads, settings, is_notificate, dispatching_id, password_datetime, password_change_next_login
                        FROM auth_user WHERE username = %s;''', (new_username, username,))
        cursor.execute("SELECT * FROM auth_user WHERE username = %s;", (new_username,))
        clone_success = cursor.fetchone()
    finally:
        cursor.close()
    return clone_success
