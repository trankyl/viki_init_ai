#### Retour en arri�re

* [Documentation des strat�gies et initiatives](policies_initiatives.md)
* [Page d'accueil](../Readme.md)  


# Liste de strat�gies additionnelles  

## Verouillage de ressources dans les environnements Production et Plateforme  

### 1- Contexte

Etant donn� que l'erreur est parfois humaine , nous avons ajout�es des strat�gies pour �viter une suppression accidentelle de ressources d�ploy�es dans un environnement ( Exemple :  Production ,  Plateforme ).

### 2 - Liste des fichiers impliqu�es dans cette strat�gie  


| Fichier                              | Emplacement             | R�le    |
| ------------------------------------ | ----------------------- | -------------- |
| parameters.assigncustompolicy.yml        | /azure-pipeline/config/variables/scenario-base/policy/custom/assignments/policy/   | Contient la liste des environnements � verouiller  .  "assignmentScopes": [ "Production", "Plateforme" ] |
| parameters.custompolicies.yml       | /azure-pipeline/config/variables/scenario-
base/policy/custom/definitions/policy/    | Ajout de la strat�gie DeployResourceGroupLock |
| parameters.assigncustompolicy.yml       | /azure-pipeline/config/variables/scenario-complexe/policy/custom/assignments/policy/    | Ajout de la strat�gie Deploy-ResourceGroup-Lock pour le verouillage de ressources dans les environnements ZoneIntranetProduction , ZoneServicesEnLigneProduction , ZoneBureautiqueProduction , Plateforme |
| parameters.custompolicies.yml      | /azure-pipeline/config/variables/scenario-complexe/policy/custom/definitions/policy/    | Ajout de la strat�gie DeployResourceGroupLock |
| custompolicy.bicep      | /modules/policy/custom/assignments/policy/   | Lancement du module deployresourcegrouplock.bicep pour d�ployer la strat�gie DeployResourceGroupLock |
| deployresourcegrouplock.bicep      | /modules/policy/custom/assignments/policy/   | Verouillage des ressources dans un environnement |
| parameters.assigncustompolicy.json      | /modules/policy/custom/assignments/policy/   | Ajout de la strat�gie **Deploy-ResourceGroup-Loc** pour le verouillage de ressources dans l'environnement Identite |
| custompolicies.bicep     | /modules/policy/custom/definitions/policy/   | Lancement du module Bicep deployresourcegrouplock.bicep pour d�ployer la strat�gie de verouillage |
| deployresourcegrouplock.bicep     | /modules/policy/custom/definitions/policy/   | script Bicep qui d�plooie les stat�gies de verouillage sur des ressources |
| parameters.custompolicies.json | /modules/policy/custom/definitions/policy/   | Ajout de la strat�gie DeployResourceGroupLock  |  

### 3 - Pile d'ex�cution  

* policy.yml  
    * modules\policy\custom\assignments\policy\assigncustompolicy.bicep
        * modules\policy\custom\assignments\policy\custompolicy.bicep  
            * deployresourcegrouplock.bicep




