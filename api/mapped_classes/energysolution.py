from sqlalchemy.orm import declarative_base
from sqlalchemy import  Column, Integer, String, Float, Boolean
from sqlalchemy.sql.expression import  text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from dataclasses import dataclass

from flask_restful import reqparse, fields, marshal_with

Base = declarative_base()

@dataclass
class People(Base):
    __tablename__ = "basic_table"

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Likes = Column(String)

    def __init__(self,id, Name, Likes):
        self.id=id
        self.Name = Name
        self.Likes = Likes




@dataclass
class EnergySolution(Base):

    ############## defines the model

     __tablename__ = "energy_solution_table"

     #BATCH MetaData

     id = Column(Integer, primary_key=True)

     # the unique word acts a human readable unique key for personal reference and usage as a foreign key
     Unique_Word = Column("Unique_Word", String, unique=True, nullable=False)

     # exhausted
     Exhausted = Column("Exhausted", Boolean, server_default="False",nullable=False)

     Maker = Column("Maker",String, nullable=False)
     Date_batch_made = Column("Date_batch_made",String, nullable=False)

     # time stamp uses a function to automatically enter the time of the record entry
     Database_TimeStamp = Column(TIMESTAMP(timezone=True),
                                                        nullable=False, server_default=text("now()"))

     Description = Column("Description",String, nullable=False)
     XTimes = Column("XTimes",String, nullable=False)

     #Concentrations
     K_Glut = Column("K_glut",Float, nullable=False)
     Mg_Glut = Column("Mg_Glut",Float, nullable=False)
     Tris_Base = Column("Tris_Base",Float, nullable=False)
     DTT = Column("DTT",Float, nullable=False)
     Amino_Acids = Column("Amino Acids",Float, nullable=False)
     Tyrosine = Column("Tyrosine",Float, nullable=False)
     CoA = Column("CoA",Float, nullable=False)
     NAD = Column("NAD",Float, nullable=False)
     Folinic_Acid = Column("Folinic Acid",Float, nullable=False)
     cAMP = Column("cAMP",Float, nullable=False)
     Three_PGA = Column("3PGA",Float, nullable=False)
     HEPES = Column("HEPES",Float, nullable=False)
     Spermidine = Column("Spermidine",Float, nullable=False)
     PEG_8000 = Column("PEG 8000",Float, nullable=False)
     tRNA = Column("tRNA",Float, nullable=False)

     ATP = Column("ATP",Float, nullable=False)
     GTP = Column("GTP",Float, nullable=False)
     CTP = Column("CTP",Float, nullable=False)
     UTP = Column("UTP",Float, nullable=False)

     def __init__(self, Maker,Unique_Word,Date_batch_made,Description,XTimes,K_Glut, Mg_Glut, Tris_Base, DTT, Amino_Acids, Tyrosine, CoA, NAD, Folinic_Acid, cAMP, Three_PGA, HEPES,Spermidine,PEG_8000,tRNA,ATP,GTP,CTP,UTP):

         #defines what data is required inorder to make a new record
         self.Maker = Maker
         self.Unique_Word = Unique_Word
         self.Date_batch_made = Date_batch_made
         self.XTimes = XTimes
         self.Description = Description

         self.K_Glut = K_Glut
         self.Mg_Glut = Mg_Glut
         self.Tris_Base = Tris_Base
         self.DTT = DTT
         self.Amino_Acids = Amino_Acids
         self.Tyrosine = Tyrosine
         self.CoA = CoA
         self.NAD = NAD
         self.Folinic_Acid = Folinic_Acid
         self.cAMP = cAMP
         self.Three_PGA = Three_PGA
         self.HEPES = HEPES
         self.Spermidine = Spermidine
         self.PEG_8000 = PEG_8000
         self.tRNA = tRNA
         self.ATP = ATP
         self.GTP = GTP
         self.CTP = CTP
         self.UTP = UTP


energysolution_fields = {

"Maker":fields.String,
"Unique_Word":fields.String,
"Date_batch_made":fields.String,
"XTimes":fields.Float,
"Description":fields.String,
"K_Glut":fields.Float,
"Mg_Glut":fields.Float,
"Tris_Base":fields.Float,
"DTT":fields.Float,
"Amino_Acids":fields.Float,
"Tyrosine":fields.Float,
"CoA":fields.Float,
"NAD":fields.Float,
"Folinic_Acid":fields.Float,
"cAMP":fields.Float,
"Three_PGA":fields.Float,
"HEPES":fields.Float,
"Spermidine":fields.Float,
"PEG_8000":fields.Float,
"tRNA":fields.Float,
"ATP":fields.Float,
"GTP":fields.Float,
"CTP":fields.Float,
"UTP":fields.Float

}


# this parser and its arguments is for parsing the raw json sent in the CRUDs into a usable python object
energy_solution_args = reqparse.RequestParser()
energy_solution_args.add_argument("Maker", type=str, help="Problem withName of the maker")
energy_solution_args.add_argument("Unique_Word", type=str, help="Problem with the Unique_Word")
energy_solution_args.add_argument("Date_batch_made", type=str, help="Problem with Date_batch_made give")
energy_solution_args.add_argument("Description", type=str, help="Problem with Description")

energy_solution_args.add_argument("XTimes", type=float, help="Problem with XTimes")

energy_solution_args.add_argument("K_Glut", type=float, help="Problem with K_Glut conc")
energy_solution_args.add_argument("Mg_Glut", type=float, help="Problem with Mg_Glut conc")
energy_solution_args.add_argument("Tris_Base", type=float, help="Problem with Tris_Base conc")
energy_solution_args.add_argument("DTT", type=float, help="Problem with DTT conc")
energy_solution_args.add_argument("Amino_Acids", type=float, help="Problem with Amino_Acids conc")
energy_solution_args.add_argument("Tyrosine", type=float, help="Problem with Tyrosine conc")
energy_solution_args.add_argument("CoA", type=float, help="Problem with CoA conc")
energy_solution_args.add_argument("NAD", type=float, help="Problem with NAD conc")
energy_solution_args.add_argument("Folinic_Acid", type=float, help="Problem with Folinic_Acid conc")
energy_solution_args.add_argument("cAMP", type=float, help="Problem with cAMP conc")
energy_solution_args.add_argument("Three_PGA", type=float, help="Problem with Three_PGA conc")
energy_solution_args.add_argument("HEPES", type=float, help="Problem with HEPES conc")
energy_solution_args.add_argument("Spermidine", type=float, help="Problem with Spermidine conc")

energy_solution_args.add_argument("PEG_8000", type=float, help="Problem with PEG_8000 conc")
energy_solution_args.add_argument("tRNA", type=float, help="Problem with tRNA conc")
energy_solution_args.add_argument("ATP", type=float, help="Problem with ATP conc")
energy_solution_args.add_argument("GTP", type=float, help="Problem with GTP conc")
energy_solution_args.add_argument("CTP", type=float, help="Problem with CTP conc")
energy_solution_args.add_argument("UTP", type=float, help="Problem with UTP conc")
