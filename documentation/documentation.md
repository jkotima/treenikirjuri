## Asennus (linux)
1. Asenna python3 tarvittaessa
2. Kloonaa tai lataa sovellus haluamaasi hakemistoon
3. Luo ko. hakemistoon virtuaaliympäristö komennolla: **python3 -m venv venv**
4. Aktivoi virtuaaliympäristö komennolla: **source venv/bin/activate**
5. Asenna riippuvuudet komennolla: **pip install -r requirements.txt**
6. Aja sovellus komennolla: **python3 run.py**

## Käyttöönotto herokussa
Sovellus on heroku-yhteensopiva, ja pitäisi toimia ilman sen kummempaa säätöä herokussa. PostgreSQL pitää olla asennettuna.

# Sovelluksen käyttö

Tee itsellesi käyttäjätunnus valitsemalla "Rekisteröi". Kirjaudu sisään tunnuksillasi oikeasta yläkulmasta.

### Liikkeiden lisääminen
Voit lisätä liikkeitä valitsemalla "Liikkeet"->"Uusi liike". Täytä liikkeen tiedot ja valitse "Lisää liike".

### Liikkeiden muokkaaminen
Valitse valikosta "Liikkeet". Valitse listalta haluamasi liikkeen kohdalta "muokkaa".

### Treenitapahtuman tallentaminen
Valitse alasvetovalikosta liike jonka teit treenin aikana. Täytä sarjan toistojen lkm ja siinä käytetyt painot. Lisää liike treeniin.

Voit kommentoida treenikerran tuntemuksia yms. kommenttikenttään.

Lopuksi voit painaa "valmis"-painiketta.

*HUOM! Aktivoitu treeniohjelma on tulossa tähän näkymään, toiminnallisuus ei ole vielä valmis.*

### Treenihistorian tarkastelu
Valitse valikosta "treenihistoria".

### Treeniohjelmien luominen
Valitse valikosta "treeniohjelmat". Valitse "Uusi treeniohjelma". Anna
treeniohjelmallesi nimi ja kuvaus. Paina valmis, jonka jälkeen pääset treeniohjelman muokkausnäkymään.

#### Treenikertojen lisääminen treeniohjelmaan
Treeniohjelman muokkausnäkymässä, anna treenikerrallesi nimi (esimerkiksi 'Keskiviikko') ja kuvaus (esimerkiksi 'jalkapäivä'). Paina "Lisää treenikerta".

#### Liikkeiden lisääminen treenikertaan
Treeniohjelman muokkausnäkymässä, valitse alasvetovalikosta haluamasi liike, anna sille sarjojen ja toistojen lukumäärä ja paina "Lisää liike treenikertaan".

### Treenikertojen/liikkeiden poistaminen
Treeniohjelman muokkausnäkymässä, valitse poista treenikerta/poista liike treenikerrasta. 

### Treeniohjelman aktivoiminen
Treeniohjelmien listausnäkymässä, valitse haluamasi treeniohjelman kohdalta "aktivoi". Nyt treeniohjelma näkyy treeninäkymässä *(HUOM! tulossa oleva ominaisuus)*

Voit etsiä treeniohjelmia lisääjän perusteella.

### Treeniohjelman tarkastelu
Treeniohjelmien listausnäkymässä, klikkaa haluamasi treeniohjelman nimeä.

### Treeniohjelman muokkaaminen/poistaminen
Treeniohjelmien listausnäkymässä, klikkaa haluamasi treeniohjelman kohdalta muokkaa/poista.

## Muuta materiaalia
[Tietokantakaavio](../master/documentation/dbdiagram.png)
[Tietokantadokumentaatio](../master/documentation/dbdoc.md)
[Käyttötapaukset ja niihin liittyvät tietokantakyselyt](../master/documentation/usecases.md)