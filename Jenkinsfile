pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Repository cloned'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install pytest requests flask pytest-html
                pytest -v
                '''
            }
        }

    }
}
