from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgrebenny:B3nnychin@140.112.64.62:5432/postgres')
Base = declarative_base(engine)

Session = sessionmaker(bind=engine)
session = Session()

"""
# Tom 17/05/2012

# Example GeoAlchemy script.

from sqlalchemy import create_engine, distinct, func, MetaData, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry

# Database connection
engine = create_engine('postgresql://postgres:password@\
ip.address/database', echo=False)
Base = declarative_base(engine)

def make_link_line(point_geom, line_geom):
    '''Takes point and line PostGIS geometry, returns a new geom 
    representing shortest line between point and line.'''
    
    new_geom = func.ST_AsText(func.ST_MakeLine(point_geom, 
        func.ST_Line_Interpolate_Point(line_geom, 
            func.ST_Line_Locate_point(line_geom, point_geom))))
    
    return new_geom

class Roads(Base):
    """Mapping for roads data (existing table)"""
    __tablename__ = 'roads'
    __table_args__ = {'autoload':True}
    
class Stations(Base):
    """Mapping for stations data (existing table)"""
    __tablename__ = 'stations'
    __table_args__ = {'autoload':True}

def loadSession():
    """
    Helper class to load the database constructs via SQLAlchemy
    """ 
    # Prepare the session to be returned
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
    
if __name__ == "__main__":
    
    session = loadSession()

    # Return the geometry of line between station and closest point on road network
    for row in session.query(Stations.pkey.label('station'), 
        Roads.gid.label('road'), 
        make_link_line(Stations.the_geom, Roads.the_geom).\
            label('the_geom')).\
        order_by(Stations.pkey, 
            func.ST_Distance(Roads.the_geom, Stations.the_geom)).\
        distinct(Stations.pkey):
         
         print row.station, row.road, row.the_geom
"""