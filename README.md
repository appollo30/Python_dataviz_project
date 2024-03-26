# Python_dataviz_project

Ceci est le projet 'Accidents de Vélo' de Noureddine BOUDALI et Léo LASNIER effectué dans le cadre de l'unité 'DSIA_4101A Python pour la Datascience'.

## User Guide

Le projet a pour sujet la visualisation des données des accidents de vélo en France entre 2005 et 2021 récoltées par l'Observatoire National Interministériel de la Sécurité Routière stockées dans un fichier csv disponible à https://www.data.gouv.fr/fr/datasets/accidents-de-velo/. Il comporte 74758 entrées qui désignent un accident impliquant au moins un cycliste avec des informations telles que la date, l'heure, le lieu, la gravité de l'accident, ainsi que des informations sur la victime (âge, sexe, port de sécurité, etc.) et le ou les véhicules impliqués. 

### Déploiement

Vous pouvez déployer le projet tout d'abort en clonant le dépot git avec ```git clone git@github.com:appollo30/Python_dataviz_project.git```. 

Puis, pour les dépendances, installez python 3.8, puis les librairies additionnelles avec ```pip install -r requirements.txt```.

Alternativement, il est possible d'utiliser un environnement conda avec ```conda env create -f environment.yml```, puis ```conda activate project-accidentsvelo``` dans le shell conda.

Vous êtes donc prêt à lancer le projet. Pour le lancer, vous pouvez taper ```python main.py``` et l'app devrait se lancer. Vous devriez voir le dashboard suivant: 

<img width="1440" alt="image" src="https://github.com/appollo30/Python_dataviz_project/assets/27921296/4a095d1f-582c-44f1-a413-9b88614a9f97">

#### Précisions sur les cartes
Le dashboard affiche des cartes qui contiennent les informations géolocalisées des accidents par année. La génération de ces cartes prend un certain temps (~30mn), c'est pourquoi nous avons fait le choix de les stocker dans ```/templates```. On peut les regénérer à l'aide de la commande ```python Generate_maps.py```.

### Le Projet

Le dashboard affiche 3 zones pour la donnée

#### Zone 1
Dans la première zone, on peut choisir quel type de visualisation on souhaite afficher à l'aide d'un slider. Le 1er est un bar graph où se trouvent la repartition hommes/femmes des accidents de vélo pour chaque année, on peut choisir quelles années afficher à l'aide d'un menu déroulant. Le second chart est un histogramme qui affiche la distribution des âges des victimes des accidents par année. Le troisième est un scatterplot de la gravité moyenne des accidents en fonction de l'âge de la victime pour chaque année. 
#### Zone 2
La seconde zone est une carte de la France Métropolitaine qui montre les lieux des accidents. On peut choisir de montrer toutes les années ou bien une année en particulier. Chaque année est représentée par un point différent. 
#### Zone 3
La troisième zone est un diagramme circulaire qui montre la répartition hommes/femmes pour chaque année. 

### Commentaires

Pour le bar chart, on voit que la répartition hommes-femmes est déséquilibrée, avec les femmes qui sont victimes de 2 fois moins d'accidents que les hommes, et ce pour chaque année, ce qui signifie que ce n'est probablement pas une erreur statistique. Cela ne veut pas nécessairement dire que les femmes ont moins tendance à être impliquées dans les accidents, mais plutôt qu'elles ont moins tendance à prendre le vélo. C'est confirmé par l'enquête de l'ADEME https://librairie.ademe.fr/mobilite-et-transport/332-impact-economique-et-potentiel-de-developpement-des-usages-du-velo-en-france-en-2020.html, qui affirme que seulement 1 cycliste sur 3 est une femme. 
On remaque également une diminution soudaine du nombre d'accidents à partir de 2018. Ici on peut difficilement dire que les accidents ont été moins nombreux, mais plutôt que certaines données pour ces années là n'ont pas été renseignées.

<img width="1278" alt="image" src="https://github.com/appollo30/Python_dataviz_project/assets/27921296/bfbc73bc-59c4-4a7b-aac7-254144362a74">


Pour l'histogramme, on remarque que pour chaque année, les données sont ordonnées sous la forme d'une gaussienne centrée autour de ~40 ans. Les âges des victimes des accidents de vélo suivent donc le théorème centrale limite. On remarque également parfois une légère augmentation autour de 20 ans. 

<img width="1360" alt="image" src="https://github.com/appollo30/Python_dataviz_project/assets/27921296/2e1b405d-122c-49a8-ac27-c4ca93324136">

On peut attribuer cette augmentation au fait que les vingtenaires sont moins précautionneux que les plus jeunes et les plus agés sur les normes de sécurité, et qu'ils ont donc plus tendance à être impliqués dans des accidents.

Cette hypothèse est démentie par le chart suivant, le scatterplot, où l'on voit que la gravité moyenne des accidents est relativement constante entre 15 et 80 ans, et donc a priori ce n'est pas une question de porter ou non un casque. 
On peut ajouter que pour les enfants de moins de 15 ans et les adultes de plus de 80 ans, la gravité est plus faible, ici on peut attribuer cela soit au fait que ce sont des personnes plus fragiles, et qui sont donc plus concernées par les problématiques de sécurité, ou alors que quisque ce sont des âges où les accidents sont moins nombreux (cf le chart précédent), ils suivent moins la loi des grands nombres que les âges où l'on a plus d'échantillons, et donc l'écart-type est plus grand. 

<img width="1308" alt="image" src="https://github.com/appollo30/Python_dataviz_project/assets/27921296/bdc4da9b-3d6e-4f4a-a43b-f61db46ff455">

Ensuite, pour la carte, on remarque que les accidents sont plutôt concentrés autour des grandes agglomérations (Paris, Lyon, Marseille, Montpellier, Strasbourg, Toulouse, Lille, Rennes) et que les zones avec des densité de population plus faibles sont moins représentées. Cela semble logique puisque les zones les plus peuplées sont aussi celles où il y a le plus de circulation, et donc plus d'accidents. 

<img width="720" alt="image" src="https://github.com/appollo30/Python_dataviz_project/assets/27921296/1fea21ba-7c23-4add-9035-006449eed311">

(Il est important de noter que les cartes ne constituent pas un sous-ensemble exhaustif du dataset, puisqu'il y a beaucoup d'entrées où la localisation n'est pas renseignée)

Enfin, pour le pie chart, on voit la même répartition hommes/femmes que le bar chart.

<img width="645" alt="image" src="https://github.com/appollo30/Python_dataviz_project/assets/27921296/f05c3a49-3c0d-4756-9a20-e6cfb19ccd56">
