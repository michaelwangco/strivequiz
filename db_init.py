import sqlite3
from datetime import datetime
now = datetime.now()

con = sqlite3.connect('quiz.db')

cur = con.cursor()

# Create tables
cur.execute('''CREATE TABLE quiz (creationdate timestamp, quiz_id real, quiz_name text)''')
#(creationdate, quiz_id, quiz_name)
cur.execute("insert into quiz values (?, ?, ?)", (now, 1, "Basic Quiz Example"))

cur.execute('''CREATE TABLE quiz_questions (creationdate timestamp,
        prompt text, question_id real, quiz_id real)''')
#(creationdate, prompt, question_id, quiz_id)
cur.execute("insert into quiz_questions values (?, ?, ?, ?)", (now, "What date is today?", "1", "1"))
cur.execute("insert into quiz_questions values (?, ?, ?, ?)", (now, "What time is it now?", "2", "1"))

cur.execute('''CREATE TABLE question_response (creationdate timestamp,
        response_id real, quiz_response text, question_id real, quiz_id real)''')

# Insert a row of data
# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
