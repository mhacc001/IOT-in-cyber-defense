import time

count = 1

print("Starting device: GM-HYDROLOGIC-01")
print("Location: main-building")
print("Publishing sensor data...")
print("--------------------------------")

while True:
    print(f"[{count}] Pressure: 82 PSI, Flow: 41 gal/min")
    count += 1
    time.sleep(2)