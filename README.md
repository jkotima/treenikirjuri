# treenikirjuri

Käyttäjä kirjautuu sovellukseen. 

Sovelluksessa voi luoda treeniohjelman kuntosalille. Treeniohjelma (program) koostuu treeneistä, treeni (workout) koostuu liikkeistä, liike (exercise) koostuu seteistä (sets).

Treenin aikana käyttäjällä on käytössään treenitila, jossa merkataan jokaisen treenitapahtuman aikana tehdyt liikkeet ja niihin liittyvät toistot ja painot.

Treenikertojen historiatietoja voidaan tarkastella.

## Toimintoja:

* Kirjautuminen
- Kuntosaliohjelman luominen *(tulossa oleva ominaisuus)*
	* Kuntosaliohjelmaan lisätään treenit (esim. "Maanantai")
		* Treeneihin lisätään liikkeet (esim. penkkipunnerrus. Valitaan listasta, tai luodaan uusi)

- Kuntosaliohjelman aktivointi *(tulossa oleva ominaisuus)*
	* Valitaan käyttäjän omista tai muiden käyttäjien tekemistä ohjelmista

- Treenitila
	* Treenin valinta (näkymässä näkyvät liikkeet määräytyvät tämän mukaisesti) *(tulossa oleva ominaisuus)*
	* Liikkeissä käytettyjen painojen ja toistojen lkm kirjaaminen
	* Liikkeiden kohdalla näkyy edellisen kerran toistot ja painot *(tulossa oleva ominaisuus)*

- Historia
	* Käyttäjä voi tarkastella menneitä treenitapahtumiansa
	* Käyttäjä voi tarkastella liikekohtaista edistymistään *(tulossa oleva ominaisuus)*

## Testitunnukset kirjautumiseen:
* käyttäjätunnus:hello
* salasana:world

[Tietokantakaavio](../master/documentation/dbdiagram.png)

[Käyttötapaukset](../master/documentation/usecases.md)

[Sovellus Herokussa](https://treenikirjuri.herokuapp.com/)

