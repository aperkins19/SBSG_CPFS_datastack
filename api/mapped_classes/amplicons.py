from sqlalchemy.orm import declarative_base
from sqlalchemy import  Column, Integer, String, Float, Boolean
from sqlalchemy.sql.expression import  text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from dataclasses import dataclass

from flask_restful import reqparse, fields, marshal_with

Base = declarative_base()


@dataclass
class Amplicon(Base):

    ############## defines the model
     __tablename__ = "amplicons_table"

     #BATCH MetaData
     id = Column(Integer, primary_key=True)

     # the unique word acts a human readable unique key for personal reference and usage as a foreign key
     Unique_Word = Column("Unique_Word", String, unique=True, nullable=False)

     Maker = Column("Maker",String, nullable=False)
     Date_batch_made = Column("Date_batch_made",String, nullable=False)

     # time stamp uses a function to automatically enter the time of the record entry
     Database_TimeStamp = Column(TIMESTAMP(timezone=True),
                                                        nullable=False, server_default=text("now()"))

     Description = Column("Description",String)
     Template_Seq = Column("Template_Seq",String, nullable=False)
     Forward_Primer_Seq = Column("Forward_Primer_Seq",String, nullable=False)
     Reverse_Primer_Seq = Column("Reverse_Primer_Seq",String, nullable=False)


     def __init__(self, Maker,Unique_Word,Date_batch_made,Description, Template_Seq, Forward_Primer_Seq, Reverse_Primer_Seq):

         #defines what data is required inorder to make a new record
         self.Unique_Word = Unique_Word
         self.Maker = Maker
         self.Date_batch_made = Date_batch_made
         self.Description = Description
         self.Template_Seq = Template_Seq
         self.Forward_Primer_Seq = Forward_Primer_Seq
         self.Reverse_Primer_Seq = Reverse_Primer_Seq



amplicons_fields = {

"Maker":fields.String,
"Unique_Word":fields.String,
"Date_batch_made":fields.String,
"Description":fields.String,
"Template_Seq":fields.String,
"Forward_Primer_Seq":fields.String,
"Reverse_Primer_Seq":fields.String
}


# this parser and its arguments is for parsing the raw json sent in the CRUDs into a usable python object
amplicons_args = reqparse.RequestParser()
amplicons_args.add_argument("Maker", type=str, help="Problem withName of the maker")
amplicons_args.add_argument("Unique_Word", type=str, help="Problem with the Unique_Word")
amplicons_args.add_argument("Date_batch_made", type=str, help="Problem with Date_batch_made give")
amplicons_args.add_argument("Description", type=str, help="Problem with Description")

amplicons_args.add_argument("Template_Seq", type=str, help="Problem with Template_Seq")
amplicons_args.add_argument("Forward_Primer_Seq", type=str, help="Problem with Forward_Primer_Seq")
amplicons_args.add_argument("Reverse_Primer_Seq", type=str, help="Problem with Reverse_Primer_Seq")
