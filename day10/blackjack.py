def jobnameparts = JOB_NAME.tokenize('/') as String[]
def jobconsolename = jobnameparts[0]
pipeline {
  agent any
  parameters
  {
    string(name: 'DEPLOYMENT', defaultValue: 'NO', description: 'Deploy this build ( YES or NO) --- Default value is NO ----')   
    
  }
  environment {
    PROJECT_NAME = "${jobconsolename}"
    DOMAIN_NAME = "${BRANCH_NAME}.${jobconsolename}.blackbox.nobroker.in"
    STACK_NAME = "${jobconsolename}-${BRANCH_NAME}"
    DEPLOY = "${DEPLOYMENT}"
  }
  stages {
    stage('Build image') {
      steps {
        script {
          // Build the jars
          withCredentials([usernamePassword(credentialsId: 'Bitbucket', usernameVariable: 'BITBUCKET_USERNAME', passwordVariable: 'BITBUCKET_PASSWORD')]) {
            checkout scm
            ////Packing the jars


            ///copying 
            sh "echo this stage  is passed"
          
          }
        }
      }
    }
    stage('Docker Build and Push') {
      steps {
        script {
          ///building docker image
            withCredentials([usernamePassword(credentialsId: 'hoodrepo', usernameVariable: 'HOODREPO_USERNAME', passwordVariable: 'HOODREPO_PASSWORD')]) {
            sh '''
            sudo docker login http://repository.nobrokerhood.com:9093 -u $HOODREPO_USERNAME -p $HOODREPO_PASSWORD
            cd /var/jenkins_home/workspace/${PROJECT_NAME}_${BRANCH_NAME}/
            sudo docker build -f devops/Dockerfile_blackbox . -t repository.nobrokerhood.com:9093/hood-blackbox/${BRANCH_NAME}:${BUILD_NUMBER} -t repository.nobrokerhood.com:9093/hood-blackbox/${BRANCH_NAME}:latest
            sudo docker push repository.nobrokerhood.com:9093/hood-blackbox/${BRANCH_NAME}:${BUILD_NUMBER}
            sudo docker push repository.nobrokerhood.com:9093/hood-blackbox/${BRANCH_NAME}:latest
            echo pushed
            
              '''
            }
        }
      }
    }
    
    stage('folder') {
       when { 
         environment name:'DEPLOY', value: 'YES' 
       }
       steps {
         script {
            sh "echo this stage  is passed"
         }
       }
    }
    stage('Get portainer JWT Token') {
      when { 
        environment name:'DEPLOY', value: 'YES' 
      }
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'Portainer', usernameVariable: 'PORTAINER_USERNAME', passwordVariable: 'PORTAINER_PASSWORD')]) {
              def json = """
                  {"Username": "$PORTAINER_USERNAME", "Password": "$PORTAINER_PASSWORD"}
              """
              def jwtResponse = httpRequest acceptType: 'APPLICATION_JSON', contentType: 'APPLICATION_JSON', validResponseCodes: '200', httpMode: 'POST', ignoreSslErrors: true, consoleLogResponseBody: true, requestBody: json, url: "http://portainer:9000/api/auth"
              def jwtObject = new groovy.json.JsonSlurper().parseText(jwtResponse.getContent())
              env.JWTTOKEN = "Bearer ${jwtObject.jwt}"
          }
        }
        echo "${env.JWTTOKEN}"
      }
    }
    stage('Delete old Stack') {
      when { 
        environment name:'DEPLOY', value: 'YES' 
      }
      steps {
        script {
          // Get all stacks
          String existingStackId = ""
          if("true") {
            def stackResponse = httpRequest httpMode: 'GET', ignoreSslErrors: true, url: "http://portainer:9000/api/stacks", validResponseCodes: '200', consoleLogResponseBody: true, customHeaders:[[name:"Authorization", value: env.JWTTOKEN ], [name: "cache-control", value: "no-cache"]]
            def stacks = new groovy.json.JsonSlurper().parseText(stackResponse.getContent())
            stacks.each { stack ->
              if(stack.Name == "${PROJECT_NAME}-${BRANCH_NAME}") {
                existingStackId = stack.Id
              }
            }
          }
          if(existingStackId?.trim()) {
            // Delete the stack
            def stackURL = """
              http://portainer:9000/api/stacks/$existingStackId
            """
            httpRequest acceptType: 'APPLICATION_JSON', validResponseCodes: '204', httpMode: 'DELETE', ignoreSslErrors: true, url: stackURL, customHeaders:[[name:"Authorization", value: env.JWTTOKEN ], [name: "cache-control", value: "no-cache"]]
          }
        }
      }
    }
    stage('Deploy new stack to Portainer') {
      when { 
        environment name:'DEPLOY', value: 'YES' 
      }
      steps {
        script {
          sh "sleep 15s"
          def createStackJson = ""
          // Stack does not exist
          // Generate JSON for when the stack is created
          withCredentials([usernamePassword(credentialsId: 'Bitbucket', usernameVariable: 'BITBUCKET_USERNAME', passwordVariable: 'BITBUCKET_PASSWORD')]) {
            def swarmResponse = httpRequest acceptType: 'APPLICATION_JSON', validResponseCodes: '200', httpMode: 'GET', ignoreSslErrors: true, consoleLogResponseBody: true, url: "http://portainer:9000/api/endpoints/1/docker/swarm", customHeaders:[[name:"Authorization", value: env.JWTTOKEN ], [name: "cache-control", value: "no-cache"]]
            def swarmInfo = new groovy.json.JsonSlurper().parseText(swarmResponse.getContent())
            createStackJson = """
              {"Name": "${PROJECT_NAME}-${BRANCH_NAME}", "SwarmID": "$swarmInfo.ID", "RepositoryURL": "https://bitbucket.org/nobroker-repos/sc/", "RepositoryReferenceName": "refs/heads/${BRANCH_NAME}", "ComposeFilePathInRepository": "devops/docker-compose-blackbox.yaml", "RepositoryAuthentication": true, "RepositoryUsername": "$BITBUCKET_USERNAME", "RepositoryPassword": "$BITBUCKET_PASSWORD", "Env": [ {"name": "DOMAIN", "value": "${BRANCH_NAME}.${PROJECT_NAME}" }, {"name": "ROUTER", "value": "${BRANCH_NAME}-${PROJECT_NAME}" }, {"name": "API_BUILD", "value": "${BUILD_NUMBER}"}, {"name": "BRANCH_NAME", "value": "${BRANCH_NAME}"} ] }
            """
          }
          if(createStackJson?.trim()) {
            httpRequest acceptType: 'APPLICATION_JSON', contentType: 'APPLICATION_JSON', validResponseCodes: '200', httpMode: 'POST', ignoreSslErrors: true, consoleLogResponseBody: true, requestBody: createStackJson, url: "http://portainer:9000/api/stacks?method=repository&type=1&endpointId=1", customHeaders:[[name:"Authorization", value: env.JWTTOKEN ], [name: "cache-control", value: "no-cache"]]
          }
        }
      }
    }
    stage('Setting stack expiration timer') {
      when { 
        environment name:'DEPLOY', value: 'YES' 
      }
      steps {
        script {
          sh "echo this stage  is passed"
        }

      }
    }
  }
  post {
    success {
      slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")

    }

    failure {
      slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
    }
  }
}
