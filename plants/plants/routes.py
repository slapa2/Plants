from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required

from plants import db
from plants.plants import plants
from plants.plants.models import Plant, PlantImage
from plants.plants.forms import AddPlantForm

@plants.route('/plants')
def plants_catalog():
    plants = Plant.query.all()
    return render_template('plants.html', title='baza roślin', plants=plants)


@plants.route('/add.plant', methods=['GET', 'POST'])
@login_required
def add_plant():
    form = AddPlantForm()
    if form.validate_on_submit():
        plant = Plant(
            polish_name=        form.polish_name.data,
            latin_name=         form.latin_name.data,
            light_level =       form.light_level.data,
            light_description = form.light_description.data,
            water_level =       form.water_level.data,
            water_description = form.water_description.data,
            temperature =       form.temperature.data,
            soil =              form.soil.data,
            fertilizing =       form.fertilizing.data,
            transplanting =     form.transplanting.data,
            multiplication =    form.multiplication.data,
            image=form.image.data)

        db.session.add(plant)
        db.session.commit()
        flash(f'Roślina {form.polish_name.data} została dodana do bazy!', 'success')
        return redirect(url_for('plants.plants_catalog'))
    return render_template('addPlant.html', form=form, title='nowa roślina')

@plants.route('/edit.plant/<plant_id>', methods=['GET', 'POST'])
@login_required
def edit_plant(plant_id):

    plant = Plant.query.get(plant_id)
    form = AddPlantForm()

    if form.validate_on_submit():
        plant.polish_name=form.polish_name.data
        plant.latin_name=form.latin_name.data
        plant.light_level=form.light_level.data
        plant.light_description=form.light_description.data
        plant.water_level=form.water_level.data
        plant.water_description=form.water_description.data
        plant.temperature=form.temperature.data
        plant.soil=form.soil.data
        plant.fertilizing=form.fertilizing.data
        plant.transplanting=form.transplanting.data
        plant.multiplication=form.multiplication.data
        plant.image=form.image.data
        db.session.add(plant)
        db.session.commit()
        flash(f'Roślina {form.polish_name.data} została dodana do bazy!', 'success')
        return redirect(url_for('plants.plants_catalog'))

    form.polish_name.data = plant.polish_name
    form.latin_name.data = plant.latin_name
    form.light_level.data = plant.light_level
    form.light_description.data = plant.light_description
    form.water_level.data = plant.water_level
    form.water_description.data = plant.water_description
    form.temperature.data = plant.temperature
    form.soil.data = plant.soil
    form.fertilizing.data = plant.fertilizing
    form.transplanting.data = plant.transplanting
    form.multiplication.data = plant.multiplication
    form.image.data = plant.image

    return render_template('addPlant.html', form=form, title='nowa roślina')

@plants.route('/plants/<plant_id>')
def plant_info(plant_id):
    plant = Plant.query.get(plant_id)
    return render_template('plant.html', title='plant info', plant=plant)