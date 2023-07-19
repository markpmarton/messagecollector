from config import DB_CONN_STR

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine(DB_CONN_STR)

Base.prepare(autoload_with=engine)

User = Base.classes.app_user
Message = Base.classes.message
Type = Base.classes.type
