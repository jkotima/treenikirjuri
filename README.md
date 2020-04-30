# treenikirjuri
Sovelluksessa voi luoda treeniohjelman kuntosalille sekä pitää kirjaa treenien aikana tehdyistä liikuntasuoritteista.

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
	* Aktvoidun treeniohjelman näkyminen
	* Liikkeissä käytettyjen painojen ja toistojen kirjaaminen

- Historia
	* Käyttäjä voi tarkastella menneitä treenitapahtumiansa
	
## Mahdollisesti tulossa olevia ominaisuuksia
- Käyttäjä voi tarkastella liikekohtaista edistymistään
	* graafit yms. käppyrät
- Treenitilassa näkyvissä edellisen kerran toistot ja painot
- Treenitietojen exporttaaminen
- Käyttäjän painon kirjaus
- Toistojen/sarjojen dynaaminen lukumäärä treeniohjelmassa

## Testitunnukset herokuun:
* käyttäjätunnus:hello
* salasana:world

[Sovellus Herokussa](https://treenikirjuri.herokuapp.com/)

## Materiaalit

[Asennus- ja käyttöohje](../master/documentation/documentation.md)

[Käyttötapaukset ja niihin liittvät SQL-kyselyt](../master/documentation/usecases.md)

[Tietokantadokumentaatio](../master/documentation/dbdoc.md)

[Tietokantakaavio (dbdiagram.io)](../master/documentation/dbdiagram.png)

[Tietokantakaavio (yuml.me)](../master/documentation/dbdiagram2.png)

