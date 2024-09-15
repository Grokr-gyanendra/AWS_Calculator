pipeline {
    agent any
    
    parameters {
        choice(name: 'DEPLOY_STAGE', choices: ['staging', 'production'], description: 'Select the deployment stage')
        string(name: 'ARTIFACTS_BUCKET', defaultValue: 'my-artifacts-bucket', description: 'Enter the S3 bucket for artifacts')
        string(name: 'ARTIFACTS_PREFIX', defaultValue: 'my-prefix', description: 'Enter the S3 prefix for artifacts')
    }

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
        STACK_NAME         = "book-app-${params.DEPLOY_STAGE}"
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Grokr-gyanendra/AWS_Calculator'
            }
        }

        stage('Run in Docker') {
            steps {
                // Run all commands in a Python Docker container
                sh '''
                    docker run --rm -v $(pwd):/workspace -w /workspace python:3.8-slim /bin/bash -c "
                    python3 -m pip install --upgrade pip &&
                    python3 -m pip install -r requirements.txt &&
                    pytest tests/"
                '''
            }
        }

        stage('Package Application') {
            steps {
                script {
                    // SAM build and package with specified artifacts bucket and prefix
                    sh "sam build"
                    sh "sam package --s3-bucket ${params.ARTIFACTS_BUCKET} --s3-prefix ${params.ARTIFACTS_PREFIX} --output-template-file template.yml"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy to the stack with the appropriate stage and parameters
                    sh "sam deploy --template-file template.yml --stack-name ${STACK_NAME} --parameter-overrides ParameterKey=Stage,ParameterValue=${params.DEPLOY_STAGE} --capabilities CAPABILITY_IAM"
                }
            }
        }
    }
}
