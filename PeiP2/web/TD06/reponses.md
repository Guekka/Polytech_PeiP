Réseaux - TD3 - BIZEL Edgar
===========================

# APIs REST et JSON

Le site utilisé est www.rest-exemple.fr 

## Créer un cours

```
POST /cours HTTP/1.1
Host: www.rest-exemple.fr
Content-Length: 19
Content-Type: application/x-www-form-urlencoded

nom_cours=mon_cours
```

## Modifier le nom du cours

```
PUT /123456789A/name HTTP/1.1
Host: www.rest-exemple.fr
Content-Length: 23
Content-Type: application/x-www-form-urlencoded

nom_cours=nouveau_cours
```

## Obtenir des informations

```
GET /cours/?id_cours=123456789A HTTP/1.1
Host: www.rest-exemple.fr
```

## Obtenir la liste des cours

```
GET /cours HTTP/1.1
Host: www.rest-exemple.fr
```

## Réponse du serveur

```
HTTP/1.1 200 OK    
Content-Type: application/json; charset=utf-8 
Content-Length: 290
Connection: close

{
   "date":"Fri Dec 17 15:47:38 CEST 2021",
   "cours":[
      {
         "id":"0123456789",
         "nom_cours":"Introduction au Web",
         "nombre_participants":100,
		 "optionnel":false
      },
      {
         "id":"123456789A",
         "nom_cours":"nouveau_cours",
         "nombre_participants":20,
		 "optionnel":true
      }
   ]
}
```

# Manipulations d'objets JSON en Java

Voir fichier source.

# Jeu aux échecs en ligne grâce aux Services Web

## Création de partie

```
nc -C localhost 3000
GET /api/v1/chess/one HTTP/1.1
Host: localhost:3000

HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 99
ETag: W/"63-2Uwlqg0yuoEfYi15f7PrmGaHpQw"
Date: Fri, 17 Dec 2021 17:26:32 GMT
Connection: keep-alive

{"_id":"61bcc8486f231c1d447a7be2","status":"new game started","game_id":"61bcc8486f231c1d447a7be0"}
```

## Faire bouger une pièce du joueur humain

```
nc -C localhost 3000
POST /api/v1/chess/one/move/player HTTP/1.1
Host: localhost:3000
Content-Type: application/x-www-form-urlencoded
Content-Length: 46

from=a2&to=a3&game_id=61bcc8486f231c1d447a7be0
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 58
ETag: W/"3a-U5A4F2v3hOTAjOOsN1T7a1qhy4A"
Date: Fri, 17 Dec 2021 17:27:01 GMT
Connection: keep-alive

{"_id":"61bcc5ff6f231c1d447a7bcd","status":"figure moved"}
```

## Faire bouger une pièce par l'IA

```
nc -C localhost 3000
POST /api/v1/chess/one/move/ai HTTP/1.1
Host: localhost:3000
Content-Type: application/x-www-form-urlencoded
Content-Length: 32

game_id=61bcc8486f231c1d447a7be0
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 77
ETag: W/"4d-nIhcP0mnTA6g0tkWnw2EY8mk5RM"
Date: Fri, 17 Dec 2021 17:28:21 GMT
Connection: keep-alive

{"_id":"61bcc8b56f231c1d447a7be3","status":"AI moved!","to":"e5","from":"e7"}
```

## Récupérer le tableau au format FEN

```
nc -C localhost 3000
POST /api/v1/chess/one/fen HTTP/1.1
Host: localhost:3000
Content-Type: application/x-www-form-urlencoded
Content-Length: 32

game_id=61bcc8486f231c1d447a7be0
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 110
ETag: W/"6e-DxCrbXFCxcUPXfn+KOK6NViHM54"
Date: Fri, 17 Dec 2021 17:29:05 GMT
Connection: keep-alive

{"_id":"61bcc8e16f231c1d447a7be4","fen_string":"rnbqkbnr/pppp1ppp/8/4p3/8/P7/1PPPPPPP/RNBQKBNR w KQkq e6 0 2"}
```


