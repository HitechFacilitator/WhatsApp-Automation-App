from model.db import Session, Message, Status, ScheduledOperation
# import sqlite3

def getAllStatus():
    session = Session()
    allStatus = session.query(Status).all()
    return allStatus


def getAllMessages():
    session = Session()
    allMessages = session.query(Message).all()
    return allMessages

def getAllScheduleOps():
    session = Session()
    allScheduleOps = session.query(ScheduledOperation).all()
    return allScheduleOps

def getMessageCurrentStatus(msg):
    session = Session()
    allScheduleOps = session.query(ScheduledOperation).all()
    for scheduleOp in allScheduleOps:
        if scheduleOp.message_id == msg.id:
            return scheduleOp.current_status

def getStatusCurrentStatus(sts):
    session = Session()
    allScheduleOps = session.query(ScheduledOperation).all()
    for scheduleOp in allScheduleOps:
        if scheduleOp.message_id == sts.id:
            return scheduleOp.current_status


# def get_all_records(table_name):
#     # Connect to the SQLite database
#     conn = sqlite3.connect('model/whatsapp_automation.db')  # Path to your SQLite database file
#     cursor = conn.cursor()
    
#     try:
#         # Query to fetch all records
#         query = f"SELECT * FROM {table_name}"
#         cursor.execute(query)
        
#         # Fetch all rows
#         rows = cursor.fetchall()
        
#         # Print column names
#         column_names = [description[0] for description in cursor.description]
#         print(f"Columns: {', '.join(column_names)}")
        
#         # Display the rows
#         for row in rows:
#             print(row)
#     except sqlite3.Error as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Close the database connection
#         conn.close()

# Example usage
# get_all_records('AutomatedMessages')  # Replace with your table name

