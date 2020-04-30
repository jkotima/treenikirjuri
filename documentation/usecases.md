# Käyttötapaukset ja niihin liittvät SQL-kyselyt

## Rekisteröinti (käyttäjän lisääminen)
1. Käyttäjä valitsee 'rekisteröi'
2. Käyttäjä täyttää nimen, käyttäjänimen ja salasanan
3. Käyttäjä valitsee 'luo käyttäjä'
```sql
INSERT INTO accounts (date_created, date_modified, name, username, password) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, nimi, käyttäjänimi, salasana);
```
## Kirjautuminen
Käyttäjä kirjautuu sovellukseen omalla käyttäjätunnuksella ja salasanalla.

```sql
SELECT *
FROM accounts 
WHERE accounts.username = ? AND accounts.password = ?;

-- ...jos rivejä esiintyy, kirjataan käyttäjä sisään
```
## Liikkeiden lisääminen
1. Käyttäjä valitsee valikosta 'lisää liike'
2. Käyttäjä valitsee 'uusi liike'
3. Käyttäjä antaa liikkeelle nimen, kuvauksen ja liikkeen kirjaamisessa käytetyn yksikön (esim. kg)
4. Käyttäjä valitsee 'Lisää liike'
```sql
INSERT INTO exercises (date_created, date_modified, name, description, unit, created_by)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, current_user.id);
```
## Liikkeiden listaaminen ja suodattaminen lisääjän nimen perusteella
1. Käyttäjä valitsee päävalikosta 'Liikkeet'
2. Käyttäjä voi hakea liikettä lisääjän perusteella sivun ylälaidassa olevalla lomakkeella

```sql

-- jos käyttäjä ei hae mitään, LIKE:n parametrina on "" -
-- tällöin palautuu kaikki taulun 'exercise' rivit

SELECT exercises.id, exercises.name, exercises.description, accounts.name, exercises.created_by 
FROM exercises 
LEFT JOIN accounts ON created_by = accounts.id 
WHERE LOWER(accounts.name) LIKE ?%;
```
## Liikkeiden muokkaaminen
1. Käyttäjä valitsee päävalikosta 'Liikkeet'
2. Käyttäjä painaa Muokkaa-nappulaa haluamansa liikkeen kohdalla
3. Käyttäjä täyttää haluamansa kentät ja painaa 'päivitä liike'

```sql
-- jos käyttäjä jättää jonkin kentän tyhjäksi, jätetään ko. muuttuja pois lauseesta eli päivittämättä

UPDATE exercises 
SET date_modified=CURRENT_TIMESTAMP, name=?, description=?, unit=? 
WHERE exercises.id = ?;
```
## Liikkeiden poistaminen
1. Käyttäjä valitsee päävalikosta 'Liikkeet'
2. Käyttäjä painaa Poista-nappulaa haluamansa liikkeen kohdalla

```sql
-- aluksi pitää poistaa kaikki setit (suoritetut liikkeet), jotka ovat tätä liikettä
DELETE FROM sets WHERE sets.exercise.id = ?;

-- sitten poistetaan itse liike
DELETE FROM exercises WHERE exercises.id = ?;
```
## Uuden treenin luominen
1. Käyttäjä valitsee päävalikosta 'Treenaa'=>'Uusi treenitapahtuma'
```sql
INSERT INTO events (date_created, date_modified, user_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, current_user.id);
```
## Edelliseen treeniin palaaminen
1. Käyttäjä valitsee päävalikosta 'Treenaa'=>'Jatka edellistä'
```sql
-- käyttäjän viimeisimmän treenin id:n hakeminen
SELECT events.id
FROM events 
WHERE events.user_id = 1 ORDER BY events.id DESC
LIMIT 1;
```
## Liikekohtaisten tietojen tallentaminen treenin aikana
1. Käyttäjä valitsee päävalikosta 'Treenaa'=>'Uusi treeni' tai 'Treenaa'=>'Jatka edellistä'
2. Käyttäjä valitsee tekemänsä liikkeen ja kirjaa siihen toistojen määrän ja käytetyn painon tms.

```sql
INSERT INTO sets (date_created, date_modified, reps, amount, exercise_id, event_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?);
```
## Tietyn treenikerran liikkeiden näyttäminen treenitilassa
1. Käyttäjä valitsee Aktivoi treeni-pudotusvalikosta treenin
2. Käyttäjä painaa aktivoi
```sql
--treenikerran liikkeiden listaus
SELECT workout_id, exercise_id, name, sets, reps, description, unit 
FROM workout_exercise 
LEFT JOIN exercises ON exercise_id = exercises.id 
WHERE workout_id = ?;

--suoritettujen sarjojen lkm laskeminen
SELECT count(*)
FROM sets
WHERE sets.event_id = ? AND sets.exercise_id = ?);
```
## Treenin kommentointi
1. Käyttäjä kirjoittaa kommenttikenttään treenitilassa
2. Käyttäjä painaa 'tallenna kommentti'
```sql
UPDATE events SET date_modified=CURRENT_TIMESTAMP, comment=? WHERE events.id = ?;
```
## Treenitapahtuman poistaminen
1. Käyttäjä valitsee haluamansa treenin treenitilassa 'poista treenitapahtuma ja sen tiedot'

```sql
-- aluksi pitää poistaa kaikki setit (suoritetut liikkeet), jotka ovat osa tätä treenitapahtumaa
DELETE FROM sets WHERE sets.event_id = ?
-- poistetaan itse treenitapahtuma
DELETE FROM events WHERE events.id = ?;
```
## Treenitapahtumien listaaminen (treenihistoria)
1. Käyttäjä valitsee päävalikosta 'treenihistoria'
```sql
SELECT *
FROM events 
WHERE events.user_id = ?
ORDER BY events.date_created DESC;
```

## Kuntosaliohjelman luominen
1. Käyttäjä valitsee päävalikosta 'Treeniohjelmat'
2. Käyttäjä valitsee 'Uusi ohjelma'
3. Käyttäjä antaa ohjelmalle nimen ja kuvauksen ja valitsee 'valmis'

```sql
INSERT INTO programs (date_created, date_modified, name, description, created_by) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, current_user.id);
```

## Kuntosaliohjelman poistaminen
1. Käyttäjä valitsee päävalikosta 'Treeniohjelmat'
2. Käyttäjä valitsee haluamansa kuntosaliohjelman kohdalta 'Poista'

```sql
-- 1. Nollataan kaikkien käyttäjien active_program, jossa tämä on
UPDATE accounts SET active_program = NULL
WHERE active_program = ?;

-- 2. Poistetaan kaikki tämän ohjelman treenikertojen ilmeentymät workout_exercisesta
DELETE FROM workout_exercise 
WHERE workout_id IN (
                     SELECT workout_id
                     FROM programs
                     WHERE id = :id
                     );

-- 3. Poistetaan kaikki tämän ohjelman treenikerrat
DELETE FROM workouts
WHERE program_id = :id;

--4. Poistetaan itse ohjelma
DELETE FROM programs WHERE programs.id = ?;

```
## Treenikerran lisääminen kuntosaliohjelmaan
1. Treeniohjelman muokkaustilassa, käyttäjä täyttää treenikerran nimen sekä kuvauksen 
2. Käyttäjä valitsee 'lisää treenikerta'

```sql
INSERT INTO workouts (date_created, date_modified, name, description, program_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, muokattava_treeniohjelma.id);
```
## Treenikerran poistaminen
1. Treeniohjelman muokkaustilassa, käyttäjä valitsee haluamansa treenitilan kohdalta 'Poista'
```sql
DELETE FROM workouts WHERE workouts.id = ?;

```

## Liikkeen lisääminen treenikertaan

1. Treeniohjelman muokkaustilassa, käyttäjä valitsee alasvetovalikosta liikkeen ja täyttää kenttiin sarjojen ja toistojen lukumäärät. 
2. Käyttäjä valitsee 'lisää liike treeniikertaan'

```sql
--sqlite3:
INSERT or REPLACE INTO workout_exercise (workout_id, exercise_id, sets, reps) 
VALUES (muokattava_treenikerta.id, lisättävä_liike.id, ?, ?)

--postgres:
INSERT INTO workout_exercise (workout_id, exercise_id, sets, reps
VALUES (muokattava_treenikerta.id, lisättävä_liike.id, ?, ?)
ON CONFLICT (workout_id, exercise_id) DO UPDATE
SET sets = ?, reps = ?;
```
## Kuntosaliohjelman aktivointi
1. Käyttäjä valitsee valikosta 'Treeniohjelmat'
2. Käyttäjä valitsee haluamansa ohjelman kohdalta 'Aktivoi'

```sql
UPDATE accounts SET date_modified=CURRENT_TIMESTAMP, active_program=? WHERE accounts.id = current_user.id;
```
## Kuntosaliohjelman deaktivointi
1. Käyttäjä valitsee valikosta 'Treeniohjelmat'
2. Käyttäjä valitsee oikeasta yläkulmasta, aktiivisen treeniohjelman nimen kohdalta 'deaktivoi'

```sql
UPDATE accounts SET date_modified=CURRENT_TIMESTAMP, active_program = NULL WHERE accounts.id = current_user.id;
```
## Yhteenlasketun painomäärän (selkävikaluku) tarkastelu
1. Käyttäjä katsoo etusivulle
2. Käyttäjä lopettaa kuntosalijäsenyytensä

```sql
SELECT SUM(sets.reps*sets.amount) AS weight FROM sets
LEFT JOIN exercises ON sets.exercise_id = exercises.id"
LEFT JOIN events ON sets.event_id = events.id"
WHERE exercises.unit = 'kg' AND events.user_id = :id";
```


