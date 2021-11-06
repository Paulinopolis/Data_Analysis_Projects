# La France n'a pas dit son dernier mot: word frequency analysis of comments about Zemmour's book


**Objectifs intermédiaires**

- récupération de données du site web Amazon et de donnée du réseau social Twitter

- création d'une dataframe contenant les données Amazon avec les données Twitter 

- application d'une word frequency de l'ensemble des données fournies par le dataframe


**Objectif final**

- Analyse des mots les plus utilisés dans les avis du site Amazon concernant le livre d'Eric Zemmour et dans les tweets crées suivant le hashtag #lafrancenapasditsonderniermot


**Les différentes étapes**

Etapes pour Amazon

- importation/récupération des données via un web scraping 

```sh
https://www.amazon.fr/France-pas-dit-son-dernier/product-reviews/2957930501?pageNumber
```

- création d'un dataframe contenant le titre du commentaire, la date, nombre de likes et source(Amazon)

- création d'un deuxième dataframe contenant seulement les commentaires et la source

Etapes pour Twitter

- importation/récupération des données Twitter via API RESTful 

```sh
url_rest = "https://api.twitter.com/1.1/search/tweets.json"
q = '%23lafrancenapasditsonderniermot'
```


- cleaning data des tweets
- retirer les urls
- retirer les emojis
- retirer la ponctuation inutiles


- creation d'un dataframe contenant le texte et la source (Twitter)


**Etapes de concatenation des données Amazon et Twitter**

- utilisation de MYSQL pour associer les deux tableaux

- creation d'une frequency des mots les plus utilisés par Amazon et Twitter

- création d'un wordcloud

- création d'une concordance avec les termes/référants "la France"


**Installations**

### Amazon:

```sh 
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from requests import get
import numpy as np
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
```

### Twitter:

```sh 
import requests
from requests_oauthlib import OAuth1   
import pandas as pd
from sqlalchemy import create_engine
```


**Difficultés** 

- impossibilité de récupérer les données de la FNAC (données sécurisées)
- création de browsers artificiels  pour récupérer les données Amazon (données sécurisées) 
- impossibilité d'utiliser les stop-words pour retirer les mots non-pertinents des données
- récupération du nombres de Tweets limitée (données sur 7 jours maximum)



