from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.route("/books", methods=["GET"])
def fetch_books():
    try:
        connection = psycopg2.connect(user="user",
                                      password="12345678",
                                      host="0.0.0.0",
                                      port="5000",
                                      database="database1")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from books"

        cursor.execute(postgreSQL_select_Query)
        book_records = cursor.fetchall()

        books = []
        for row in book_records:
            id = row[0]
            title = row[1]
            description = row[2]
            price = row[3]
            date_add = row[4]
            status = row[5]

            book = {"id": id, "title": title, "description": description, "price": price, "date_add": date_add, "status": status}
            books.append(book)

        return jsonify(books)

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    app.run()