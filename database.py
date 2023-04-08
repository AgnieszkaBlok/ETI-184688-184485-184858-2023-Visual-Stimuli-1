import os
from sqlalchemy import create_engine, text 

db_connection_string = os.environ['db_connection_string']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

#with engine.connect() as conn:
 # result = conn.execute(text("select * from interviewee"))
  #print(result.all())

def add_into_file(interviewee): 
  with engine.connect() as conn:
    query = text("INSERT INTO interviewee (gender, age) VALUES (:gender, :age)")
    conn.execute(query, {'gender':interviewee['gender'], 
                         'age':interviewee['age']})