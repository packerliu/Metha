docker run --name metha-system -it -p 5678:5678 --network host \
--mount type=bind,source="$(pwd)"/,target=/root/metha \
metha:latest
