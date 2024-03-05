
# Pour créer un script Python qui analyse une zone d'atterrissage OCI (Oracle Cloud Infrastructure) et génère un rapport CSV contenant les détails de toutes les ressources,
# vous devrez utiliser le SDK OCI Python. Assurez-vous que le SDK est installé en exécutant pip install oci.

# Voici un script qui rassemble les informations requises et génère un rapport CSV :


#-------------------------------------------------------------- -----------------------------------------

import oci
import csv

import traceback

from populate_table import PopulateTable

try:
    # set up config and create search client
    config = oci.config.from_file()
    search_client = oci.resource_search.ResourceSearchClient(config)
    
    #print(search_client.__dict__)
    # define query text and query
    print("define query text and query ------>>>>> ")
    query_text = "QUERY all resources where lifeCycleState != 'TERMINATED' && lifeCycleState != 'FAILED'"
    query = "QUERY all resources where lifeCycleState != 'TERMINATED' && lifeCycleState != 'FAILED'" 
    # create StructuredSearchDetails object and perform search query
    print("create StructuredSearchDetails object and perform search query ------>>>>> ")
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

    liste_nom_colonne = ['display_name', 'resource_type','compartment_id', 'identity_context', 'identifier', 'attribute_map',
            'availability_domain', '_additional_details', 'system_tag', 'defined_tag', 'lifecycle_state', 
            '_search_context',  'freeform_tags', 'time_created', 'swagger_types']

    print("Sauvegarde des types d attribut dans BD mysql----->>>>>")
    PopulateTable.populate_table_type_attribut(liste_nom_colonne , True)
    print("Types d attribut enregistres avec sucess dans BD mysql----->>>>>")

    

except:
# printing stack trace
 
 traceback.print_exc()

 
    
    