pipeline {
    agent any
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
                sh('chmod 777 run_all_tests.sh ')
                sh('./run_all_tests.sht')
	    }
        }
        stage("Deploy to Staging") {
            when {
                buildingTag()
                environment name: 'ENVIRONMENT', value: 'staging'
            }
            steps {
                sh('chmod 777 build_and_publish.sh')
                sh('./build_and_publish.sh')
	    }
        }
    }
}