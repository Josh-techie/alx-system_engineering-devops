# Secured and Monitored Web Infrastructure

![Image of a secured and monitored infrastructure](https://ibb.co/NT2TQ8G)

## Description
	This is a 3-server web infrastructure that is secured, monitored, and serves encrypted traffic.

## Specifics About This Infrastructure

### Purpose of Firewalls
	The firewalls are in place to protect the network, specifically the web servers, from unwanted and unauthorized users. They act as intermediaries between the internal and external networks and block incoming traffic that matches certain criteria.

### Purpose of SSL Certificate
	The SSL certificate serves to encrypt the traffic between the web servers and the external network. This encryption prevents man-in-the-middle attacks (MITM) and network sniffers from intercepting sensitive information. SSL certificates ensure privacy, data integrity, and server identification.

### Purpose of Monitoring Clients
	The monitoring clients are responsible for monitoring the servers and the external network. They analyze server performance and operations, measure overall health, and alert administrators if servers are not performing as expected. The monitoring tool observes server behavior, providing key metrics and conducting tests for accessibility, response time, and error detection (e.g., corrupt/missing files, security vulnerabilities).

## Issues With This Infrastructure

### SSL Termination at Load Balancer Level
	Terminating SSL at the load balancer level would leave the traffic between the load balancer and the web servers unencrypted, potentially posing security risks.

### Single MySQL Server
	Having only one MySQL server is problematic as it is not scalable and can act as a single point of failure for the entire web infrastructure. Redundancy and failover mechanisms should be considered for improved reliability.

### Identical Server Components
	Using servers with identical components can lead to resource contention, including CPU, memory, and I/O. This can result in poor performance and make it challenging to diagnose and address issues. A more scalable and efficient configuration should be explored to optimize resource utilization.

