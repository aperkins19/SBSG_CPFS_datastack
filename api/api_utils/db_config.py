db_config = {
'hostname':'postgres_hostname',
'database':'default_database',
'username':'username',
'pwd':'password',
'port_id':5432
}

engine_string = 'postgresql://'+db_config['username']+':'+db_config['pwd']+'@'+db_config['hostname']+':'+str(db_config['port_id'])+'/'+db_config['database']