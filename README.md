# treenikirjuri
Sovelluksessa voi luoda treeniohjelman kuntosalille. Treeniohjelma (program) koostuu treeneistä, treeni (workout) koostuu liikkeistä, liike (exercise) koostuu seteistä (sets).

Käyttäjä kirjautuu sovellukseen. 


Treenin aikana käyttäjällä on käytössään treenitila, jossa merkataan jokaisen treenitapahtuman aikana tehdyt liikkeet ja niihin liittyvät toistot ja painot.

Treenikertojen historiatietoja voidaan tarkastella.

## Toimintoja:

* Kirjautuminen

- Liikkeiden luominen
- Kuntosaliohjelman luominen
	* Kuntosaliohjelmaan lisätään treenikerrat (esim. "Maanantai")
		* Treenikertoihin lisätään liikkeet

- Kuntosaliohjelman aktivointi
	* Valitaan käyttäjän omista tai muiden käyttäjien tekemistä ohjelmista

- Treenitila
	* Treenikerran valinta kuntosaliohjelmasta (näkymässä näkyvät liikkeet määräytyvät tämän mukaisesti)
	* Liikkeissä käytettyjen painojen ja toistojen kirjaaminen

- Historia
	* Käyttäjä voi tarkastella menneitä treenitapahtumiansa

[Asennus- ja käyttöohje](../master/documentation/documentation.md)

[Käyttötapaukset ja niihin liittvät SQL-kyselyt](../master/documentation/usecases.md)

[Tietokantadokumentaatio](../master/documentation/dbdoc.md)

[Tietokantakaavio (dbdiagram.io)](../master/documentation/dbdiagram.png)

[Tietokantakaavio (yuml.me)](../master/documentation/dbdiagram2.png)

## Mahdollisesti tulossa olevia ominaisuuksia
- Käyttäjä voi tarkastella liikekohtaista edistymistään
- Liikkeiden kohdalla näkyy edellisen kerran toistot ja painot
- Treenitietojen exporttaaminen

## Testitunnukset herokuun:
* käyttäjätunnus:hello
* salasana:world

[Sovellus Herokussa](https://treenikirjuri.herokuapp.com/)




