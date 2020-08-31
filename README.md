# **Team Name Generator**

**Resources:**

Link to Trello Board: [https://trello.com/b/0ba4ryhB/team-name-generator](https://trello.com/b/0ba4ryhB/team-name-generator)

Link to presentation: [https://docs.google.com/presentation/d/1-qkPSeRvVBQ76ULQ\_o\_-Dhd3Ke0ToMs74tFCF\_mbnaw/edit?pli=1#slide=id.p](https://docs.google.com/presentation/d/1-qkPSeRvVBQ76ULQ_o_-Dhd3Ke0ToMs74tFCF_mbnaw/edit?pli=1#slide=id.p)

**Brief**

As set by the client

To create an application that generates &quot;Objects&quot; upon a set of predefined rules.
 These &quot;Objects&quot; can be from whatever domain you wish.

You are required to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

This document encloses all the necessary steps that were taken to complete this brief. To do this, numerous tools and frameworks were used to create the back end of the web app, testing of the app, and the deployment of the web app.

Additional requirements of this project set by the client were as followed:

- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- This could also provide a record of any issues or risks that you faced creating your project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

**Initial approach of the project**

In consideration of the brief and requirements of the project, below is a streamlined approach of what I intended to include in the app, I felt as though the brief had greater focus on the deployment of the web app and so a simple program was initially proposed, this was as followed:

A web app that would produce a fortune of a sports team next game, based on services 2 and 3 a win, draw or loss would be chosen along with a final score of the game.

- Service 1 – The core service that would render the templates and persist data using a database.
- Service 2 - Generating random number (win, draw, loss)
- Service 3 – Generating random number (score)
- Service 4 – Object is produced based upon the results of services 2 &amp; 3 (fortune)

**Updated approach**

After a discussion with the client, the approach of the project was adjusted to make more creative use of both service 2 and 3, therefore the updated and chosen approach of the project was as followed:

- Service 1 – The core service that would render the templates and persist data using a database.
- Service 2 - Generate the first half of the team name (London, Manchester, Leeds)
- Service 3 – Generate a second half of the team name (chosen from a list of 15 possibilities)
- Service 4 – Object is produced based upon the results of services 2 &amp; 3 (team name and a slogan based upon the chosen city name)

**MoSCow Prioritization**

The MoSCoW method was used when deciding the prioritization of certain features within the application and decided what would or wouldn&#39;t be included. The original MoSCoW of the project can be seen below:

![image](https://user-images.githubusercontent.com/66956487/91771182-74036980-ebda-11ea-9683-176b784f6134.png)


**Project Tracking**

Trello was the chosen method when planning the project and tracking the progress of tasks set out. This was done to ensure a steady workflow and create an agile work frame where changes could be made through the production of the web app. This was necessary to allow for an agile workflow ensuring smaller tasks were being completed and this allowed for a structured approach when tackling the project. Below is the trello board used for this project:

![image](https://user-images.githubusercontent.com/66956487/91771247-939a9200-ebda-11ea-9360-0c869a5cb61e.png)

**Database Structure**

Below is an entity diagram showing the 4 services that was used for the project and how they interacted with each other to achieve the object being produced. This was used to visualise how the 4 services would work and to determine where the best location was for the database and how each service should function. This diagram is the updated version to the approach showing service 1 persisting data and displaying the jinja2 templates, service 2 and 3 persisting lists of data that would be chosen by random, and service 4 that would produce the slogan from a list dependent on the data received from service 1 that were gathered from services 2 and 3.

![image](https://user-images.githubusercontent.com/66956487/91771289-a4e39e80-ebda-11ea-8ff1-1ad283ec9f62.png)

**Testing**

Testing has become imperative when determining the success of a project. It cannot be reinforced the importance of carrying out relevant and sufficient tests to ensure that the work produced fulfils the needs required when being used and that is has the reliability to be used on multiple occasions to a point where bugs or issues do not interfere with the users experience. The tools used for testing the application was pytest when conducting unit tests. The nature of the project meant that 100% coverage on all 4 services would be expected to ensure they are all functioning and with no issues as this could have a significant knock on effect to the app&#39;s functionality. Below is the coverage reports of all 4 services.

![image](https://user-images.githubusercontent.com/66956487/91771329-b62cab00-ebda-11ea-9d28-3f33c8b541cb.png)

![image](https://user-images.githubusercontent.com/66956487/91771344-bc228c00-ebda-11ea-8540-3c1f33aa060c.png)

![image](https://user-images.githubusercontent.com/66956487/91771355-c04ea980-ebda-11ea-8fbc-f8f72e446828.png)

![image](https://user-images.githubusercontent.com/66956487/91771359-c3e23080-ebda-11ea-92ef-e895be4ef57c.png)

There was no major issues throughout the testing stage. More setup was required for service 1 due to the set up of a test database which is reflected on the greater number of statements tested to achieve the 100% coverage. I would have preferred to have just 1 coverage report for the application as a whole but due to the nature of the command use (pytest --cov application) there was an error due to there being an application folder in each service. Therefore, individual coverage reports have been produced.

**Technologies Used and Continuous Integration Pipeline**

Below is an image showing the Continuous Integration pipeline of the project depicting all the frameworks and tools used to complete the project successfully.

![image](https://user-images.githubusercontent.com/66956487/91771383-d2304c80-ebda-11ea-9b84-ff1379a105c7.png)

The chosen CI server for this project was Jenkins, this was the chosen CI for my previous project and the reason for this is due to its official plugins that can be downloaded by default to support the server. An example of this is to produce testing reports with the use of pytest that can be seen while the build is produced. Further frameworks of the pipeline included Git for the management of code being pushed and allowed for the agile work where branching could be used to complete particular areas of the production, once completed was then pushed to the master branch when fully functioning.

Docker was used to produce a swarm that allowed for the manager and 2 worker nodes to join and carry out load balancing. Docker hub was also used to allow for the storage of container images that would be used later to deploy the program. Ansible was chosen to produce the configuration of the program and the deployment. The automation tool allowed for the use of **scripts** to carry out the set up that ensures the ease of later deployment with no further configuration needed. **Nginx** was used as the web server to carry out both the role load balancing and serving static content.

To deploy the program the process of integrating automation was utilised wherever feasible and most convenient for later deployment. This was done with the use of a **Jenkins pipeline** build that would run off a **Jenkinsfile**. The reasons as to why this method has been chosen is it allows for smoother releases if changes were to be made and means that no further configuration is needed once the initial setup has been completed and successfully deploys the program to a live environment. The stages used for this pipeline was: Configuration, Test, Build, and Deploy.

The configure stage allowed for all the packages and dependencies required such as ansible to be installed on the required VM&#39;s for the deployment of the program. This also involved **Ansible** running the playbook.yaml configured that means roles for the docker swarm, manager node and worker nodes was carried out to initialise the swarm and set up of a git and docker repository.

The build stage allowed for production of new docker images to be created and pushed to the desired **docker hub** repository. However, to ensure zero conflicts with previous images all images are removed before the production of new images. This was done with the use of **docker compose** to simplify the process

The testing stage as previous explained allowed for the program to be reliable and confident that there would be no bugs or issues when deployed to a live environment. This was carried out with the use of **pytest** mock tests and production coverage reports of each service, all of which have 100% coverage.

The deploy stage allows for the program to get deployed to a live environment. To accomplish this docker stack was used when in the manager node that allows for the management of a cluster of docker containers with the use of the **docker swarm** initiated in the configure stage. This docker stack used the images previously pushed to the chosen docker hub repository.

**Risk Assessment**

The risk assessment produced for the project can be found below. It attempts to cover all risks or threats involved and what would be done to eliminate or reduce the impact of these threats. The risk assessment shown below is latest version that was added to as the project progressed and introduced new risks.

![image](https://user-images.githubusercontent.com/66956487/91771392-d65c6a00-ebda-11ea-8732-6713dad28c47.png)

**Future Improvements &amp; Bugs**

The only current known issue with the program is that every time there is an implementation triggering a rebuild, the database is cleared and rebuilt meaning any teams generated before the rebuild after removed.

An account feature could also be setup to allow for a user to have stored team names generated on an individual account only.

The most recent team generated could also potentially be shown on the generate page than having to go to all team&#39;s page to see the most recent generated team name.


**Author**

Jason Worger


**Acknowledgements**

QA Academy for the teaching of the skills needed to carry out this project successfully.