import cx_Oracle
import oracledb
import json
import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from .constants import BRANCHES

base_dir = settings.BASE_DIR

with open(os.path.join(base_dir, 'secrets.json')) as secret_file:
    secrets = json.load(secret_file)

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured(f"Set the {setting} setting")
    


def conndb():
    try:
        oracledb.init_oracle_client()
        cp = oracledb.ConnectParams()
        cp.parse_connect_string("152.67.34.112:1521/orapdb1.subnetprax02.vcnpraxioocisp0.oraclevcn.com")
        connection = oracledb.connect(user="CONSULTA142", password="BORA241", params=cp)
    except Exception as e:
        print(e)
        raise e
    else:
        return connection

    
def dictfetchall(cursor):
    #Return all rows from a cursor as a dict
    columns = [col[0].lower() for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_branch(company, branch):
    branch_name = BRANCHES.get(company, {}).get(branch)
    return branch_name
