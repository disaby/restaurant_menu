import sqlite3 as sql
from create_bot import bot


def sqlite_start():
    global sqlite, cursor
    sqlite = sql.connect('database.db')
    cursor = sqlite.cursor()
    if sqlite:
        print("Database connected!")
    sqlite.execute(
        "CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)"
    )
    sqlite.execute(
        "CREATE TABLE IF NOT EXISTS admins(id TEXT PRIMARY KEY, username TEXT)"
    )
    sqlite.commit()


async def add_moder(id, name):
    cursor.execute("INSERT INTO admins VALUES (?,?)", (
        id,
        name,
    ))
    sqlite.commit()


async def get_moders_db():
    return cursor.execute("SELECT id FROM admins").fetchall()


async def sqlite_upload(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES (?,?,?,?)",
                       tuple(data.values()))
        sqlite.commit()


async def sqlite_read(message):
    for ret in cursor.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(
            message.from_user.id, ret[0],
            f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')


async def sqlite_read2():
    return cursor.execute('SELECT * FROM menu').fetchall()


async def sqlite_delete(name):
    cursor.execute('DELETE FROM menu WHERE name == ?', (name, ))
    sqlite.commit()
