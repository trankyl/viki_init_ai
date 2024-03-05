
# Pour créer un script Python qui analyse une zone d'atterrissage OCI (Oracle Cloud Infrastructure) et génère un rapport CSV contenant les détails de toutes les ressources,
# vous devrez utiliser le SDK OCI Python. Assurez-vous que le SDK est installé en exécutant pip install oci.

# Voici un script qui rassemble les informations requises et génère un rapport CSV :


#-------------------------------------------------------------- -----------------------------------------

import oci
import csv

import traceback

import mysql.connector

phost_mysql = "10.71.0.95"
puser = "admin"
ppwd = "Admincmdb2023$"
pdatabase = "cmdb"
port = 3306

config_bd_mysql = {
  'user': puser,
  'password': ppwd,
  'host': phost_mysql,
  'database': pdatabase ,
  'raise_on_warnings': True,
  'auth_plugin':'mysql_native_password'
}


def save_to_mysql_db() :
    
    global config_bd_mysql

    try:

        connection = mysql.connector.connect(**config_bd_mysql)
        
        cursor = connection.cursor()

        cursor.execute("select database();")

        db = cursor.fetchone()
        
        if db:
            print("You're connected to database: ", db)
        else:
            print('Not connected.')

        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        cursor.execute(sql, val)

        connection.commit()

        print(cursor.rowcount, "record inserted.")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return


def ajout_type_attribut_et_domaine_valeur(pliste_ressource) :
    global phost_mysql , puser , ppwd , pdatabase , port

    mydb = mysql.connector.connect( host=phost_mysql, database=pdatabase, user=puser, password=ppwd , auth_plugin='mysql_native_password' )
    
    index_colonne = 0 #index de colonne pour identifier le nm de la colonne en cours d'iération

    liste_nom_colonne = ['_display_name' , '_resource_type' , '_compartment_id'] 

    lnom_type_atribut = ''  #nom d'un type d'attribut

    for resource in pliste_ressource:
        
        index_colonne = index_colonne + 1 #passer a la colonne suivante
        lnom_type_atribut = ''

        if (index_colonne == 3) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne]
        else:
            continue

        mycursor = mydb.cursor()

        sql = "INSERT INTO type_attribut (nom_type_attr ) VALUES (%s)"
        val = (lnom_type_atribut)
        mycursor.execute(sql, val)

        mydb.commit()

    return

try:
    # set up config and create search client
    config = oci.config.from_file()
    search_client = oci.resource_search.ResourceSearchClient(config)
    
    #print(search_client.__dict__)
    # define query text and query
    query_text = "QUERY all resources where lifeCycleState != 'TERMINATED' && lifeCycleState != 'FAILED'"
    query = "QUERY all resources where lifeCycleState != 'TERMINATED' && lifeCycleState != 'FAILED'" 
    # create StructuredSearchDetails object and perform search query
    search_details = oci.resource_search.models.StructuredSearchDetails(query=query)

    search_lists = []
    search_response = search_client.search_resources(search_details=search_details)
    search_lists +=  search_response.data.items
    #next_page=None
    while search_response.next_page:
        search_response = search_client.search_resources(search_details=search_details, page=search_response.next_page)
        search_lists +=  search_response.data.items
 
    items =[]
    for resource in search_lists:
      
        items.append(vars(resource))
     
    print('Datatype ,Total Numbers of Ressources----->>>>> ',type(items), len(items))
    fields = ['_display_name', '_resource_type','_compartment_id', '_identity_context', '_identifier', 'attribute_map',
        '_availability_domain', '_additional_details', '_system_tags', '_defined_tags', '_lifecycle_state', 
        '_search_context',  '_freeform_tags', '_time_created', 'swagger_types']
    with open('oci_resources_report.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = fields)
        writer.writeheader()
        writer.writerows(items)
    
    print("OCI Resources report generated: oci_resources_report.csv")


    mydb = mysql.connector.connect( host=phost_mysql, database=pdatabase, user=puser, password=ppwd , auth_plugin='mysql_native_password' )

    mycursor = mydb.cursor()

    sql = "INSERT INTO ressource (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    

except:
# printing stack trace
 
 traceback.print_exc()

 
    
    