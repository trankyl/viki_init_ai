#### Retour en arrière

* [Documentation des stratégies et initiatives](policies_initiatives.md)
* [Page d'accueil](../Readme.md)  


# Liste de stratégies additionnelles  

## Verouillage de ressources dans les environnements Production et Plateforme  

### 1- Contexte

Etant donné que l'erreur est parfois humaine , nous avons ajoutées des stratégies pour éviter une suppression accidentelle de ressources déployées dans un environnement ( Exemple :  Production ,  Plateforme ).

### 2 - Liste des fichiers impliquées dans cette stratégie  


| Fichier                              | Emplacement             | Rôle    |
| ------------------------------------ | ----------------------- | -------------- |
| parameters.assigncustompolicy.yml        | /azure-pipeline/config/variables/scenario-base/policy/custom/assignments/policy/   | Contient la liste des environnements à verouiller  .  "assignmentScopes": [ "Production", "Plateforme" ] |
| parameters.custompolicies.yml       | /azure-pipeline/config/variables/scenario-
base/policy/custom/definitions/policy/    | Ajout de la stratégie DeployResourceGroupLock |
| parameters.assigncustompolicy.yml       | /azure-pipeline/config/variables/scenario-complexe/policy/custom/assignments/policy/    | Ajout de la stratégie Deploy-ResourceGroup-Lock pour le verouillage de ressources dans les environnements ZoneIntranetProduction , ZoneServicesEnLigneProduction , ZoneBureautiqueProduction , Plateforme |
| parameters.custompolicies.yml      | /azure-pipeline/config/variables/scenario-complexe/policy/custom/definitions/policy/    | Ajout de la stratégie DeployResourceGroupLock |
| custompolicy.bicep      | /modules/policy/custom/assignments/policy/   | Lancement du module deployresourcegrouplock.bicep pour déployer la stratégie DeployResourceGroupLock |
| deployresourcegrouplock.bicep      | /modules/policy/custom/assignments/policy/   | Verouillage des ressources dans un environnement |
| parameters.assigncustompolicy.json      | /modules/policy/custom/assignments/policy/   | Ajout de la stratégie **Deploy-ResourceGroup-Loc** pour le verouillage de ressources dans l'environnement Identite |
| custompolicies.bicep     | /modules/policy/custom/definitions/policy/   | Lancement du module Bicep deployresourcegrouplock.bicep pour déployer la stratégie de verouillage |
| deployresourcegrouplock.bicep     | /modules/policy/custom/definitions/policy/   | script Bicep qui déplooie les statégies de verouillage sur des ressources |
| parameters.custompolicies.json | /modules/policy/custom/definitions/policy/   | Ajout de la stratégie DeployResourceGroupLock  |  

### 3 - Pile d'exécution  

* policy.yml  
    * modules\policy\custom\assignments\policy\assigncustompolicy.bicep
        * modules\policy\custom\assignments\policy\custompolicy.bicep  
            * deployresourcegrouplock.bicep




