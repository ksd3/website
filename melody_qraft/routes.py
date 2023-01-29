from flask import Blueprint, render_template, jsonify
from melody_qraft.get_beat import get_beat_strings
from melody_qraft.beatgenerator import create_midi_file
import random
import string


# Blueprint Configuration

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/autogenerated_midi', methods=['GET'])
def autogenerated_midi():
    hihat_beat, snare_beat, bass_beat = get_beat_strings()
    name = ''.join(random.choices(string.ascii_lowercase, k=5))
    create_midi_file(name, bass_beat, snare_beat, hihat_beat)
    return render_template('autogenerated_midi.html', name=name)



