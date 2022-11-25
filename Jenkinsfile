pipeline {
    agent { label 'myLabel' }
    parameters {
        choice(choices: 'staging\nproduction', description: 'Which environment?', name: 'ENVIRONMENT')
    }
    environment {
        GIT_TAG = sh(returnStdout: true, script: 'git describe --always').trim()
    }
    stages {
        stage("Checkout") {
            steps {
                checkout scm
	    }
        }
        stage("Test") {
            steps {
                sh('make test')
	    }
        }
        stage("Deploy to Staging") {
            when {
                buildingTag()
                environment name: 'ENVIRONMENT', value: 'staging'
            }
            steps {
                sh('make deploy')
	    }
        }
    }
}