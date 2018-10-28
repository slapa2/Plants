from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required

from plants import db
from plants.plants import plants
from plants.plants.models import Plant, PlantImage
from plants.plants.forms import AddPlantForm

@plants.route('/plants')
def plants_catalog():
    plants = Plant.query.all()
    return render_template('plants_catalog.html', title='baza roślin', plants=plants)


@plants.route('/add.plant', methods=['GET', 'POST'])
@login_required
def add_plant():
    form = AddPlantForm()
    if form.validate_on_submit():
        plant = Plant(polish_name=form.polish_name.data, image=form.image.data)
        db.session.add(plant)
        db.session.commit()
        flash(f'Roślina {form.polish_name.data} została dodana do bazy!', 'success')
        return redirect(url_for('plants.plants_catalog'))
    return render_template('addPlant.html', form=form, title='nowa roślina')
