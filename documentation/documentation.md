## Asennus (linux)
1. Asenna python3 tarvittaessa
2. Kloonaa tai lataa sovellus haluamaasi hakemistoon
3. Luo ko. hakemistoon virtuaaliympäristö komennolla: **python3 -m venv venv**
4. Aktivoi virtuaaliympäristö komennolla: **source venv/bin/activate**
5. Asenna riippuvuudet komennolla: **pip install -r requirements.txt**
6. Aja sovellus komennolla: **python3 run.py**

## Käyttö Herokussa
Sovellus on Heroku-yhteensopiva. PostgreSQL pitää olla asennettuna.

# Sovelluksen käyttö

Tee itsellesi käyttäjätunnus valitsemalla "Rekisteröi". Kirjaudu sisään tunnuksillasi oikeasta yläkulmasta.

### Liikkeiden lisääminen
Voit lisätä liikkeitä valitsemalla "Liikkeet"->"Uusi liike". Täytä liikkeen tiedot ja valitse "Lisää liike".

### Liikkeiden muokkaaminen
Valitse valikosta "Liikkeet". Valitse listalta haluamasi liikkeen kohdalta "muokkaa".

### Treenitapahtuman tallentaminen

#### Liikkeiden lisääminen ilman aktivoitua treeniohjelmaa
Valitse alasvetovalikosta liike jonka teit treenin aikana. Täytä sarjan toistojen lkm ja siinä käytetyt painot. Lisää liike treeniin.

#### Treeniohjelman treenikerran liikkeiden listaaminen treenitilassa
Aluksi sinulla pitää olla treeniohjelma aktivoituna (treeniohjelmat=>aktivoi).
Aktivoi treeni-vetivalikosta voit valita treenin, tämän jälkeen paina 'aktivoi'.
Nyte liikkeet ovat näkyvillä.

Voit kommentoida treenikerran tuntemuksia yms. kommenttikenttään.

Lopuksi voit painaa "valmis"-painiketta.

### Treenihistorian tarkastelu
Valitse valikosta "treenihistoria". Voit muokata ja tarkastella treenikertaa Muokkaa-painikkeesta

### Treeniohjelmien luominen
Valitse valikosta "treeniohjelmat". Valitse "Uusi ohjelma". Anna treeniohjelmallesi nimi ja kuvaus. Paina valmis, jonka jälkeen pääset treeniohjelman muokkausnäkymään.

### Treeniohjelman muokkaaminen
Treeniohjelmien listausnäkymässä, valitse 'Muokkaa' (haluamasi treeniohjelman kohdalta)

#### Treenikertojen lisääminen treeniohjelmaan
Treeniohjelman muokkausnäkymässä, anna treenikerrallesi nimi (esimerkiksi 'Keskiviikko') ja kuvaus (esimerkiksi 'jalkapäivä'). Paina "Lisää treenikerta".

#### Liikkeiden lisääminen treenikertaan
Treeniohjelman muokkausnäkymässä, valitse alasvetovalikosta haluamasi liike, anna sille sarjojen ja toistojen lukumäärä ja paina "Lisää liike treenikertaan".

### Treenikertojen/liikkeiden poistaminen
Treeniohjelman muokkausnäkymässä, valitse poista treenikerta/poista liike treenikerrasta. 

### Treeniohjelman aktivoiminen
Treeniohjelmien listausnäkymässä, valitse haluamasi treeniohjelman kohdalta "aktivoi". Nyt treeniohjelma näkyy treeninäkymässä. 
Voit myös etsiä treeniohjelmia lisääjän perusteella.

### Treeniohjelman tarkastelu
Treeniohjelmien listausnäkymässä, klikkaa haluamasi treeniohjelman nimeä.

### Treeniohjelman muokkaaminen/poistaminen
Treeniohjelmien listausnäkymässä, klikkaa haluamasi treeniohjelman kohdalta muokkaa/poista.
