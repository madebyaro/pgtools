import sqlalchemy as db
import os

engine = db.create_engine('postgresql://user1:user1@localhost/mydb')

for root, directories, filenames in os.walk('/home/user1/pg1/bin'):
    for directory in directories:
        print(os.path.join(root, directory))
    for filename in filenames:
        print(os.path.join(root,filename))

metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)

files = db.Table('files', metadata, autoload=True, autoload_with=engine )
print(files.columns.keys)

user = Table('user', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)
