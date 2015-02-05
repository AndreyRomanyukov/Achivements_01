from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, TIMESTAMP, BYTEA, TEXT, BOOLEAN

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.schema import DropConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
metadata = MetaData(bind=engine, schema='achivements')
Base = declarative_base(metadata=metadata)
Session = sessionmaker(bind=engine, expire_on_commit=True)


class Achivement(Base):
    __tablename__ = 'achivements'

    achivement_id = Column(INTEGER, primary_key=True)
    #achivement_time = Column(TIMESTAMP())
    #achivement_image = Column(BYTEA)
    achivement_title = Column(TEXT)
    achivement_description = Column(TEXT)
    achivement_xtimes = Column(INTEGER)
    achivement_progress_current = Column(INTEGER)
    achivement_progress_end = Column(INTEGER)
    achivement_done = Column(BOOLEAN)
    achivement_tag = Column(TEXT)


def drop_all():
    metadata.reflect()
    for table in metadata.tables.values():
        for fk in table.foreign_keys:
            engine.execute(DropConstraint(fk.constraint))
    metadata.drop_all()


def add_test_data():
    for i in range(10):
        test_data = Achivement()
        test_data.achivement_title = "title" + str(i)
        test_data.achivement_description = "description" + str(i)

        session = Session()
        try:
            session.add(test_data)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


def reset():
    print "DB reset started..."
    print "Drop all..."
    drop_all()
    print "Drop all done!"

    print "Create all..."
    Base.metadata.create_all()
    print "Create all done!"

    print "Add test data..."
    add_test_data()
    print "Add test data done!"
    print "DB reset done!"


def main():
    print "Hello world from db.py"


if __name__ == "__main__":
    main()