<br/>
<h1 align="center">
    <img alt="netorc logo" src="miscellaneous/landing/page/images/default-monochrome-black.png" width="400"/>
</h1>
<br/>
<p align="center">
<img src="https://badgen.net/badge/version/demo/green?icon=github" alt="netorc status"/>&nbsp;<a href="https://github.com/netorc-community/netorc/issues" 
><img src="https://badgen.net/github/open-issues/netorc-community/netorc" alt="netorc open issues" /></a>&nbsp;<a href="https://github.com/netorc-community/netorc/issues?q=is%3Aissue+is%3Aclosed+" 
><img src="https://badgen.net/github/closed-issues/netorc-community/netorc" alt="netorc closed issues" /></a></p>


<p align="center">NetORC lays the foundation for central network orchestration. It acts as an intermediary between your business support systems and the network automation tooling of your choice. By being tool agnostic, the project aims to enhance the adoption of network automation into other business functions through its simple-to-use REST API.</p>

## Project Goals

- Develop an open-source, vendor-agnostic network orchestrator with a REST API.
- Prioritize reliability and usability over speed.
- Provide a set of helpful add-ons to support the adoption of central orchestration.
- Enable queuing and feedback of task progress.

## Architectural Principles

- The orchestrator should lay the foundations for bespoke customization and improvement, rather than trying to be
  exhaustive.
- The orchestrator ought to facilitate the importation of automation scripts already in existence with minimal or no
  alteration required from the user.
- The orchestrator should be designed to abstract away technical details such it's REST API, security, and queuing
  framework, enabling the user to utilize the tool without requiring an understanding of these underlying technologies.

## Demo Quick Start

First, [download](https://docs.docker.com/get-docker/) and install 🐳 **Docker**. Engine version: 19.03.0 or higher is
required.

Next, clone the repository using the following command:

```bash
git clone -b demo https://github.com/netorc-community/netorc.git && cd netorc && mkdir logs
```

Finally, build the images and start the containers with:

```bash
docker compose -f docker-compose.dev.yml
```

Navigate to `localhost:8000/api`, congrats! 🎉. Documentation can be found at `/docs`
