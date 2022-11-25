node {
    stage ("checkout") {
        checkout scm
    }
    stage("test") {
        sh('chmod 777 run_all_tests.sh ')
        sh('./run_all_tests.sh')
    }
    def tag = sh(returnStdout: true, script: "git tag --contains | head -1").trim()
    if (tag) {
        stage("deploy") {
            sh('chmod 777 build_and_publish.sh')
            sh('./build_and_publish.sh')
        }
    }
}
