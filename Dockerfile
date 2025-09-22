FROM ubuntu:20.04

WORKDIR /root

ENV TZ=Americas/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y software-properties-common git python3 python3-pip opam z3 wget pkg-config libgmp-dev libzmq3-dev maven openjdk-8-jdk libpcre3 libpcre3-dev
RUN opam init --disable-sandboxing

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./scripts ./scripts
RUN chmod +x ./scripts/install_pict.sh
RUN ./scripts/install_pict.sh
RUN chmod +x ./scripts/install_nv.sh
RUN ./scripts/install_nv.sh
RUN chmod +x ./scripts/install_cbgp.sh
RUN ./scripts/install_cbgp.sh
#RUN chmod +x ./scripts/install_batfish.sh
#RUN ./scripts/install_batfish.sh

# newer ntc-templates will have different folder structure
RUN git clone --depth 1 --branch v1.6.0 https://github.com/networktocode/ntc-templates.git

# clean up
RUN /bin/rm -rf ./scripts
RUN /bin/rm requirements.txt
RUN apt-get clean && apt-get autoclean && apt-get autoremove
RUN pip3 install --upgrade pip
RUN pip3 cache purge

# Build: 
#   docker build . -t metha
# or
#   docker build . -t dabg/metha
# 
# Run: 
#   docker run -it --name metha -v.:/root/metha dabg/metha
# then
#   python3 metha.py -p example-tests/tests-new/test0 run -s batfish
#
# using debugpy for remote debugging:
#   docker run -it --rm --name metha --network=host -v.:/root dabg/metha:latest /usr/bin/python3 metha.py -p example-tests/tests-new/test0 single-test -s nv
#
# now we need to hook up GNS somehow to let this python3 sees the GNS3 pid outside of the container. 
