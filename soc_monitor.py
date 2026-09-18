# soc_monitor.py

import os
import time

# --- Simulate a log file for demonstration ---
# In a real Security Operations Center (SOC), logs would stream from various sources
# (firewalls, servers, endpoints, applications). For this example, we'll use a simple dummy log file.
LOG_FILE_NAME = "security_logs.log"

# Define suspicious patterns that a SOC analyst might look for.
# These represent simplified threat indicators that a SOC's Security Information and Event Management (SIEM)
# system would typically process using rules and correlation engines.
SUSPICIOUS_PATTERNS = {
    "FAILED_LOGIN": ["failed login", "authentication failure", "invalid credentials"],
    "MALWARE_ALERT": ["malware detected", "virus alert", "trojan found"],
    "UNAUTHORIZED_ACCESS": ["unauthorized access", "permission denied", "access violation"],
    "PHISHING_ATTEMPT": ["phishing email", "suspicious link clicked"],
    "RANSOMWARE_INDICATOR": ["encrypted files", "ransom note"],
    "DATA_EXFILTRATION": ["data transfer out", "large upload to external IP"]
}

def create_dummy_log_file():
    """Creates a dummy log file with mixed benign and suspicious entries for the demo."""
    if os.path.exists(LOG_FILE_NAME):
        # If the file exists, assume user might have modified it or it's a rerun.
        # We won't overwrite it automatically.
        print(f"Using existing log file: {LOG_FILE_NAME}")
        return

    print(f"Creating dummy log file: {LOG_FILE_NAME}")
    log_entries = [
        "2023-10-27 10:00:01 INFO User 'john.doe' logged in from 192.168.1.100",
        "2023-10-27 10:00:05 WARNING Failed login attempt for 'admin' from 203.0.113.45", # FAILED_LOGIN detected
        "2023-10-27 10:00:10 INFO System health check passed.",
        "2023-10-27 10:00:15 ERROR Malware detected in 'C:\\temp\\malicious.exe' on host 'SERVER01'", # MALWARE_ALERT detected
        "2023-10-27 10:00:20 INFO User 'jane.smith' accessed document 'report.docx'",
        "2023-10-27 10:00:25 CRITICAL Unauthorized access attempt to database 'prod_db' from 10.0.0.5", # UNAUTHORIZED_ACCESS detected
        "2023-10-27 10:00:30 WARNING User 'marketing_user' clicked on a suspicious link in a phishing email.", # PHISHING_ATTEMPT detected
        "2023-10-27 10:00:35 INFO Firewall blocked connection from 1.2.3.4",
        "2023-10-27 10:00:40 ERROR Multiple files encrypted with '.crypt' extension on 'FILESVR02'. Ransom note found.", # RANSOMWARE_INDICATOR detected
        "2023-10-27 10:00:45 INFO User 'john.doe' logged out.",
        "2023-10-27 10:00:50 ALERT Large data transfer out to external IP 185.199.108.153", # DATA_EXFILTRATION detected
        "2023-10-27 10:00:55 INFO Regular system backup completed successfully.",
        "2023-10-27 10:01:00 WARNING Authentication failure for 'guest' from 172.16.0.1" # FAILED_LOGIN detected
    ]
    with open(LOG_FILE_NAME, "w") as f:
        for entry in log_entries:
            f.write(entry + "\n")

def analyze_log_entry(log_line):
    """
    Analyzes a single log line for predefined suspicious patterns.
    This function simulates the detection capabilities of a SOC.
    In a real SOC, this would involve more sophisticated SIEM rules,
    correlation engines, and integration with threat intelligence feeds.
    """
    detected_threats = []
    for threat_type, patterns in SUSPICIOUS_PATTERNS.items():
        for pattern in patterns:
            if pattern.lower() in log_line.lower():
                detected_threats.append(threat_type)
                # In a real system, we might stop at the first match or
                # prioritize certain threats. For simplicity, we collect all.
    return detected_threats

def simulate_soc_monitoring():
    """
    Simulates a SOC monitoring process by reading a log file
    and alerting on suspicious activities, mimicking the core function
    of identifying and responding to cyber threats.
    """
    print("--- Starting SOC Log Monitoring Simulation ---")
    print(f"Monitoring log file: {LOG_FILE_NAME}\n")

    if not os.path.exists(LOG_FILE_NAME):
        print(f"Error: Log file '{LOG_FILE_NAME}' not found. Please ensure it exists or run create_dummy_log_file().")
        return

    incident_count = 0
    with open(LOG_FILE_NAME, "r") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            detected_threats = analyze_log_entry(line)

            if detected_threats:
                incident_count += 1
                # When a suspicious pattern is found, an 'incident' is generated.
                # This is a critical step in a SOC's workflow.
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] --- INCIDENT DETECTED! ---")
                print(f"  Log Line ({line_num}): {line}")
                print(f"  Threat Type(s): {', '.join(detected_threats)}")
                # This is a simplified 'incident response' action. A real SOC would
                # trigger automated alerts, open tickets in an Incident Response Platform (IRP),
                # enrich data, potentially isolate systems, and involve human analysts.
                print("  Suggested Action: Investigate immediately, escalate to Tier 2 analyst.")
                print("-" * 50)
            # Simulate real-time monitoring by pausing briefly
            time.sleep(0.05)

    if incident_count == 0:
        print("No suspicious activities detected in the log file.")
    else:
        print(f"\n--- Monitoring complete. Total incidents detected: {incident_count} ---")
        print("This simulation demonstrates how a SOC continuously monitors logs to identify and alert on potential security threats.")

if __name__ == "__main__":
    create_dummy_log_file() # Ensure the log file exists for the demo
    simulate_soc_monitoring()
