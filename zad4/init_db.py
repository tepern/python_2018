import db

schema_sql = '''
DROP TABLE IF EXISTS pizza;
DROP TABLE IF EXISTS orders;

CREATE TABLE pizza (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT UNIQUE NOT NULL,
  price TEXT,
  ingredients TEXT  
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP(18) NOT NULL,
  pizza_id INTEGER NOT NULL,
  client TEXT NOT NULL,
  phone TEXT NOT NULL,
  address TEXT NOT NULL,
  status TEXT NOT NULL
);

'''


def run():
    conn_new, cur_new = db.get_db()
    cur_new.executescript(schema_sql)


if __name__ == '__main__':
    run()
