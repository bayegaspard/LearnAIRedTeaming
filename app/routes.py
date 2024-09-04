# flask_app/app/routes.py

from flask import render_template, redirect, url_for, flash, request
from app.installer import InstallationManager
from app.executor import ServiceManager

installer = InstallationManager()
executor = ServiceManager()

def register_routes(app):
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/install', methods=['GET', 'POST'])
    def install():
        if request.method == 'POST':
            installer.install()
            flash('Installation complete!', 'success')
            return redirect(url_for('result', action='install'))
        return render_template('install.html')

    @app.route('/run', methods=['GET', 'POST'])
    def run():
        if request.method == 'POST':
            service_name = request.form.get('service')
            executor.run_service(service_name)
            flash(f'Service {service_name} started!', 'success')
            return redirect(url_for('result', action=f'run-{service_name}'))
        return render_template('run.html')

    @app.route('/result/<action>')
    def result(action):
        return render_template('result.html', action=action)
