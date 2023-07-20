from config import DB_CONN_STR

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine

# for simplicity I used Db-first auto-mapping
Base = automap_base()

engine = create_engine(DB_CONN_STR)

Base.prepare(autoload_with=engine)

# The app_user table contains the properties of the customer (e.g. customerId)
User = Base.classes.app_user
# The massage table stores the properties of the collected message objects. Used later in the statprovider.
Message = Base.classes.message
# The type table contains the previously used message types.
Type = Base.classes.type
