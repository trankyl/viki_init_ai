# Zone d’accueil OCI pour les organismes publics et les établissements des réseaux (REES et RSSS)

## Table des matières

- [Mise en Contexte](#mise-en-contexte)
- [Limitations de la solution et règles de déploiement](#limitations-de-la-solution-et-règles-de-déploiement)
- [Exemples de limites](Doc\Limites.md)
- [Exploitation de la zone d'accueil](#exploitation-de-la-zone-d'accueil)
- [Documentation et référence](#documentation-et-référence)
- [Lexique](Doc\Lexique.md)
  
### Architecture

- [Architecture de la zone d'accueil](Doc/Architecture/Architecture.md)  
  
### Déploiement

- [Description du script](Doc/Déploiement/Script_Desc.md)
- [Les Prérequis](Doc/Déploiement/PreRequis.md)
- [Déploiement du script](Doc/Déploiement/Deploi_Script.md)
- [Vérification du déploiement](Doc/Déploiement/Deploi_verif.md)
- [Autres scénarios de déploiement](Doc/Déploiement/autre_scenario_deploiement.md)   
- [Analyse des ressources importantes dans une zone d'accueil OCI](Doc/Déploiement/Analyse_des_ressources_importantes_dans_une_zone_d'accueil_de_l'OCI.md)     

### Réseautique   

- [Plan adressage](Doc/Réseautique/plan_adressage.md)   
- [Routage](Doc/Réseautique/routage.md)   


### Sécurité   

- [Contrôles de sécurité liés aux 12 exigences minimales](Doc/Sécurité/OCI_12_exigences.md)
- [Contrôle d'accès basé sur les rôles](Doc/Sécurité/Identification_des_roles.md)  
- [Cloud Guard](Doc/Sécurité/cloud_guard/menu_cloud_guard.md)  
- [Stratégies](Doc/Sécurité/RBAC.MD)
- [Journalisation](Doc/Sécurité/journalisation.md)
- [Pare-feu](Doc/Sécurité/pare_feu.md)
- [Zone de Sécurité](Doc/Sécurité/Zone_securite/menu_zone_securite_oci.md)


### Scripts et outils   

- [Suppression de la zone d'accueil via la pile de déploiement](Doc/Scripts-et-outils/suppression_stack_orm_oci.md)
- [Script de validation du déploiement de la zone d’accueil fournie par Oracle](Doc/Scripts-et-outils/pbmmPython.md)    
- [Suppression de la zone d'accueil via un script Python](Doc/Scripts-et-outils/superdelete/doc_superdelete.md)

### Notes de versions et mise à jour  

- [Historique des améliorations et des versions](Doc/Notes-de-versions-et-mise-à-jour/HistoriqueVersions.md)

### Tarification et coûts  

- [Traitement des anomalies](Doc\Gestion-des-Coûts\Traitement_des_anomalies.md)  
- [Analyse de l'utilisation des ressources dans une zone d'accueil de l'OCI](Doc\Gestion-des-Coûts\Analyse_de_l'utilisation_des_ressources_dans_une_zone_d'accueil_de_l'OCI.md)  
- [Gestion du Cycle de Vie des Ressources](Doc\Gestion-des-Coûts\Gestion_du_Cycle_de_Vie_des_Ressources.md)  
- [OCI-Contrôles automatisés des coûts](Doc\Gestion-des-Coûts\OCI-Contrôles_automatisés_des_coûts.md)


## Mise en Contexte

Le présent projet est réalisé dans le cadre du Décret 596-2020 visant la transposition infonuagique des infrastructures informatiques des organismes publics (OP) et des établissements du réseau de la santé et des services sociaux (RSSS), ainsi que celui de l’éducation et de l’enseignement supérieur (REES).

Dans le cadre du Programme de consolidation des centres de traitement informatique (PCCTI), la majorité des données gouvernementales québécoises doivent être regroupées dans l’infonuagique. Pour soutenir les organismes publics (OP) et les établissements dans leur démarche de consolidation, le Centre d’expertise en infonuagique (CEI) mettra à leur disposition des zones d’accueil déployables et réutilisables pour chacun des fournisseurs qualifiés. Celles-ci doivent respecter plusieurs exigences reconnues de sécurité afin d’assurer l'intégrité et la protection des données. Pour plus d'information en ce qui concerne la conformité et la sécurité, vous pouvez vous référer aux documents [contrôles de sécurité du Profil B](Doc/Sécurité/OCI_12_exigences.md) qui explique l'implémentation des 12 exigences minimales ou au document [RBAC](Doc/Sécurité/Identification_des_roles.MD) relatif au modèle d'accès.  

Dans ce contexte, le CEI a développé, en collaboration avec Oracle, une solution pour la zone d’accueil d'Oracle. Cette solution permet un déploiement rapide avec une activation des règles de sécurité qui permettent de déployer des charges de travail d'une façon sécuritaire. Le script de la solution est écrit en [Terraform](https://www.terraform.io/), un outil en distribution libre (*open source*) d'infrastructure en tant que code qui permet de provisionner l'infrastructure en utilisant un langage déclaratif simple à comprendre. Le déploiement de la zone d'accueil ne nécessite pas une connaissance particulière de Terraform, il suffit d'initialiser quelques variables avec des valeurs et de lancer son exécution. Pour les étapes complètes du déploiement, veuillez-vous référer au document [Déploiement du script](Doc/Déploiement/Deploi_Script.md) ainsi qu'au document de [Vérification du déploiement](Doc/Déploiement/Deploi_verif.md).

Pour plus d'information en ce qui concerne la structure du script et de ses différents modules, vous pouvez vous référer à la  [description du script](Doc/Déploiement/Script_Desc.md), qui fournit suffisamment de détail pour permettre l'exploitation et la modification du script, au besoin.

En ce qui concerne la sécurité, la zone d'accueil d'Oracle déploie le service [Cloud Guard](https://www.oracle.com/ca-fr/security/cloud-security/cloud-guard/) ainsi qu'une liste des [contrôles et sous-contrôles de sécurité](Doc/Sécurité/PBMM.md) correspondant aux 12 exigences minimales de sécurité du Profil B.

## Limitations de la solution et règles de déploiement

Le déploiement de la zone d'accueil d'Oracle dans les laboratoires du CEI a été complété en établissant et en respectant certaines règles. De plus, certains choix de paramètres utilisés restent à titre indicatif seulement, ces paramètres doivent être adaptés à chaque environnement et aux objectifs à atteindre. Vous avez la responsabilité de définir et de personnaliser les différents composants du script en fonction de vos besoins.

Voici une liste, non exhaustive, de ces hypothèses, des limitations et des données à revoir lors de votre installation.

- Les cinq blocs d'adresses utilisés sont ceux proposés par le MCN pour les zones d'accueil.
- Le découpage des blocs d'adresses est à titre indicatif seulement, ce découpage doit être revu pour chaque installation.
- Par défaut, les compartiments de la zone d'accueil sont déployés dans le compartiment racine de la location. Dans ce cas, toutes les stratégies de la zone d'accueil sont attachées au compartiment racine. Il est conseillé de modifier cette configuration lors de l'installation en précisant un "compartiment englobant".  Voir la section [**information de la pile**](Doc/Déploiement/Deploi_Script.md#information-de-la-pile) et [**variable de la pile**](Doc/Déploiement/Deploi_Script.md#variables-de-la-pile) dans la procédure [Déploiement du script](Doc/Déploiement/Deploi_Script.md).
- La zone d'accueil offre un nombre limité de services et des quotas bien définis. Vous pouvez réviser ces limites à partir de votre console, en consultant la section 'Limits, Quotas and Usage'.  
  - À partir du menu de votre console :
        - Choisir 'Governance & Administration'.
          - Dans 'Tenancy Explorer'
            - Choisir 'Limits, Quotas and Usage'.

      Cette même page vous donne la possibilité de créer une requête pour augmenter ces limites. À noter que le quota pour les compartiments peut être modifié par l'un des administrateurs et ne nécessite pas une ouverture de requête chez Oracle.  

      Il est possible de demander une augmentation de quota également à partir du menu 'Aide'/'Help'.
      En ouvrant le menu 'Aide'/'Help'
        - Dans la section Support
          - Cliquez sur 'Request service limit increase'/'.

Demander une augmentation de la limite de services

Pour avoir plus d'information au sujet de ces limites, pour faire une modification ou créer une requête pour un changement, veuillez consulter le lien suivant :

[Limites des services](https://docs.oracle.com/fr-ca/iaas/Content/General/Concepts/servicelimits.htm)

- La zone d'accueil déploie, par défaut, deux étiquettes (*tag*) par ressource, la première étiquette est 'CreatedBy' indiquant le créateur de la ressource, et la seconde est 'CreatedOn' représentant la date et l'heure de la création de la ressource. Évidemment, d'autres étiquettes peuvent être créées pour faciliter l'exploitation des ressources.  

## Exploitation de la zone d'accueil

En ce qui concerne l'exploitation de la zone d'accueil après sa création, la Direction générale du PCCTI (MCN) a publié un avis à la clientèle pour expliquer le processus d’approbation de l’architecture de la zone d’accueil des OP qui doivent transposer leurs charges de travail en infonuagique externe.

## Documentation et référence

[Oracle Github, Zone d'accueil-déploiement (en anglais)](https://github.com/oracle-quickstart/oci-cis-landingzone-quickstart/blob/main/DEPLOYMENT-GUIDE.md)

[Estimez votre coût mensuel](https://docs.oracle.com/fr-ca/iaas/Content/GSG/Tasks/signingup_topic-Estimating_Costs.htm)
