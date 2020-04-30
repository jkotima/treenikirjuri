from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, validators


class ExerciseForm(FlaskForm):
    name = StringField("Nimi", [validators.required(),
                                validators.Length(max=144)])

    description = StringField("Kuvaus", [validators.Length(max=144)])
    unit = RadioField('Toistoissa käytetty yksikkö',
                      choices=[('kg', 'Kilogramma'),
                               ('min', 'Minuutti'),
                               ('sec', 'Sekunti'),
                               ('m', 'Metri'),
                               ('km', 'Kilometri')],
                      default='kg')

    class Meta:
        csrf = False


class NewRadioField(RadioField):
    # overridetaan Radiofieldin pre_validate -metodi
    # (palauttaa validationerrorin ilman syytä)
    def pre_validate(self, form):
        pass


class ExerciseEditForm(FlaskForm):
    name = StringField("Korvaava nimi", [validators.optional(),
                                         validators.Length(max=144)])

    description = StringField("Korvaava kuvaus", [validators.optional(),
                                                  validators.Length(max=144)])

    unit = NewRadioField('Korvaava toistoissa käytetty yksikkö',
                         choices=[('kg','Kilogramma'),
                                  ('min','Minuutti'),
                                  ('sec', 'Sekunti'),
                                  ('m', 'Metri'),
                                  ('km', 'Kilometri')])

    class Meta:
        csrf = False


class ExerciseFilterForm(FlaskForm):
    createdBy = StringField("Lisääjä")

    class Meta:
        csrf = False
