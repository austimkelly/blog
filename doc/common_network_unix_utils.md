Some basic tools for network troubleshooting on Unix systems. These are essential baseline tools for DNS/network administration, pen testing, and general network troubleshooting.

| Tool         | Summary                                                         | Example                                    |
|--------------|-----------------------------------------------------------------|--------------------------------------------|
| `traceroute` | Traces the route packets take to a destination.                  | `traceroute example.com`                   |
| `netstat`    | Displays network connections, routing tables, and interface stats.| `netstat -an`                              |
| `dig`        | A flexible DNS querying tool for network admins.                 | `dig example.com ANY`                      |
| `whoami`     | Displays the username associated with the current session.        | `whoami`                                   |
| `nmap`       | Scans networks for open ports, services, and vulnerabilities.    | `nmap -Pn example.com`                     |
| `curl`       | A command-line tool for transferring data with URL syntax.       | `curl https://example.com`                 |
| `netcat`     | A networking utility for reading/writing data across network connections. | `nc -zv example.com 80`              |
| `ssh`        | Securely connects to a remote computer or server.                | `ssh user@example.com`                     |
| `ping`       | Sends ICMP echo requests to a host to check network connectivity.| `ping example.com`                         |
| `uname`      | Displays system information about the current machine.            | `uname -a`                                 |
| `ifconfig`   | Displays network interface configuration information.             | `ifconfig`                                 |