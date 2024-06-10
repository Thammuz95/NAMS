import netmiko
from alert_utils import send_alert


def backup_configuration(device_info):
    """
    Backs up the configuration of the specified network device.

    Parameters:
    device_info (dict): Dictionary containing device connection information

    Returns:
    void: Saves the configuration to a file
    """
    try:
        # Establish SSH connection to the device
        connection = netmiko.ConnectHandler(**device_info)

        # Send command to get the running configuration
        config = connection.send_command("show running-config")

        # Define the filename for saving the configuration
        filename = f"{device_info['host']}_config_backup.txt"

        # Save the configuration to a file
        with open(filename, "w") as f:
            f.write(config)

        # Disconnect from the device
        connection.disconnect()
        print(f"Configuration backed up to {filename}")
    except netmiko.NetMikoTimeoutException as e:
        print(f"Connection timed out: {e}")
    except netmiko.NetMikoAuthenticationException as e:
        print(f"Authentication failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def monitor_health(device_info):
    """
    Monitors the health of the specified network device and sends an alert if thresholds are exceeded.

    Parameters:
    device_info (dict): Dictionary containing device connection information

    Returns:
    void: Sends email alerts if health thresholds are exceeded
    """
    try:
        # Establish SSH connection to the device
        connection = netmiko.ConnectHandler(**device_info)

        # Send command to get CPU and memory usage
        cpu_usage = connection.send_command("show processes cpu")
        mem_usage = connection.send_command("show processes memory")

        # Placeholder thresholds for alerts
        cpu_threshold = 80
        mem_threshold = 80

        # Parse usage data (simplified example)
        cpu_value = int(cpu_usage.split()[-1].replace('%', ''))
        mem_value = int(mem_usage.split()[-1].replace('%', ''))

        # Send alert if CPU usage exceeds threshold
        if cpu_value > cpu_threshold:
            send_alert("CPU Usage Alert", f"CPU usage is at {cpu_value}% on {device_info['host']}")

        # Send alert if memory usage exceeds threshold
        if mem_value > mem_threshold:
            send_alert("Memory Usage Alert", f"Memory usage is at {mem_value}% on {device_info['host']}")

        # Disconnect from the device
        connection.disconnect()
    except netmiko.NetMikoTimeoutException as e:
        print(f"Connection timed out: {e}")
    except netmiko.NetMikoAuthenticationException as e:
        print(f"Authentication failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def collect_logs(device_info):
    """
    Collects logs from the specified network device and saves them locally.

    Parameters:
    device_info (dict): Dictionary containing device connection information

    Returns:
    void: Saves logs to a local file
    """
    try:
        # Establish SSH connection to the device
        connection = netmiko.ConnectHandler(**device_info)

        # Send command to get the logs
        logs = connection.send_command("show log")

        # Define the filename for saving the logs
        filename = f"{device_info['host']}_logs.txt"

        # Save the logs to a file
        with open(filename, "w") as f:
            f.write(logs)

        # Disconnect from the device
        connection.disconnect()
        print(f"Logs collected to {filename}")
    except netmiko.NetMikoTimeoutException as e:
        print(f"Connection timed out: {e}")
    except netmiko.NetMikoAuthenticationException as e:
        print(f"Authentication failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def security_audit(device_info):
    """
    Performs a security audit on the specified network device and saves the results.

    Parameters:
    device_info (dict): Dictionary containing device connection information

    Returns:
    void: Saves audit results to a file
    """
    try:
        # Establish SSH connection to the device
        connection = netmiko.ConnectHandler(**device_info)

        # Send command to perform the security audit
        audit_result = connection.send_command("show security audit")

        # Define the filename for saving the audit results
        filename = f"{device_info['host']}_audit.txt"

        # Save the audit results to a file
        with open(filename, "w") as f:
            f.write(audit_result)

        # Disconnect from the device
        connection.disconnect()
        print(f"Audit results saved to {filename}")
    except netmiko.NetMikoTimeoutException as e:
        print(f"Connection timed out: {e}")
    except netmiko.NetMikoAuthenticationException as e:
        print(f"Authentication failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
