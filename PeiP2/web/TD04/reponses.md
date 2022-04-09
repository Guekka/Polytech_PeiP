# Réseaux - TD1 - BIZEL Edgar

## Exercice 1

Mon adresse IP est 172.29.181.47

## Exercice 2

L'adresse obtenue pour www.i3s.unice.fr est 134.59.130.2. Elle permet bien d'accéder au site

## Exercice 3

L'adresse obtenue pour www.univ-cotedazur.fr est 134.59.204.162. Firefox nous avertit d'une erreur de certificat SSL lorsqu'on s'y connecte. Si on procède malgré tout, on obtient une page d'erreur : "Page not found"

## Exercice 4

https://lms.univ-cotedazur.fr/course/view.php?id=13659&section=6#tabs-tree-start

Cette adresse est composée de :
- https: protocole de communication
- : caractère de séparation
- lms : sous domaine
- univ-cotedazur : nom de domaine de second niveau
- fr : nom de domaine de premier niveau
- /course/.../view.php : chemin de la resource
- ? : caractère de séparation 
- id=... : paramètres de requête GET

## Exercice 5

Pour lancer rapidement ces commandes sur tous les hôtes, on peut créer un petit script bash:
```bash
for url in www.univ-cotedazur.fr www.njcu.edu www.mit.edu ufrj.br; do ip=$(getent hosts $url | awk '{ print $1 }' | head -n1) && printf "\n$url\nping\n" >> res.txt && ping -c2 $ip >> res.txt && printf "\nnmap\n"  >> res.txt && nmap -p 80 $ip >> res.txt; done
```
Il semblerait cependant que ce script ne marche pas pour www.njcu.edu et www.mit.edu, dont les résultats ont été ajoutés manuellement.

On remarque que ufrj.br a un temps de latence bien plus élevé que les autres sites.
Cela est dû à la localisation du serveur : au Brésil

Les autres serveurs américains parviennent à obtenir une latence équivalente aux serveurs européens grâce à l'utilisation d'un Content Delivery Network
Celui-ci consiste en l'utilisation de plusieurs serveurs placés dans différentes zones géographiques, afin d'avoir toujours un serveur assez près de l'utilisateur

Résultats :
```
www.univ-cotedazur.fr
ping
PING 134.59.204.162 (134.59.204.162) 56(84) bytes of data.
64 octets de 134.59.204.162 : icmp_seq=1 ttl=52 temps=20.3 ms
64 octets de 134.59.204.162 : icmp_seq=2 ttl=52 temps=20.2 ms

--- statistiques ping 134.59.204.162 ---
2 paquets transmis, 2 reçus, 0 % paquets perdus, temps 1002 ms
rtt min/avg/max/mdev = 20.181/20.216/20.251/0.035 ms

nmap
Starting Nmap 7.80 ( https://nmap.org ) at 2021-12-15 16:30 CET
Nmap scan report for dev-portail.unice.fr (134.59.204.162)
Host is up (0.0031s latency).

PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.20 seconds

www.mit.edu
ping
PING 23.72.20.126 (23.72.20.126) 56(84) bytes of data.
64 octets de 23.72.20.126 : icmp_seq=1 ttl=53 temps=20.6 ms
64 octets de 23.72.20.126 : icmp_seq=2 ttl=53 temps=18.8 ms

--- statistiques ping 23.72.20.126 ---
2 paquets transmis, 2 reçus, 0 % paquets perdus, temps 1006 ms
rtt min/avg/max/mdev = 18.762/19.694/20.626/0.932 ms

nmap
Starting Nmap 7.80 ( https://nmap.org ) at 2021-12-15 16:32 CET
Nmap scan report for a23-72-20-126.deploy.static.akamaitechnologies.com (23.72.20.126)
Host is up (0.0039s latency).

PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.23 seconds

www.njcu.edu
ping
PING 23.185.0.1 (23.185.0.1) 56(84) bytes of data.
64 octets de 23.185.0.1 : icmp_seq=1 ttl=56 temps=20.8 ms
64 octets de 23.185.0.1 : icmp_seq=2 ttl=56 temps=21.2 ms

--- statistiques ping 23.185.0.1 ---
2 paquets transmis, 2 reçus, 0 % paquets perdus, temps 1001 ms
rtt min/avg/max/mdev = 20.782/21.010/21.238/0.228 ms

nmap
Starting Nmap 7.80 ( https://nmap.org ) at 2021-12-15 16:36 CET
Nmap scan report for 23.185.0.1
Host is up (0.0034s latency).

PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.30 seconds

ufrj.br
ping
PING 146.164.84.216 (146.164.84.216) 56(84) bytes of data.
64 octets de 146.164.84.216 : icmp_seq=1 ttl=32 temps=229 ms
64 octets de 146.164.84.216 : icmp_seq=2 ttl=32 temps=230 ms

--- statistiques ping 146.164.84.216 ---
2 paquets transmis, 2 reçus, 0 % paquets perdus, temps 1005 ms
rtt min/avg/max/mdev = 229.245/229.463/229.681/0.218 ms

nmap
Starting Nmap 7.80 ( https://nmap.org ) at 2021-12-15 16:30 CET
Nmap scan report for 146.164.84.216
Host is up (0.00042s latency).

PORT   STATE    SERVICE
80/tcp filtered http

Nmap done: 1 IP address (1 host up) scanned in 0.39 seconds
```