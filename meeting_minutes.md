Meeting minutes 10/2/2025

Standup reports: little forward progress due to some blockers
- Michael: formatting the raw data text files
- Mihir: authorization blocking the execution of Metha
- Anish: gns3server giving issues

Logistical updates:
- Anish joining Metha test code deletion process so we can remove framework dependencies

Pushing out manual topology creations for until after Metha code is no longer a testing framework.

In __main__ there is code that waits for remote attach client for debug purposes.

How to fix authentication issues:

GNS3 settings -> server tab -> disable authentication

docker run -it --rm --name metha --network=host -v.:/root dabg/metha:20250921 /usr/bin/python3 run_single_gns3.py -p example-tests/tests-new/test0/