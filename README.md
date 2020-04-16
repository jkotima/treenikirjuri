# treenikirjuri

Käyttäjä kirjautuu sovellukseen. 

Sovelluksessa voi luoda treeniohjelman kuntosalille. Treeniohjelma (program) koostuu treeneistä, treeni (workout) koostuu liikkeistä, liike (exercise) koostuu seteistä (sets).

Treenin aikana käyttäjällä on käytössään treenitila, jossa merkataan jokaisen treenitapahtuman aikana tehdyt liikkeet ja niihin liittyvät toistot ja painot.

Treenikertojen historiatietoja voidaan tarkastella.

## Toimintoja:

* Kirjautuminen
- Kuntosaliohjelman luominen *(keskeneräinen ominaisuus)*
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

## Testitunnukset herokuun:
* käyttäjätunnus:hello
* salasana:world

[Sovellus Herokussa](https://treenikirjuri.herokuapp.com/)

## Asennus (linux)
1. Asenna python3 tarvittaessa
2. Kloonaa tai lataa sovellus haluamaasi hakemistoon
3. Luo ko. hakemistoon virtuaaliympäristö komennolla: **python3 -m venv venv**
4. Aktivoi virtuaaliympäristö komennolla: **source venv/bin/activate**
5. Asenna riippuvuudet komennolla: **pip install -r requirements.txt**
6. Aja sovellus komennolla: **python3 run.py**


## Käyttö

Tee itsellesi käyttäjätunnus valitsemalla "Rekisteröi". Kirjaudu sisään tunnuksillasi oikeasta yläkulmasta.

### Liikkeiden lisääminen
Voit lisätä liikkeitä valitsemalla "Liikkeet"->"Uusi liike". Täytä liikkeen tiedot ja valitse "Lisää liike".

### Liikkeiden muokkaaminen
Valitse valikosta "Liikkeet". Valitse listalta haluamasi liikkeen kohdalta "muokkaa".

### Treenitapahtuman tallentaminen
Valitse alasvetovalikosta liike jonka teit treenin aikana. Täytä sarjan toistojen lkm ja siinä käytetyt painot. Lisää liike treeniin.

Voit kommentoida treenikerran tuntemuksia yms. kommenttikenttään.

Lopuksi voit painaa "valmis"-painiketta.

### Treeniohjelmien luominen ja käyttö
Tulossa...

## Muuta materiaalia
[Tietokantakaavio](../master/documentation/dbdiagram.png)

[Käyttötapaukset](../master/documentation/usecases.md)



