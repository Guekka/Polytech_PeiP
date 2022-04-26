# Réseaux - TD2 - BIZEL Edgar

## Q1

Retour de netcat:
```
GET / HTTP/1.1
Host: 127.0.0.1:1234
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
```

## Q2

La seule différence avec le retour précédent est la requête GET : au lieu de demander l'accès à /, la racine, on demande l'accès à /dir1/page1.html

```
GET /dir1/page1.html HTTP/1.1
Host: localhost:1234
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
```

## Q3

Encore une fois, la seule différence est la requête GET, qui contient cette fois les paramètres données dans l'URL

```
GET /dir1/page1.html?var1=1&var2 HTTP/1.1
Host: 127.0.0.1:1234
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
```

## Q4

Voici un exemple de retour que l'on peut donner à la requête émise par le navigateur :
```
HTTP/1.1 200 OK    
Content-Type: text/plain; charset=utf-8 
Content-Length: 6
Connection: close

Erreur
```

## Q5

### Partie 1

On utilise d'abord la commande host pour récupérer l'adresse IP : 
`host www.i3s.unice.fr`. On obtient 134.59.130.2

On se connecte ensuite avec la commande suivante :
`openssl s_client -crlf 134.59.130.2:443`
On utilise le port 443, correspondant à l'HTTPS

Pour demander une ressource, on utilise une requête GET. Une fois la connexion effectuée, on écrit :
```
GET /~lopezpac/ HTTP/1.1
Host: www.i3s.unice.fr
Connection: close
```
Et la réponse :
```
HTTP/1.1 200 OK
Date: Thu, 16 Dec 2021 10:32:02 GMT
Server: Apache/2.4.38 (Debian)
Vary: Accept-Encoding
Content-Length: 5734
Connection: close
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
...
```

Le contenu HTML de la page est renvoyé.
Les feuilles CSS et les images ne sont pas téléchargées. Le navigateur doit donc "parser" l'HTML, et télécharger chaque ressource nécessaire.

### Partie 2

On recommence avec la même adresse, mais sans le "/". 
Cette fois, la réponse est différente
```
HTTP/1.1 301 Moved Permanently
Date: Thu, 16 Dec 2021 10:33:42 GMT
Server: Apache/2.4.38 (Debian)
Location: https://www.i3s.unice.fr/~lopezpac/
Content-Length: 243
Connection: close
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
...
```

On peut constater que cette adresse ne désigne pas la même page. On obtient cette fois un code 301, qui indique une redirection

### Partie 3

On recommence une troisième fois avec la page `/~toto/`. On obtient :
```
HTTP/1.1 404 Not Found
Date: Thu, 16 Dec 2021 10:35:38 GMT
Server: Apache/2.4.38 (Debian)
X-Content-Type-Options: nosniff
Expires: Sun, 19 Nov 1978 05:00:00 GMT
Cache-Control: no-cache, must-revalidate
X-Content-Type-Options: nosniff
Content-Language: fr
X-Frame-Options: SAMEORIGIN
Permissions-Policy: interest-cohort=()
X-Generator: Drupal 7 (http://drupal.org)
Connection: close
Transfer-Encoding: chunked
Content-Type: text/html; charset=utf-8

3f29
<!DOCTYPE html>
```

Cette fois, nous avons un 404 Not Found : la page n'existe pas.

## Q6

L'adresse utilisée par le navigateur est `file:///home/user/T%C3%A9l%C3%A9chargements/form.html`
On a donc les composants habituels, plus, au départ, "file://". Cela indique au navigateur de chercher un fichier local

En regardant le code HTML, on voit que les données sont envoyées à `localhost:1234`

Pour que le serveur réponde, on utilise netcat : `netcat -l 1234`
```
GET /?var=coucou HTTP/1.1
Host: localhost:1234
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Sec-Fetch-User: ?1

HTTP/1.1 200 OK    
Content-Type: text/plain; charset=utf-8 
Content-Length: 7
Connection: close

Bonjour
```

Le navigateur affiche alors "Bonjour"
## Q7

On change la méthode pour POST. netcat affiche :
```
POST / HTTP/1.1
Host: localhost:1234
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 10
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Sec-Fetch-User: ?1

var=coucou

HTTP/1.1 200 OK    
Content-Type: text/plain; charset=utf-8 
Content-Length: 7
Connection: close

Bonjour
```

On remarque que la variable est passée différemment. Dans le cas du GET, elle est à côté du chemin de la ressource, séparée par "?"
Dans le cas de POST, la variable est après tous les paramètres, à la fin du paquet.

## Q8

On démarre deux terminaux avec `netcat -l 1234` et `netcat -l 1235`

On se connecte dans le navigateur à `localhost:1234`. Le premier netcat affiche 
```
GET / HTTP/1.1
Host: localhost:1234
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
```

On donne la réponse suivante :
```
HTTP/1.1 200 OK
Content-type: text/html
Connection: close
Content-length: 86

<html>
<head></head>
<body><img src="http://localhost:1235/test.jpg"/></body>
</html>
```

Cette fois, c'est le second netcat qui affiche :
```
GET /test.jpg HTTP/1.1
Host: localhost:1235
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: image/avif,image/webp,*/*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: http://localhost:1234/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: cross-site
```

On voit donc qu'il est possible d'héberger deux serveurs distincts sur la même machine à condition d'utiliser des ports différents. Chacun des netcat est indépendant.