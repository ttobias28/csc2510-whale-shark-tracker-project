from flask import Blueprint, render_template, request, redirect, url_for
from .models import get_all_sightings, add_sighting, get_stats

main = Blueprint('main', __name__)

@main.route('/')
def index():
    sightings = get_all_sightings()
    stats = get_stats()
    return render_template('index.html', sightings=sightings, stats=stats)

@main.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_sighting(
            request.form['location'],
            request.form['date'],
            request.form['size_meters'],
            request.form['observer'],
            request.form.get('notes', '')
        )
        return redirect(url_for('main.index'))
    return render_template('add_sighting.html')

@main.route('/health')
def health():
    return {'status': 'ok', 'app': 'whale-shark-tracker'}, 200