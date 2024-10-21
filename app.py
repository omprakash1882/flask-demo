from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)
db_config = {
    'user': 'root',
    'password': '(lIJKHLQ,]REeYoq',
    'host': '34.56.18.90',
    'database': 'summary-db'
}
def create_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    summary = request.form['summary']

    conn = create_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO summaries (email, summary) VALUES (%s, %s)"
    cursor.execute(query, (email, summary))
    conn.commit()
    cursor.close()
    conn.close()

    return "Data submitted successfully!"

@app.route('/summaries', methods=['GET'])
def get_summaries():
    conn = create_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM summaries")
    data = cursor.fetchall()    
    cursor.close()
    conn.close()

    return jsonify(data)

@app.route('/summaries/<int:id>', methods=['PATCH'])
def update_summary(id):
    conn = create_db_connection()
    cursor = conn.cursor()

    new_summary = request.json['summary']
    query = "UPDATE summaries SET summary = %s WHERE id = %s"
    cursor.execute(query, (new_summary, id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Summary updated successfully"})


@app.route('/summaries/<int:id>', methods=['DELETE'])
def delete_summary(id):
    conn = create_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM summaries WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Summary deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
