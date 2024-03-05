# Le pare-feu réseau natif de Oracle Cloud Infrastructure  

Au menu  

- [Description](#description)
- [Fonctions de sécurité](#fonctions-de-sécurité)
- [Modèle de tarification](#modèle-de-tarification)
- [Coût](#coût)
- [Options de déploiement](#options-de-déploiement)
- [Configuration du pare-feu OCI](#configuration-du-pare\-feu-oci)
- [Journalisation dans le pare-feu OCI](#journalisation-dans-le-pare-feu-oci)
- [Modèle de responsabilité partagée du pare-feu natif dans Oracle Cloud Infrastructure](#modèle-de-responsabilité-partagée-du-pare-feu-natif-dans-oracle-cloud-infrastructure)
- [Comparaison avec le pare-feu FortiGate](#comparaison-avec-le-pare-feu-fortigate)
- [FAQ sur le pare-feu OCI](#faq-sur-le-pare-feu-oci)

## Description

With the CloudGuard solution, you can:  

- Open and maintain VPN tunnels
- Inspect data when it enters and leaves the private subnet
- Segregate networks in the VCN
- Protect your VCN resources with Check Point Software Blades
- Centrally manage this solution from your existing Check Point Security Management Server deployment

For setup in the Oracle Cloud, you must have basic knowledge of:  

- Check Point Security Gateways and Management Servers

- Oracle Cloud Infrastructure 

## Fonctions de sécurité  

- Filtrage de réseau avec état
- Filtrage personnalisé par URL et nom de domaine complet
- Détection et prévention des intrusions
- Inspection SSL
- Inspection du trafic du sous-réseau intra-VCN
- Inspection du trafic inter-VCN

Référence : <https://docs.oracle.com/fr-ca/iaas/Content/network-firewall/overview.htm>  

## Modèle de tarification  

There are multiple licensing options available:  

- License the CloudGuard Network Security Gateways: Bring-Your-Own-License (BYOL).  
- License a Security Management Server: Buy an Open Server license.  
- Pay-as-you-Go licensing via the Oracle Cloud Marketplace for both Security Gateways and Security Management.  

## Coût

![tarification_pare_feu_natif_oracle](image/tarification_pare_feu_natif_oracle2.png)  

Le pare-feu natif OCI coûte 2,75 $ CAD par heure. 

## Solution Topology

This sample environment is used to explain the configuration steps. When you follow the configuration steps below, make sure to replace the IP addresses in the example to reflect your environment.  

https://sc1.checkpoint.com/documents/IaaS/WebAdminGuides/EN/CP_CloudGuard_Network_for_Oracle_Cloud_Getting_Started/Content/Topics-Oracle-GS/Deploying-Cluster-in-Oracle-Cloud.htm?tocpath=_____4

## CloudGuard Cluster Deployment  

Follow these instructions to deploy Check Point's CloudGuard Cluster solution in Oracle. Perform the steps from the Oracle portal in the preferred compartment(s).

Sign in to your OCI tenant account.

Select the relevant CloudGuard listing from the Oracle Cloud Marketplace.

Create a new VCN or select an existing VCN (for example VCN with CIDR Block 10.0.0.0/16 ).

https://sc1.checkpoint.com/documents/IaaS/WebAdminGuides/EN/CP_CloudGuard_Network_for_Oracle_Cloud_Getting_Started/Content/Topics-Oracle-GS/Deploying-Cluster-in-Oracle-Cloud.htm?tocpath=_____4 


## Options de déploiement  

Vous pouvez déployer le pare-feu natif Oracle :  

- à partir de l'interface graphique d'Oracle Cloud;
- à l'aide d'[Oracle Resource Manager](https://github.com/oracle-quickstart/oci-network-firewall/tree/master/oci-network-firewall-reference-architecture#deploy-using-oracle-resource-manager).
- Vous pouvez également télécharger le code à partir de [Github](https://github.com/oracle-quickstart/oci-network-firewall/tree/master/oci-network-firewall-reference-architecture) ,le personnaliser en fonction de vos besoins d'affaires spécifiques et le déployer en utilisant [Terraform CLI](https://github.com/oracle-quickstart/oci-network-firewall/tree/master/oci-network-firewall-reference-architecture#deploy-using-oracle-resource-manager).

Dans ce document, nous allons déployer le pare-feu natif à partir de l'interface graphique d'Oracle Cloud.

## Configuration du pare-feu OCI

Il existe deux approches :

- Utilisation de la [console Web](https://docs.oracle.com/fr-ca/iaas/Content/network-firewall/policies.htm) dans un navigateur
- Utilisation de l'[API REST](https://docs.oracle.com/en-us/iaas/api/#/en/network-firewall/20211001/NetworkFirewallPolicy/CreateNetworkFirewallPolicy/)  

Référence : <https://docs.oracle.com/fr-ca/iaas/Content/network-firewall/setting-up-network-firewall.htm>

## Journalisation dans le pare-feu OCI

Vous pouvez activer la journalisation de vos pare-feux si les règles de la politique associée la prennent en charge et que vous êtes abonné au service de journalisation pour Oracle Cloud Infrastructure. Les journaux affichent l'activité de journalisation et les détails de chaque événement journalisé pendant une période spécifiée. Les journaux vous indiquent quand le trafic déclenche des règles et vous aident à renforcer la sécurité.

Référence : <https://docs.oracle.com/fr-ca/iaas/Content/network-firewall/logs.htm>  

## Modèle de responsabilité partagée du pare-feu natif dans Oracle Cloud Infrastructure  

| Responsabilité | Oracle | Client |
|------ | ------------- | -------------|
| Intégrer/configurer les stratégies du pare-feu | Non | Non |
| Configurer les dépendances d’intégration du pare-feu (DNS, règles d’entrée, réseau) | Non | Oui |
| Fournir une haute disponibilité (HA) pour le pare-feu | Oui | Non |
| Maintenir l’infrastructure du pare-feu à jour | Oui | Non |
| Surveiller les journaux de bord pour détecter tout comportement anormal ou indésirable | Oui | Oui |
| Construire de nouvelles règles basées sur les nouvelles vulnérabilités et atténuations | Oui | Non |
| Examiner et accepter les nouvelles règles recommandées | Non | Oui |

## Comparaison avec le pare-feu FortiGate

| Critère | Pare-feu natif OCI | Pare-feu FortiGate |
|------ | ------------- | -------------|
| Utiliser les groupes de sécurité réseau pour contrôler le trafic | Oui | Non |
| Déploiement par ORM | Oui | Oui |
| Déploiement par Terraform CLI | Oui | Oui |
| Licence BYOL | Non | Oui |
| Consommation à l'heure | Oui | / |
| Possibilité d'arrêter le pare-feu sans le supprimer, puis de le redémarrer | Non | Oui |
| Déploiement dans le sous-réseau de votre choix | Oui | Oui |
| Possibilité d'affecter manuellement une adresse IP au pare-feu | Oui | Non |
| Module Terraform | Oui | Oui |
| Journalisation - Le pare-feu réseau est intégré à Oracle Cloud Infrastructure Logging | Oui | / |
| Mesures - Le pare-feu réseau est intégré à Oracle Cloud Infrastructure Monitoring | Oui | / |

## FAQ sur le pare-feu OCI

<https://docs.oracle.com/fr-ca/iaas/Content/network-firewall/troubleshooting.htm>  

[Retour à la Page d'accueil](../README.md "Retour à la page d'accueil")
