import traceback

class PopulateTable():
        
    def populate_table_type_attribut(liste_nom_colonne , pvider_table) :
        global phost_mysql , puser , ppwd , pdatabase , port

        try:
            
            index_colonne = 0 #index de colonne pour identifier le nm de la colonne en cours d'iération

            

            lnom_type_atribut = ''  #nom d'un type d'attribut

            if ( len (liste_nom_colonne) == 0) : 
                return

            mydb = mysql.connector.connect( host=phost_mysql, database=pdatabase, user=puser, password=ppwd , auth_plugin='mysql_native_password' )

            
            if (pvider_table) :
                print("vidage table type_attribut")
                sql = "TRUNCATE TABLE `type_attribut`"
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                mydb.commit()
                print("table type_attribut videe")

            for resource in liste_nom_colonne:
                
                index_colonne = index_colonne + 1 #passer a la colonne suivante
                lnom_type_atribut = ''

                if (index_colonne == 3) : 
                    lnom_type_atribut = liste_nom_colonne[index_colonne-1]
                elif (index_colonne == 5) : 
                    lnom_type_atribut = 'ocid' #liste_nom_colonne[index_colonne-1]
                elif (index_colonne == 7) : 
                    lnom_type_atribut = 'domaine_disponibilite' #liste_nom_colonne[index_colonne-1]
                elif (index_colonne == 9) : 
                    lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_system_tags
                elif (index_colonne == 10) : 
                    lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_defined_tags
                elif (index_colonne == 11) : 
                    lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_lifecycle_state
                elif (index_colonne == 13) : 
                    lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_freeform_tags
                elif (index_colonne == 14) : 
                    lnom_type_atribut = liste_nom_colonne[index_colonne-1] #_time_created
                else:
                    continue


                sql = "INSERT INTO type_attribut (nom_type_attr ) VALUES ('" + lnom_type_atribut + "')"

                print("INSERT INTO type_attribut (nom_type_attr ) VALUES ('" + lnom_type_atribut + "')")

                mycursor = mydb.cursor()
                
                mycursor.execute(sql)

                mydb.commit()

                print(mycursor.rowcount, "record inserted.")

                print("1 record inserted, ID:", mycursor.lastrowid)

        except:

          traceback.print_exc()

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")

        return
    

    def populate_table_attribut_ressource(pvaleur_attribut , pnom_type_attribut , pocid_ressource , pdateheure_attr , mydb) :

        #obtenir l,ID associé au nom de type attribut
        print("Obtenir ID associé au nom de type attribut : " + pnom_type_attribut)
        sql = "select id_type_attr from type_attribut where nom_type_attr = '" + pnom_type_attribut + "'"
        print(sql)
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        row = mycursor.fetchone()
        
        lid_type_attribut = row[0]
        print("ID type attribut est : " + str(lid_type_attribut))

        sql = "INSERT INTO attribut ( valeur_attr , id_type_attr  , ocid_res  , dateheure_attr) VALUES ("
        sql = sql + "'" + pvaleur_attribut + "'"
        sql = sql + ", " + str(lid_type_attribut) + ""
        sql = sql + ", '" + pocid_ressource + "'"
        sql = sql + ", '" + pdateheure_attr + "'"
        sql = sql + ")"

        print(sql)

        mycursor = mydb.cursor()
            
        mycursor.execute(sql)

        mydb.commit()

        print("1 record inserted, ID:", mycursor.lastrowid)

        return

    def populate_table_ressource(pliste_ressource , liste_nom_colonne , pvider_table) :
        global phost_mysql , puser , ppwd , pdatabase , port

        try:

            
            index_colonne = 0 #index de colonne pour identifier le nm de la colonne en cours d'iération

            lnom_type_atribut = ''  #nom d'un type d'attribut

            if ( len (pliste_ressource) == 0) : 
                return

            mydb = mysql.connector.connect( host=phost_mysql, database=pdatabase, user=puser, password=ppwd , auth_plugin='mysql_native_password' )

            if (pvider_table) :
                print("vidage table ressource")
                sql = "TRUNCATE TABLE `ressource`"
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                mydb.commit()
                print("table ressource videe")

                print("vidage table attribut")
                sql = "TRUNCATE TABLE `attribut`"
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                mydb.commit()
                print("table attribut videe")

            for resource in pliste_ressource:
                
                index_colonne = index_colonne + 1 #passer a la colonne suivante
                lnom_type_atribut = ''

                lliste_info_ressource = resource.split(';')

                locid_ressource = lliste_info_ressource[4]
                lnom_ressource = lliste_info_ressource[0]
                ltype_ressource = lliste_info_ressource[1]
                locid_compartiment_ressource = lliste_info_ressource[2]
                ldescription_ressource = ''
                ldate_heure_creation_ressource = lliste_info_ressource[13]

                #TABLE ressource ( ocid_res VARCHAR(255) PRIMARY KEY , nom_res VARCHAR(100), type_res VARCHAR(100), cmp_ocid VARCHAR(255) , desc_res VARCHAR(255) , dateheure_creation_res DATETIME );

                sql = "INSERT INTO ressource ( ocid_res , nom_res , type_res , cmp_ocid , desc_res , dateheure_creation_res  ) VALUES ("
                sql = sql + "'" + locid_ressource + "'"
                sql = sql + ", '" + lnom_ressource + "'"
                sql = sql + ", '" + ltype_ressource + "'"
                sql = sql + ", '" + locid_compartiment_ressource + "'"
                sql = sql + ", '" + ldescription_ressource + "'"
                sql = sql + ", '" + ldate_heure_creation_ressource + "'"
                sql = sql + ")"

                print(sql)

                mycursor = mydb.cursor()
                
                mycursor.execute(sql)

                mydb.commit()


                print("1 record inserted, ID:", mycursor.lastrowid)

                #ajouter des attriburts a cette ressource

                print("ajouter des attriburts a cette ressource, ID:", mycursor.lastrowid)

                PopulateTable.populate_table_attribut_ressource(locid_ressource , "ocid" , locid_ressource , ldate_heure_creation_ressource , mydb)
                #attribut ocid compartiment
                PopulateTable.populate_table_attribut_ressource( locid_compartiment_ressource , liste_nom_colonne[2] , locid_ressource , ldate_heure_creation_ressource, mydb)
                #attribut resource_type
                PopulateTable.populate_table_attribut_ressource( ltype_ressource , liste_nom_colonne[1] , locid_ressource , ldate_heure_creation_ressource, mydb)
                #attribut availability_domain
                PopulateTable.populate_table_attribut_ressource( lliste_info_ressource[6] , liste_nom_colonne[6] , locid_ressource , ldate_heure_creation_ressource, mydb)
                #attribut system_tag
                PopulateTable.populate_table_attribut_ressource( lliste_info_ressource[8] , liste_nom_colonne[8] , locid_ressource , ldate_heure_creation_ressource, mydb)
                #attribut defined_tag
                PopulateTable.populate_table_attribut_ressource( lliste_info_ressource[9] , liste_nom_colonne[9] , locid_ressource , ldate_heure_creation_ressource, mydb)
                #attribut lifecycle_state
                PopulateTable.populate_table_attribut_ressource( lliste_info_ressource[10] , liste_nom_colonne[10] , locid_ressource , ldate_heure_creation_ressource, mydb)
                #attribut freeform_tags
                PopulateTable.populate_table_attribut_ressource( lliste_info_ressource[12] , liste_nom_colonne[12] , locid_ressource , ldate_heure_creation_ressource, mydb)
                #attribut time_created
                PopulateTable.populate_table_attribut_ressource( lliste_info_ressource[13] , liste_nom_colonne[13] , locid_ressource , ldate_heure_creation_ressource, mydb)
        
        finally:

            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")

        return


