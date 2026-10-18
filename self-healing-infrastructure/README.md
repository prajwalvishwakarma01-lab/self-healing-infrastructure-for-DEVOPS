# 🚀 Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

## 📖 Overview

This project demonstrates a complete self-healing infrastructure that automatically detects service failures and performs automatic recovery without human intervention.

The project uses Prometheus for monitoring, Alertmanager for alert routing, Flask Webhooks for event handling, and Ansible for automated remediation.

---

## 🎯 Project Objective

Build an automated infrastructure capable of:

- Detecting service outages
- Triggering alerts automatically
- Executing recovery actions
- Restoring services without manual intervention

---

## 🛠️ Tech Stack

| Category | Tool |
|-----------|--------|
| Monitoring | Prometheus |
| Alerting | Alertmanager |
| Health Checks | Blackbox Exporter |
| Automation | Ansible |
| Webhook Service | Flask |
| Containerization | Docker |
| Operating System | Ubuntu (WSL2) |
| Version Control | Git & GitHub |

---

## 🏗️ Architecture

```text
                 +-------------+
                 |   NGINX     |
                 +-------------+
                        |
                        v
           +-----------------------+
           | Blackbox Exporter     |
           +-----------------------+
                        |
                        v
                 +-------------+
                 | Prometheus  |
                 +-------------+
                        |
                        v
                 +--------------+
                 | Alertmanager |
                 +--------------+
                        |
                        v
                 +----------+
                 | Webhook  |
                 +----------+
                        |
                        v
                 +----------+
                 | Ansible  |
                 +----------+
                        |
                        v
             +--------------------+
             | Restart NGINX       |
             +--------------------+
```

---

## ⚙️ Workflow

### Normal State

1. NGINX application runs inside Docker.
2. Blackbox Exporter continuously checks application health.
3. Prometheus scrapes metrics every few seconds.
4. Alertmanager waits for alerts.

### Failure State

When NGINX becomes unavailable:

```text
NGINX Down
      ↓
Blackbox Detection
      ↓
Prometheus Alert
      ↓
Alertmanager Notification
      ↓
Webhook Trigger
      ↓
Ansible Playbook
      ↓
NGINX Restart
```

---

## 📂 Project Structure

```text
self-healing-infrastructure/
│
├── alertmanager/
│   └── alertmanager.yml
│
├── ansible/
│   └── restart-nginx.yml
│
├── blackbox/
│   └── blackbox.yml
│
├── prometheus/
│   ├── prometheus.yml
│   └── alert.rules.yml
│
├── webhook/
│   └── webhook.py
│
├── screenshots/
│
├── docker-compose.yml
│
├── .gitignore
│
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/self-healing-infrastructure.git

cd self-healing-infrastructure
```

### Start Infrastructure

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

---

## 📈 Prometheus

Open:

```text
http://localhost:9090
```

Check:

```text
Status → Targets
```

Ensure all targets show:

```text
UP
```

---

## 🚨 Alertmanager

Open:

```text
http://localhost:9093
```

Alertmanager receives alerts from Prometheus and forwards them to the configured webhook.

---

## 🧪 Self-Healing Test

### Stop NGINX

```bash
docker stop nginx
```

### Expected Flow

```text
NginxDown Alert
        ↓
Alertmanager
        ↓
Webhook
        ↓
Ansible
        ↓
docker restart nginx
```

### Verify Recovery

```bash
docker ps
```

NGINX should automatically come back online.

---

## 📸 Screenshots

### Docker Containers Running

screenshots/01-docker-containers.png

---

### Prometheus Targets

screenshots/02-prometheus-targets.png

---

### Alert Firing

screenshots/03-alert-firing.png

---

### Alertmanager

screenshots/04-alertmanager.png

---

### Webhook Triggered

screenshots/05-webhook-triggered.png

---

### Automatic Recovery

screenshots/06-nginx-restarted.png

---

## 💡 Key Learning Outcomes

Through this project, I learned:

- Docker Containerization
- Infrastructure Monitoring
- Alert Management
- Service Health Checks
- Webhook Integration
- Ansible Automation
- Linux Administration
- Incident Response Automation
- Self-Healing Infrastructure Design
- DevOps Troubleshooting and Debugging

---

## 🎓 Resume Description

### Self-Healing Infrastructure using Prometheus, Alertmanager & Ansible

Built a self-healing infrastructure capable of automatically detecting service failures and performing corrective actions. Integrated Prometheus, Alertmanager, Flask Webhooks, Blackbox Exporter, and Ansible to automate NGINX service recovery. Implemented event-driven monitoring and remediation workflows within a Dockerized environment.

---

## 🔮 Future Improvements

- Grafana Dashboard Integration
- Email Notifications
- Slack / Microsoft Teams Alerts
- Kubernetes Deployment
- Auto Scaling Policies
- Multi-Service Recovery Workflows

---

## 👨‍💻 Author

**Prajwal**

DevOps | Linux | Docker | Automation | Monitoring

---
