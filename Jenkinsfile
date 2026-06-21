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
                pytest -v --html=report.html --self-contained-html
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t hitachi-flask .
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop flask-container || true
                docker rm flask-container || true

                docker run -d \
                --name flask-container \
                -p 5000:5000 \
                hitachi-flask
                '''
            }
        }

    }

    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])
        }
    }
}
