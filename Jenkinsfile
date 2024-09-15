pipeline {
    agent any
    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/calculator' 
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
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
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-credentials-id']]) {
                    sh 'sam deploy --no-confirm-changeset --stack-name calculator-stack --capabilities CAPABILITY_IAM'
                }
            }
        }
    }
}
