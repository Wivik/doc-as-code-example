FROM pandoc/extra:latest-ubuntu

RUN apt-get update && apt-get install default-jre graphviz plantuml -y && apt-get clean autoclean && apt-get autoremove --yes && rm -rf /var/lib/{apt,dpkg,cache,log}/
