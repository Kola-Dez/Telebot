import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()
# если нет то будет автоматически создаваться если есть то подключается
# создание таблицы если существует то не создаем(передаем атребуты-+)
    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo TEXT, age TEXT, description TEXT, name TEXT)")
# Завершаем операцию
    db.commit()

# Создание профиля пользователя
async def create_profile(user_id):
    # Если пользователь уже создан то мыв его возвращяем в переменную user
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key = user_id)).fetchone()
    # Если пользователя несуществует то user вернет none
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?)",(user_id, '', '', '', ''))
        db.commit()


# профиль заполненый
# состояние и индификатор
async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET photo = '{}', age = '{}', description = '{}', name = '{}' WHERE user_id == '{}' ".format(
            data['photo'], data['age'], data['description'], data['name'], user_id ))
        db.commit()