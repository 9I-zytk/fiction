import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123',
                             db='fiction',
                             charset='utf8')
cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)


def add_fiction(item):
    values = (
        item['upc'],
        item['name'],
        item['price'],
        item['review_rating'],
        item['review_num'],
        item['stock'],
    )
    sql = 'INSERT INTO books VALUES (%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, values)
    pass


def update_fiction(item):
    values = (
        item['upc'],
        item['name'],
        item['price'],
        item['review_rating'],
        item['review_num'],
        item['stock'],
    )
    sql = 'UPDATE books VALUES (%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, values)
    pass


def find_ficiton_by_name(item):
    sql = "SELECT recId FROM fiction WHERE title = '%s' and author = '%s'"
    values = (
        item['title'],
        item['author']
    )
    cursor.execute(sql, values)
    return cursor.fetchall()


def dis_connect():
    connection.close()
