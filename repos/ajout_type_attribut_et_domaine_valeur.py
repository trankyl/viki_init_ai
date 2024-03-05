
# Pour créer un script Python qui analyse une zone d'atterrissage OCI (Oracle Cloud Infrastructure) et génère un rapport CSV contenant les détails de toutes les ressources,
# vous devrez utiliser le SDK OCI Python. Assurez-vous que le SDK est installé en exécutant pip install oci.

# Voici un script qui rassemble les informations requises et génère un rapport CSV :


#-------------------------------------------------------------- -----------------------------------------

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



def ajout_type_attribut_et_domaine_valeur(pliste_ressource) :
    global phost_mysql , puser , ppwd , pdatabase , port

    
    
    index_colonne = 0 #index de colonne pour identifier le nm de la colonne en cours d'iération

    liste_nom_colonne = ['_display_name', '_resource_type','_compartment_id', '_identity_context', '_identifier', 'attribute_map',
            '_availability_domain', '_additional_details', '_system_tags', '_defined_tags', '_lifecycle_state', 
            '_search_context',  '_freeform_tags', '_time_created', 'swagger_types']

    lnom_type_atribut = ''  #nom d'un type d'attribut

    if ( len (pliste_ressource) == 0) : 
       return

    mydb = mysql.connector.connect( host=phost_mysql, database=pdatabase, user=puser, password=ppwd , auth_plugin='mysql_native_password' )

    for resource in liste_nom_colonne:
        
        index_colonne = index_colonne + 1 #passer a la colonne suivante
        lnom_type_atribut = ''

        if (index_colonne == 3) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1]
        elif (index_colonne == 5) : 
            lnom_type_atribut = 'ocid' #liste_nom_colonne[index_colonne-1]
        elif (index_colonne == 7) : 
            lnom_type_atribut = 'domaine_disponibilite' #liste_nom_colonne[index_colonne-1]
        if (index_colonne == 9) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_system_tags
        if (index_colonne == 10) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_defined_tags
        if (index_colonne == 11) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_lifecycle_state
        if (index_colonne == 13) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_freeform_tags
        if (index_colonne == 14) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_time_created
        else:
            continue

        #sql = "INSERT INTO type_attribut (nom_type_attr ) VALUES (%s)"
        #val = (lnom_type_atribut)

        sql = "INSERT INTO type_attribut (nom_type_attr ) VALUES ('" + lnom_type_atribut + "')"

        print("INSERT INTO type_attribut (nom_type_attr ) VALUES ('" + lnom_type_atribut + "')")

        mycursor = mydb.cursor() #pat++
        
        #mycursor.execute(sql, val) #pat++
        mycursor.execute(sql)

        mydb.commit() #pat++

        print(mycursor.rowcount, "record inserted.")

        print("1 record inserted, ID:", mycursor.lastrowid)

    return


def populate_table_type_attribut() :
    global phost_mysql , puser , ppwd , pdatabase , port

    
    
    index_colonne = 0 #index de colonne pour identifier le nm de la colonne en cours d'iération

    liste_nom_colonne = ['_display_name', '_resource_type','_compartment_id', '_identity_context', '_identifier', 'attribute_map',
            '_availability_domain', '_additional_details', '_system_tags', '_defined_tags', '_lifecycle_state', 
            '_search_context',  '_freeform_tags', '_time_created', 'swagger_types']

    lnom_type_atribut = ''  #nom d'un type d'attribut

    if ( len (liste_nom_colonne) == 0) : 
       return

    mydb = mysql.connector.connect( host=phost_mysql, database=pdatabase, user=puser, password=ppwd , auth_plugin='mysql_native_password' )

    for resource in liste_nom_colonne:
        
        index_colonne = index_colonne + 1 #passer a la colonne suivante
        lnom_type_atribut = ''

        if (index_colonne == 3) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1]
        elif (index_colonne == 5) : 
            lnom_type_atribut = 'ocid' #liste_nom_colonne[index_colonne-1]
        elif (index_colonne == 7) : 
            lnom_type_atribut = 'domaine_disponibilite' #liste_nom_colonne[index_colonne-1]
        if (index_colonne == 9) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_system_tags
        if (index_colonne == 10) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_defined_tags
        if (index_colonne == 11) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_lifecycle_state
        if (index_colonne == 13) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_freeform_tags
        if (index_colonne == 14) : 
            lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_time_created
        else:
            continue

        #sql = "INSERT INTO type_attribut (nom_type_attr ) VALUES (%s)"
        #val = (lnom_type_atribut)

        sql = "INSERT INTO type_attribut (nom_type_attr ) VALUES ('" + lnom_type_atribut + "')"

        print("INSERT INTO type_attribut (nom_type_attr ) VALUES ('" + lnom_type_atribut + "')")

        mycursor = mydb.cursor() #pat++
        
        #mycursor.execute(sql, val) #pat++
        mycursor.execute(sql)

        mydb.commit() #pat++

        print(mycursor.rowcount, "record inserted.")

        print("1 record inserted, ID:", mycursor.lastrowid)

    return


try:
   
   #liste_ressource = "test.vcncmpproddbcam.oraclevcn.com;CustomerDnsZone;ocid1.compartment.oc1..aaaaaaaa4yqsiipgbcn43ymekt7wtqrgzzug2rra7unddv3hgivka4ns6riq;{};ocid1.dns-zone.oc1.ca-toronto-1.aaaaaaaadasnsw4xzcfzcdspyw4augiajgniogmlsiqhp5cquffmbrlybqdq;{'resource_type': 'resourceType', 'identifier': 'identifier', 'compartment_id': 'compartmentId', 'time_created': 'timeCreated', 'display_name': 'displayName', 'availability_domain': 'availabilityDomain', 'lifecycle_state': 'lifecycleState', 'freeform_tags': 'freeformTags', 'defined_tags': 'definedTags', 'system_tags': 'systemTags', 'search_context': 'searchContext', 'identity_context': 'identityContext', 'additional_details': 'additionalDetails'};;{};{};{'Oracle-Tags': {'CreatedBy': 'default/stephane.kengne-ext@mcn.gouv.qc.ca', 'CreatedOn': '2023-05-04T16:42:17.539Z'}};ACTIVE;;{};2023-05-04 16:42:18.457000+00:00;{'resource_type': 'str', 'identifier': 'str', 'compartment_id': 'str', 'time_created': 'datetime', 'display_name': 'str', 'availability_domain': 'str', 'lifecycle_state': 'str', 'freeform_tags': 'dict(str, str)', 'defined_tags': 'dict(str, dict(str, object))', 'system_tags': 'dict(str, dict(str, object))', 'search_context': 'SearchContext', 'identity_context': 'dict(str, object)', 'additional_details': 'dict(str, object)'};;".split(';')

   #ajout_type_attribut_et_domaine_valeur(liste_ressource)

   populate_table_type_attribut()

except:

 
 traceback.print_exc()

 
    
    