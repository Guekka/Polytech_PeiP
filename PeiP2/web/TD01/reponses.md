# EXERCICE 3

### Question 1
> Quelle est la distance totale entre les bords droits et gauche, et
> entre les bords supérieur et inférieur, du bloc 0 (c'est à dire du paragraphe
> qui est à l'intérieur du div d'id part1) si la propriété "padding: 10px 20px
> 30px 40px;" lui est affectée ?

Cette propriété affecte, dans l'ordre, le bord haut - droit - bas - gauche.
Sans compter les bords:
    - Entre les bords droit et gauche, il y a 260px : 20px + 40px + 200px
    - Entre les bords supérieur et inférieur, il y a 60px : 10px + 30px + 20px

### Question 2
> Que se passe-t-il (quels changement visuel prennent effet) lorsque
> la propriété "margin: 0px 0px 100px 0px;" est ajoutée au bloc 0 ? Supposez que
> la propriété padding de la question précédente est toujours en place.

Un grand espace vide en dessous du bloc 0 apparait. Le rectangle ne change pas.

### Question 3
> Que se passe-t-il si les blocs 1, 2 et 3 sont tous des boîtes
> block ? inline ? inline-block ?

Block: chaque bloc est affiché sur sa propre ligne
Inline-block: les blocs ne changent pas, mais sont affichés à la suite
Inline: les blocs sont affichés sur la même ligne mais leur dimension n'est pas
préservée. Il semblerait que le padding soit supprimé.

### Question 4 (Optionnel)
> Testez les propriétés suivantes sur le bloc 0 et
> prenez le temps de bien identifier les différentes zones de la boîte (contenu,
> padding, bordure, margin) : margin à 1em, 100px, 10%, 2cm. padding à 1em,
> 100px, 10%, 2cm. Essayer de ne changer que le padding ou margin du dessus,
> dessous ou des côtés (en utilisant margin-top par exemple). Essayer de donner
> quatre valeurs différentes au margin (ou le padding) du dessus, dessous ou des
> côtés.

### Question 5 (Optionnel)
> Explorez ce qu'il se passe si les boîtes 1, 2 et 3
> deviennent des boîtes  block, inline et inline-block respectivement ?
> inline-block, inline et block respectivement ? inline, block et inline-block
> respectivement ? testez d'autres combinaisons possibles.


# EXERCICE 4

<a>, <img />, <li>, <ol>, <ul>, <br>, <em>, <hX>, <strong>, <p> sont des
balises communes

