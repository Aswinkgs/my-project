pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Terraform Apply') {
            steps {
                dir('terraform') {
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }

        stage('Run Ansible') {
            steps {
                sshagent(credentials: ['ec2-ssh-key']) {
                    sh 'ansible-playbook -i hosts.ini playbook.yml --ssh-common-args="-o StrictHostKeyChecking=no"'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Pipeline failed - check logs above'
        }
    }
}