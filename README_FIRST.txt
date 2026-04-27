PROJECT 4 QUICK START (Mac)

1) Open Terminal and run:
mkdir -p ~/Documents/hydroficient-project/project-04
cd ~/Documents/hydroficient-project/project-04

2) Copy these files into that folder:
- generate_certs.py
- publisher_tls.py
- subscriber_tls.py
- experiment_runner.py
- mosquitto_insecure.conf
- mosquitto_tls.conf

3) Install Python packages if needed:
pip3 install cryptography paho-mqtt

4) Generate certificates:
python3 generate_certs.py

5) Verify certs folder exists:
ls certs/

6) Stop old Mosquitto:
pkill mosquitto

7) Start secure broker (leave this terminal open):
mosquitto -c mosquitto_tls.conf -v

8) Open a NEW terminal and test insecure connection fails:
cd ~/Documents/hydroficient-project/project-04
mosquitto_sub -h localhost -p 8883 -t 'test/#'

Expected: Error: A TLS error occurred.

9) In that same terminal after the test, run subscriber:
python3 subscriber_tls.py

10) Open a THIRD terminal and run publisher:
cd ~/Documents/hydroficient-project/project-04
python3 publisher_tls.py

11) Take screenshot showing:
- Broker terminal says: Opening TLS listener on port 8883
- Subscriber terminal says: Connected successfully over TLS!
- Subscriber terminal receiving messages

12) If Python says module not found:
pip3 install cryptography paho-mqtt

13) If Mosquitto says address already in use:
pkill mosquitto

14) If certificate verify fails:
Make sure you ran python3 generate_certs.py first and that certs/ca.pem exists.
