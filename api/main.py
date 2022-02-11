from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, marshal_with, fields

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2
import json
import pandas as pd

from api_utils.db_config import *
from api_utils.my_functions import *

from mapped_classes.energysolution import *
from mapped_classes.amplicons import *


# initialise flask app and api
api_app = Flask(__name__)
api = Api(api_app)

# connect to database
try:
    engine = sqlalchemy.create_engine(engine_string)
    print("Connected to database with: "+engine_string)

except Exception as error:
    print("failed to connect to database with connection string: "+engine_string)
    print("Error: ", error)

# create the session maker
Session = sessionmaker(autocommit=False, autoflush = False, bind=engine)

# automatically initialise tables
conn = engine.connect()
Base.metadata.create_all(engine)
conn.close()


class Amplicons(Resource):
    @marshal_with(amplicons_fields)
    def get(self):
        """ This function gets all of the amplicons in the table """
        # check if table exists
        insp = sqlalchemy.inspect(engine)
        # if the table doesn't exist, abort
        if insp.has_table("amplicons_table") != True:
            abort()

        # new session
        local_session = Session(bind=engine)
        ESs = local_session.query(Amplicon).all()
        local_session.close()

        return ESs

    @marshal_with(amplicons_fields)
    def post(self):
        """ Puts a single energy solution into the table """
        # parse the args using the parser defined in energysolution.py
        args = amplicons_args.parse_args()
        #start a new session
        local_session = Session(bind=engine)

        # define new energysolution
        new_es = Amplicon(
        Maker=args['Maker'],
        Unique_Word=args['Unique_Word'],
        Date_batch_made=args['Date_batch_made'],
        Description=args['Description'],
        Template_Seq = args['Template_Seq'],
        Forward_Primer_Seq = args['Forward_Primer_Seq'],
        Reverse_Primer_Seq = args['Reverse_Primer_Seq']
        )

        local_session.add(new_es)
        local_session.commit()
        local_session.refresh(new_es)
        local_session.close()


        return {"Server:": "Amplicon Added."}

class EnergySolutions(Resource):
    @marshal_with(energysolution_fields)
    def get(self):
        """ This function gets all of the energy solutions in the table """
        # check if table exists
        insp = sqlalchemy.inspect(engine)
        # if the table doesn't exist, abort
        if insp.has_table("energy_solution_table") != True:
            abort()

        # new session
        local_session = Session(bind=engine)
        ESs = local_session.query(EnergySolution).all()
        local_session.close()

        return ESs

    @marshal_with(energysolution_fields)
    def post(self):
        """ Puts a single energy solution into the table """
        # parse the args using the parser defined in energysolution.py
        args = energy_solution_args.parse_args()
        #start a new session
        local_session = Session(bind=engine)


        # define new energysolution
        new_es = EnergySolution(
        Maker=args['Maker'],
        Unique_Word=args['Unique_Word'],
        Date_batch_made=args['Date_batch_made'],
        XTimes=args['XTimes'],
        Description=args['Description'],
        K_Glut=args['K_Glut'],
        Mg_Glut=args['Mg_Glut'],
        Tris_Base=args['Tris_Base'],
        DTT=args['DTT'],
        Amino_Acids=args['Amino_Acids'],
        Tyrosine=args['Tyrosine'],
        CoA=args['CoA'],
        NAD=args['NAD'],
        Folinic_Acid=args['Folinic_Acid'],
        cAMP=args['cAMP'],
        Three_PGA=args['Three_PGA'],
        HEPES=args['HEPES'],
        Spermidine=args['Spermidine'],
        PEG_8000=args['PEG_8000'],
        tRNA=args['tRNA'],
        ATP=args['ATP'],
        GTP=args['GTP'],
        CTP=args['CTP'],
        UTP=args['UTP']
        )


        local_session.add(new_es)
        local_session.commit()
        local_session.refresh(new_es)
        local_session.close()


        return {"Server:": "Energy Sol Added."}

api.add_resource(EnergySolutions, "/energysolutions/")
api.add_resource(Amplicons, "/amplicons/")

if __name__ == "__main__":
    api_app.run(host="0.0.0.0", port=4000, debug=True)
