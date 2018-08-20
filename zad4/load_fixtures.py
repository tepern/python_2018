import db

fixtures_sql = '''
INSERT INTO pizza (id, title, price, ingredients) VALUES (1, "Pizza Margherita", "100 р.", "mushroom, mozzarella, tomato, black olives");
INSERT INTO pizza (id, title, price, ingredients) VALUES (2, "Pizza Napolitana", "200 р.", "mushroom, parmezan, tomato, black olives, basil");
INSERT INTO pizza (id, title, price, ingredients) VALUES (3, "Pizza Pepperoni", "220 р.", "mozzarella, tomato, pepperoni");
INSERT INTO pizza (id, title, price, ingredients) VALUES (4, "Pizza Hawaiian", "150 р.", "tomato, pineapples, mozzarella");

'''


def run():
    conn_new, cur_new = db.get_db()
    cur_new.executescript(fixtures_sql)
    conn_new.commit()

if __name__ == '__main__':
    run()
