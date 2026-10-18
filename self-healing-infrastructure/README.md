Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible
Overview
This project demonstrates a self-healing infrastructure that automatically detects service outages and performs automated recovery using monitoring, alerting, and configuration management tools.

Technologies Used
Docker
Prometheus
Alertmanager
Blackbox Exporter
Flask Webhook
Ansible
Ubuntu (WSL2)
Git & GitHub
Architecture
+-----------+
|   NGINX   |
+-----------+
      |
      v
+-------------------+
| Blackbox Exporter |
+-------------------+
      |
      v
+------------+
| Prometheus |
+------------+
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
+----------------+
| Restart NGINX  |
+----------------+
How It Works
NGINX runs inside a Docker container.
Blackbox Exporter continuously checks NGINX availability.
Prometheus scrapes metrics every few seconds.
When NGINX becomes unavailable, Prometheus triggers an alert.
Alertmanager receives the alert.
Alertmanager sends a webhook notification.
Flask webhook receives the notification.
Webhook triggers Ansible playbook.
Ansible automatically restarts the NGINX container.
Project Structure
self-healing-infrastructure
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
└── README.md
Deployment
Start services:

docker compose up -d
Verify:

docker ps
Test Self-Healing
Stop NGINX:

docker stop nginx
Prometheus detects failure.

Alertmanager sends notification.

Webhook invokes Ansible.

Ansible restarts NGINX automatically.

Verify:

docker ps
NGINX should be running again.

Screenshots
1. Docker Containers Running
Add screenshot: screenshots/docker-ps.png

2. Prometheus Targets
Add screenshot: screenshots/prometheus-targets.png

3. Alert Firing
Add screenshot: screenshots/nginxdown-firing.png

4. Alertmanager Alert
Add screenshot: screenshots/alertmanager-alerts.png

5. Webhook Triggered
Add screenshot: screenshots/webhook-triggered.png

6. Auto Recovery
Add screenshot: screenshots/nginx-restarted.png

Key Learning Outcomes
Infrastructure Monitoring
Alert Management
Event-Driven Automation
Linux Administration
Docker Containerization
Self-Healing Systems
DevOps Fundamentals

Author
Prajwal
