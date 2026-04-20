# n8n Production Deployment: AWS and Kubernetes Best Practices

Source: Running n8n on AWS EC2, ECS, or Kubernetes: Best Practices by Business Compass LLC
URL: https://youtube.com/watch?v=lQom4XwXohs
Extracted: 2026-04-20
Businesses: bridgeworks

## What it is
A technical guide covering best practices for running n8n in production on AWS infrastructure. Covers the tradeoffs between EC2 (simple, single server), ECS (containerized, managed), and Kubernetes (scalable, complex).

## How it works
1. EC2: cheapest option, good for single-client or testing; manual updates required
2. ECS: Docker-based, easier scaling, integrates with AWS load balancer
3. Kubernetes: best for multi-tenant or high-volume; steep setup cost
4. Use environment variables and secrets manager for credentials
5. Set up persistent volume for n8n data (SQLite or PostgreSQL)

## BridgeWorks application
As BridgeWorks grows its n8n-based automation delivery, self-hosting n8n on AWS will cut costs versus n8n Cloud. EC2 is the right starting point for the first 5-10 clients. This video is a reference for when BridgeWorks hits the threshold where self-hosting saves money. Watch before making infrastructure decisions.
