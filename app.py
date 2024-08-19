from flask import Flask, jsonify
import snowflake.connector

app = Flask(__name__)

def get_snowflake_connection():
    return snowflake.connector.connect(
        user='???????',
        password='??????',
        account='???????',
        warehouse='???????',
        database='SYSTEM_SERVICES',
        schema='ELASTICSEARCH'
    )

@app.route('/')
def home():
    return "Welcome to the Flask Snowflake App!"

@app.route('/logs/<log_level>')
def get_logs(log_level):
    conn = get_snowflake_connection()
    cursor = conn.cursor()

    query = f"SELECT TIMESTAMP, TASK_ID, MESSAGE FROM APPLICATION_LOGS WHERE LOG_LEVEL = '{log_level.upper()}'"
    cursor.execute(query)
    logs = cursor.fetchall()
    cursor.close()
    conn.close()


    formatted_logs = []
    for log in logs:
        formatted_logs.append({
            'timestamp': log[0],
            'task_id': log[1],
            'message': log[2]
        })

 
    return jsonify({log_level.upper(): formatted_logs})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
