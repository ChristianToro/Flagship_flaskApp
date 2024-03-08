from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/EFT')
def escape_tarkov():
    return render_template('eft.html')

@app.route('/cooking')
def cooking():
    return render_template('cook.html')

@app.route('/swole', methods=['GET', 'POST'])
def fitness():
    if request.method == 'POST':
        data = request.get_json()
        goal = data['goal']
        level = data['level']
        routine = generate_routine(goal, level)  # You need to implement this function
        return jsonify({'routine': routine})
    return render_template('gym.html')

def generate_routine(goal, level):
    routines = {
        'weight_loss': {
            'beginner': "Cardio: 30 minutes brisk walking daily. Strength: 2 sets of 10 squats, 10 lunges, and 10 push-ups, three times a week.",
            'intermediate': "Cardio: 45 minutes running or cycling, four times a week. Strength: 3 sets of 15 squats, lunges, and push-ups with light weights, three times a week.",
            'advanced': "HIIT: 20 minutes, five times a week. Strength: 4 sets of 20 squats, lunges, and push-ups with heavier weights, four times a week.",
        },
        'muscle_gain': {
            'beginner': "Strength: Full body workouts focusing on compound movements (squats, deadlifts, bench press) 3 times a week. Aim for 3 sets of 8-12 reps.",
            'intermediate': "Strength: Split routine focusing on different muscle groups each day, 4 times a week. Increase weights and include isolation exercises. 4 sets of 8-12 reps.",
            'advanced': "Strength: Advanced split routines with heavy weights, focusing on muscle hypertrophy. Include drop sets and super sets. 5 times a week, 4-5 sets of 6-12 reps.",
        },
        'improve_fitness': {
            'beginner': "Cardio: Daily walks or cycling for 30 minutes. Flexibility: Yoga or stretching exercises twice a week.",
            'intermediate': "Cardio: Running, swimming, or cycling for 45 minutes, four times a week. Flexibility: Yoga or pilates, three times a week.",
            'advanced': "Cardio: Advanced cardio sessions (trail running, competitive cycling) for an hour, five times a week. Flexibility: Advanced yoga or martial arts for flexibility and core strength, four times a week.",
        }
    }

    return routines.get(goal, {}).get(level, "Routine not found. Please choose both a goal and a level.")
    

if __name__ == '__main__':
    app.run(debug=True)
