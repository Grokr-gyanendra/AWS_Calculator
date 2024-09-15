pipeline {
    agent any
    environment {
        AWS_DEFAULT_REGION = 'eu-north-1'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Grokr-gyanendra/AWS_Calculator' 
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/' 
            }
        }
        stage('Install SAM CLI') {
            steps {
                sh 'pip install aws-sam-cli'
            }
        }
        stage('Build') {
            steps {
                sh 'sam build'
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS_ACCESS_KEY_ID']]) {
                    sh 'sam deploy --no-confirm-changeset --stack-name calculator-stack --capabilities CAPABILITY_IAM'
                }
            }
        }
    }
}
