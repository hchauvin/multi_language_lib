FROM r-base:3.6.1

RUN pip install --upgrade conan

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y cmake libxml2-dev libcurl4-openssl-dev
RUN R -e "install.packages('devtools', repos = 'http://cran.us.r-project.org')"
