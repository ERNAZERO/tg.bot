import sqlite3
from phones_brand import getPhone, getDiscountItem

def fullToTable():
    try:
        conn = sqlite3.connect('softech_database.db')
        cursor = conn.cursor()

        iphoneModels = getPhone('https://softech.kg/phones/apple-smartphone/')

        dataInserting = "INSERT OR IGNORE INTO iphone (model, price, context, link, img) VALUES (?,?,?,?,?)"        
        
        for value_list in iphoneModels:
            cursor.execute(dataInserting, value_list)
        
        conn.commit()

    except sqlite3.Error as error:
        print('Error:', error)

    finally:
        if conn:
            conn.close()
            
    
# fullToTable()

# fullToTable()




def showModels(brand):
    try:
        conn = sqlite3.connect('softech_database.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT model FROM " +brand)
        rows = cursor.fetchall()
        spisok = []
        for row in rows:
            row = str(row)[11:-3]
            spisok.append(row)   
        return spisok
    except sqlite3.Error as error:
        print('Error:', error)

    finally:
        if conn:
            conn.close()


def getLink(brand):
    try:
        conn = sqlite3.connect('softech_database.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT link FROM " + brand)
        rows = cursor.fetchall()
        spisok = []
        for row in rows:
            row = str(row)[2:-3]
            spisok.append(row)   
        return spisok
    except sqlite3.Error as error:
        print('Error:', error)

    finally:
        if conn:
            conn.close()
        

def getPrice(brand):
    try:
        conn = sqlite3.connect('softech_database.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT price FROM " + brand)
        rows = cursor.fetchall()
        spisok = []
        for row in rows:
            row = str(row)[2:-3]
            spisok.append(row)
        return spisok
    except sqlite3.Error as error:
        print('Error:', error)

    finally:
        if conn:
            conn.close()
    



def check(brand, button):
    try:
        conn = sqlite3.connect('softech_database.db')
        cursor = conn.cursor()
        query = f"SELECT img FROM {brand} WHERE model = ?"
        cursor.execute(query, (button,))
        img = cursor.fetchone()
        # print(type(img))
        return str(img)[2:-3]
    except sqlite3.Error as error:
        print('Error:', error)

    finally:
        if conn:
            conn.close()
            
print(check('iphone', 'Смартфон Apple iPhone 14 128GB'))















 # nothingModels = getPhone('https://softech.kg/phones/nothing/')
        # realmeModels = getPhone('https://softech.kg/phones/oppo/')
        # xiaomiModels = getPhone('https://softech.kg/phones/xiaomiphones/')
        
        # discountItems = getDiscountItem()
        
        # dataInserting = "INSERT OR IGNORE INTO discount_items (model, price_new, price_old, price_sale, description, link) VALUES (?,?,?,?,?,?)"
        
        
        
        
        
        
        
        
        
                # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS xiaomi (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         model TEXT,
        #         price TEXT,
        #         context TEXT
        #     )
        # """)

        # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS iphone (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         model TEXT,
        #         price TEXT,
        #         context TEXT,
        #         link TEXT,
        #         img BLOB
        #     )
        # """)
        
        # cursor.execute("""
        #         CREATE TABLE IF NOT EXISTS nothing_phone (
        #             id INTEGER PRIMARY KEY AUTOINCREMENT,
        #             model TEXT,
        #             price TEXT, 
        #             context TEXT
        #         )
        #                """)

        # cursor.execute("""
        #         CREATE TABLE IF NOT EXISTS xiaomi (
        #             id INTEGER PRIMARY KEY AUTOINCREMENT,
        #             model TEXT,
        #             price TEXT, 
        #             context TEXT,
        #             link TEXT
        #         )
        #                """)
