from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        'name': 'Y. Sudheer Babu',
        'title': 'Aspiring Full Stack Developer',
        'bio': 'Fresher passionate about Python, Web Development, and solving real-world problems.',
        'skills': ['Python', 'Flask', 'Django', 'JavaScript', 'SQL', 'Java'],
        'projects': [
            {'title': 'Emotion Detection', 'description': 'Detects human emotions from real-time data using machine learning.'},
            {'title': 'Weather App', 'description': 'Provides real-time weather updates using public APIs.'},
            {'title': 'Portfolio Website', 'description': 'This responsive website showcasing my profile.'}
        ],
        'contact': {
            'email': 'sudheers.k8790@gmail.com',
            'linkedin': 'linkedin.com/in/sudheer-yanamala',
            'github': 'https://github.com/babuyanama'
        }
    }
    return render_template('index.html', profile=profile)

@app.route('/resume')
def download_resume():
    return send_from_directory('resume', 'Y.SudheerBabu_Resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)
