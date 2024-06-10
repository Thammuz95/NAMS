# Thammuz 95 - May 3rd, 2024

# Import necessary functions from the other modules
from network_utils import backup_configuration, monitor_health, collect_logs, security_audit
from traffic_analysis import traffic_analysis


def main():
    """
    Main function to handle user arguments and coordinate network tasks.

    Parameters:
    None

    Returns:
    void: Executes the main program logic
    """
    # Sample device info dictionary for connecting to a network device
    device_info = {
        'device_type': 'cisco_ios',  # Type of device, e.g., Cisco IOS
        'host': '192.168.1.1',  # IP address of the device
        'username': 'admin',  # Username for device login
        'password': 'password',  # Password for device login
        'secret': 'secret',  # Enable secret (if required)
    }

    # Perform network tasks
    backup_configuration(device_info)  # Backup the device configuration
    monitor_health(device_info)  # Monitor the health of the device
    collect_logs(device_info)  # Collect logs from the device
    security_audit(device_info)  # Perform a security audit on the device

    # Perform traffic analysis
    traffic_analysis()  # Capture and analyze network traffic


if __name__ == "__main__":
    main()
