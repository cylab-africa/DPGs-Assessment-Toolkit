# DPGs Assessment Toolkit

# Installation

### Clone the repository
```
git clone https://github.com/cylab-africa/MOSIP_Kubernetes_Assessment_Tool
```

# Setup
1. In `gvm/config/local.env` edit the `GVM_PASSWORD` environment variable on line 12 to set you own password and etit the timezone (TZ) variable.
2. Set the `SMTP_HOST`, `SMTP_MASQ` and `SMTP_PORT` variables with your SMTP server informations (optional)
3. In `main/main.env` set your timezone and the MOSIP console IP
4. In `Dockerfile`, edit the line `ENV ALL_IP="ip1 ip2 ip3"` where IP1, IP2, etc are the list of your MOSIP VMs IPs 
5. In gvm/Dockerfile edit the  `RUN echo "gvmuser:gvmpass" | chpasswd` line and replace gvm pass by a custom password


# Build and run

```
docker-compose up -d --build
docker ps
```
