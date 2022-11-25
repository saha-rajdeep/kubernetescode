<<<<<<< HEAD
node {
    stage ("checkout") {
        checkout scm
=======
pipeline {
    agent any 
    parameters {
        choice(choices: 'staging\nproduction', description: 'Which environment?', name: 'ENVIRONMENT')
>>>>>>> cce99d48e9bfca7722856a2ae9d900e85bc539e0
    }
    stage("test") {
        sh('run_all_tests.sh')
    }
    def tag = sh(returnStdout: true, script: "git tag --contains | head -1").trim()
    if (tag) {
        stage("deploy") {
            sh('build_and_publish.sh')
        }
    }
}
<<<<<<< HEAD

=======
>>>>>>> cce99d48e9bfca7722856a2ae9d900e85bc539e0
