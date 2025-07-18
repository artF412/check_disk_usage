import paramiko

def check_disk_via_ssh(ip, username, password, port=22):
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print(f"Connecting to {ip}...")
        ssh.connect(hostname=ip, port=port, username=username, password=password)

        # Run command "df -h"
        stdin, stdout, stderr = ssh.exec_command("df -h")

        # Read result
        output = stdout.read().decode()
        error = stderr.read().decode()

        # Close connecting
        ssh.close()

        if error:
            print(f"Error: {error}")
        else:
            print(f"Disk usage on {ip}:\n{output}")

    except Exception as e:
        print(f"Exception: {str(e)}")


# 🔧 How to use
if __name__ == "__main__":
    target_ip = "192.168.1.100"     # <== Edit IP
    username = "USERNAME"           # <== Enter User SSH
    password = "PASSWORD"           # <== Enter Pass

    check_disk_via_ssh(target_ip, username, password)
