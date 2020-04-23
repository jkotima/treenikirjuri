## Tietokantaskeema
[Tietokantakaavio](../master/documentation/dbdiagram.png)

CREATE TABLE accounts (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	active_program INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(active_program) REFERENCES programs (id)
);
CREATE TABLE exercises (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	unit VARCHAR(20) NOT NULL, 
	created_by INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES accounts (id)
);
CREATE TABLE programs (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	created_by INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES accounts (id)
);
CREATE TABLE sets (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	reps INTEGER, 
	amount FLOAT NOT NULL, 
	exercise_id INTEGER NOT NULL, 
	event_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(exercise_id) REFERENCES exercises (id), 
	FOREIGN KEY(event_id) REFERENCES events (id)
);
CREATE TABLE workout_exercise (
	workout_id INTEGER NOT NULL, 
	exercise_id INTEGER NOT NULL, 
	sets INTEGER, 
	reps INTEGER, 
	PRIMARY KEY (workout_id, exercise_id), 
	FOREIGN KEY(workout_id) REFERENCES workouts (id), 
	FOREIGN KEY(exercise_id) REFERENCES exercises (id)
);
CREATE TABLE workouts (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	program_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(program_id) REFERENCES programs (id)
);
CREATE TABLE events (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	comment VARCHAR(144), 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES accounts (id)
);
