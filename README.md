# cotedivoire-vcard-update-script

Petit script pour mettre à jour vos numéros de téléphone passant de 8 à 10 chiffres. Il supporte également la conversion des numéros fixes. Le script est en version bêta je vous recommande donc de faire une sauvegarde avant d'utiliser le nouveau fichier VCF produit par le script.


## Utilisation

Affiche les informations d'utilisation

```bash 
main.py -h
```

Crée un nouveau fichier nommé new_contacts.vcf à partir contacts.vcf

```bash
main.py -i contacts.vcf -o new_contacts

```
or 

```bash
main.py --input contacts.vcf --output new_contacts

```
