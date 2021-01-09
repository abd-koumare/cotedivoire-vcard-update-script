# cotedivoire-vcard-update-script

Petit script pour mettre à jour vos numéros de téléphone passant de 8 à 10 chiffres. Il supporte également la conversion des numéros fixes. Bien que je sois convaincu de l'efficacité du script je vous recommande de faire un sauvegarde avant d'utiliser le nouveau nouvelle vcf produit par le script.


## Usage

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
