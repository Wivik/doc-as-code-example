# 1. Project Description {#project-description}

## 1.1. Project plan {#project-plan}

Some project plan

# 2. Functional architecture {#functional-architecture}

## 2.1. Functional architecture diagram {#functional-architecture-diagram}

Some diagram

```plantuml
!include <c4/C4_Context.puml>  

'ref http://plantuml.com/stdlib
!include <office/Users/user.puml>
!include <office/Users/mobile_user.puml>

'LAYOUT_WITH_LEGEND

title System Context diagram for Internet Banking System

Person(customer  , Customer , "<$user> <$mobile_user>\n A customer of the bank, with personal bank accounts" )

System(banking_system, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

System_Ext(mail_system, "E-mail system", "The internal Microsoft Exchange e-mail system.")
System_Ext(mainframe, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

Rel(customer, banking_system, "Uses")
Rel_Back(customer, mail_system, "Sends e-mails to")
Rel_Neighbor(banking_system, mail_system, "Sends e-mails", "SMTP")
Rel(banking_system, mainframe, "Uses")
```

Example tool from [PlantUML hitchhiker's guide](https://crashedmind.github.io/PlantUMLHitchhikersGuide/C4/C4Stdlib.html#c4-example-big-bank).

# 3. Technical architecture {#technical-architecture}

## 3.1. Technical architecture diagram {#technical-architecture-diagram}

```plantuml
footer Kubernetes Plant-UML
scale max 1024 width
skinparam linetype polyline
skinparam nodesep 10
skinparam ranksep 10



' Azure
!define AzurePuml https://raw.githubusercontent.com/RicardoNiepel/Azure-PlantUML/release/2-1/dist

!includeurl AzurePuml/AzureCommon.puml
!includeurl AzurePuml/AzureSimplified.puml

!includeurl AzurePuml/Compute/AzureAppService.puml
!includeurl AzurePuml/Compute/AzureBatch.puml
!includeurl AzurePuml/Containers/AzureContainerRegistry.puml
!includeurl AzurePuml/Containers/AzureKubernetesService.puml
!includeurl AzurePuml/Databases/AzureDatabaseForPostgreSQL.puml
!includeurl AzurePuml/Databases/AzureCosmosDb.puml
!includeurl AzurePuml/Databases/AzureSqlDatabase.puml
!includeurl AzurePuml/DevOps/AzurePipelines.puml
!includeurl AzurePuml/Identity/AzureActiveDirectory.puml
!includeurl AzurePuml/Networking/AzureLoadBalancer.puml
!includeurl AzurePuml/Security/AzureKeyVault.puml
!includeurl AzurePuml/Storage/AzureBlobStorage.puml
!includeurl AzurePuml/Storage/AzureStorage.puml

' Kubernetes
!define KubernetesPuml https://raw.githubusercontent.com/dcasati/kubernetes-PlantUML/master/dist

!includeurl KubernetesPuml/kubernetes_Context.puml
!includeurl KubernetesPuml/kubernetes_Simplified.puml

!includeurl KubernetesPuml/OSS/KubernetesApi.puml
!includeurl KubernetesPuml/OSS/KubernetesIng.puml
!includeurl KubernetesPuml/OSS/KubernetesPod.puml

actor "DevOps" as devopsAlias
collections "Client Apps" as clientalias
collections "Helm Charts" as helmalias

left to right direction

' Azure Components
AzureActiveDirectory(aad, "\nAzure\nActive Directory", "Global")
AzureContainerRegistry(acr, "ACR", "Canada Central")
AzureCosmosDb(cosmos, "\nCosmos DB", "Global")
AzureKeyVault(keyvault, "\nAzure\nKey Vault", "Global")
AzureLoadBalancer(alb, "\nLoad\nBalancer", "Canada Central")
AzureSqlDatabase(sql, "\nExternal\ndata stores", "Canada Central")
AzurePipelines(ado, "CI/CD\nAzure Pipelines", "Global")

' Kubernetes Components
Cluster_Boundary(cluster, "Kubernetes Cluster") {
    KubernetesApi(KubernetesApi, "Kubernetes API", "")
    
    Namespace_Boundary(nsFrontEnd, "Front End") {
        KubernetesIng(ingress, "API Gateway", "")
    }

    Namespace_Boundary(nsBackEnd, "Back End") {
        KubernetesPod(KubernetesBE1, "", "")
        KubernetesPod(KubernetesBE2, "", "")
        KubernetesPod(KubernetesBE3, "", "")
    }

    Namespace_Boundary(nsUtil, "Utiliy Services") {
        KubernetesPod(KubernetesUtil1, "", "")
        KubernetesPod(KubernetesUtil2, "","")
    }
}

Rel(devopsAlias, aad, "AUTH")
Rel(helmalias, KubernetesApi, "helm upgrade")

Rel(aad, keyvault, " ")
Rel(KubernetesApi, aad, "RBAC", "ASYNC")

Rel(clientalias, alb, "HTTP", "ASYNC")
Rel(alb, ingress, "HTTP", "ASYNC")

Rel(ingress, KubernetesBE1, " ")
Rel(KubernetesBE1, KubernetesBE2, " ")
Rel(KubernetesBE1, KubernetesBE3, " ")

Rel(KubernetesBE2, sql, " ")
Rel(KubernetesBE3, keyvault, "Pod Identity")
Rel(KubernetesBE3, cosmos, " ")

Rel(ado, acr, "docker push")
Rel_U(KubernetesApi, acr, "docker pull")
```

## 3.2. Technical resources {#technical-resources}

### 3.2.1. Network {#network}

| Environment | Provider | Network name | Subnet name | CIDR | Description |
| ------------------ | ------------ | -------------------- | ------------------- | ------------| ---------------- |
| Dev | Some CSP | mynetwork | mysubnet | 10.0.0.0/24 | The network |
| Prod | Some CSP | mynetwork | mysubnet | 10.0.0.0/24 | The network |

### 3.2.2. Cloud {#cloud}

| Environment | Provider | Folder    | Resource Type     | Name            |
|-------------|----------|-----------|-------------------|-----------------|
| Dev         | Some CSP | myappdev  | Container runtime | mycontainerdev  |
| Dev         | Some CSP | myappdev  | PaaS Database     | mydatabasedev   |
| Prod        | Come CSP | myappprod | Container runtime | mycontainerprod |
| Prod        | Some CSP | myappprod | PaaS Database     | mydatabaseprod  |
Container runtime settings :

```
vCPU : 0.5
Mem : 512Mb
```

# 4. Security requirements {#security-requirements}

## 4.1. Authentication {#authentication}

SSO

