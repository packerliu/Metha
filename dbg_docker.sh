docker run --name metha-dbg -it -p 5678:5678 --network host \
--mount type=bind,source="$(pwd)"/,target=/root/metha \
metha:dbg
