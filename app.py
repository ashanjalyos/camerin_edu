import pymysql

# STEP 1: Database Connection

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Ashanjali@toppy0621',
    database='camerin_students',
    port=3306
)

print("Mysql connection successful")

try:
    # STEP 2: Create Cursor

    with connection.cursor() as cursor:

        # STEP 3: SQL Query

        query = """
            SELECT * FROM students
            WHERE city = 'kochi'
        """

        # STEP 4: Execute Query

        cursor.execute(query)

        # STEP 5: Fetch All Records

        result = cursor.fetchall()

        # STEP 6: Print Result

        print("Student Records")

        for record in result:
            print(record)

except Exception as e:
    print("Something went wrong:", e)

finally:
    connection.close()
    print("Operation completed")