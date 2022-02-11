
The docker compose up command runs all of the containers on the same docker network.

Be sure to run it in the root directory.

This allows them to talk to eachother via their container names instead of IP addresses or localhost.

The api will run on the flask dev server in the background.

The api_input app starts up but to get into a terminal, you need to open a new terminal and enter:

docker exec -it api_tester /bin/bash
