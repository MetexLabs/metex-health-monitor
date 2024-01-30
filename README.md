    ███╗   ███╗███████╗████████╗███████╗██╗  ██╗    ██╗      █████╗ ██████╗ ██████╗
    ████╗ ████║██╔════╝╚══██╔══╝██╔════╝╚██╗██╔╝    ██║     ██╔══██╗██╔══██╗██╔════╝
    ██╔████╔██║█████╗     ██║   █████╗   ╚███╔╝     ██║     ███████║██████╦╝╚█████╗
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══╝   ██╔██╗     ██║     ██╔══██║██╔══██╗ ╚═══██╗
    ██║ ╚═╝ ██║███████╗   ██║   ███████╗██╔╝╚██╗    ███████╗██║  ██║██████╦ ██████╔╝
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝
# GPU Health Monitor

## Overview

The GPU Health Monitor is a tool designed to provide real-time information about connected GPUs in a network. This tool is particularly useful for system administrators, developers, and users who want to monitor the health and performance of GPUs across multiple machines.

## Features

- **Real-time Monitoring**: The monitor continuously fetches and displays real-time information about connected GPUs.
  
- **Detailed GPU Information**: Gain insights into GPU model, temperature, usage, memory details, and more.

- **Network Connectivity**: Monitor GPUs across the network, making it easy to keep an eye on multiple machines from a central location.

## Running the Monitor on a WSL Env 

1. Clone the repository:
   ```bash
   git clone https://github.com/MetexLabs/metex-health-monitor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd metex-health-monitor
   ```
   
3. Navigate to the project directory:
   ```bash
   cd metex-health-monitor
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask Server
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```
5. Access the Web Browser
   ```bash
   http://localhost:5000
   ```  
      

## Alternate Usage ( More RELIABLE )

<details>
<summary><b>Running with Docker</b></summary>

```bash
git clone https://github.com/MetexLabs/metex-health-monitor.git
cd metex-health-monitor
docker-compose up --build -d
```
</details>


O: Explore real-time GPU information And usage across the network.

## Dependencies

- Python 3.x
- Flask
- NVIDIA System Management Interface (nvidia-smi)
