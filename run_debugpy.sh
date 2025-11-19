if [ "$( docker container inspect -f '{{.State.Status}}' $container_name )" = "running" ]; 
then [ "$( docker container stop $container_name; docker container prune --force )"]
fi

docker run -it --rm --name metha -p 5678:5678 --network=host -v.:/root dabg/metha:20250921 /usr/bin/python3 -m debugpy --listen 0.0.0.0:5678 --wait-for-client metha.py -p example-tests/tests-new/test0/ single-test -s nv