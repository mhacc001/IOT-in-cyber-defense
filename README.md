# IoT Security Analysis — MQTT & mTLS Implementation

This project documents a hands-on IoT security analysis focused on MQTT protocol vulnerabilities and secure device communication. The work was completed as part of an externship with Hydroficient.

## Overview
The project evaluates common security weaknesses in IoT environments and demonstrates how to secure MQTT communication using TLS and mutual TLS (mTLS).

## Key Objectives
- Identify vulnerabilities in MQTT-based communication
- Implement TLS and mTLS for secure device authentication
- Validate certificate-based trust and connection security
- Simulate attack scenarios to test security controls

## Technical Implementation
- Configured an MQTT broker using Mosquitto
- Implemented TLS encryption using CA-signed certificates
- Enforced mutual TLS (mTLS) for client authentication
- Tested certificate validation, including:
  - Expired certificates
  - Incorrect Certificate Authority (CA)
  - Invalid client credentials
- Analyzed connection behavior and rejection scenarios

## Security Concepts Covered
- MQTT Protocol Security
- TLS / mTLS Encryption
- Certificate-Based Authentication
- Public Key Infrastructure (PKI)
- Secure Device Identity Management
- IoT Threat Modeling

## Tools & Technologies
- Mosquitto MQTT Broker
- Python (Paho-MQTT)
- OpenSSL
- Wireshark
- Linux Environment

## Key Takeaways
- IoT devices are highly vulnerable without proper authentication and encryption
- mTLS significantly improves device trust and communication security
- Certificate validation is critical to preventing unauthorized access
- Secure configuration of MQTT brokers is essential in production environments

## Repository Structure
- `/configs` — Mosquitto configuration files (TLS/mTLS)
- `/certs` — Certificate generation and testing files
- `/scripts` — Python scripts for testing MQTT connections
- `/tests` — Security test scenarios (valid, invalid, expired certs)

## Author
Marie Haccandy
