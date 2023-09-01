# Scaled Up Web Infrastructure

![Image of a scaled up web infrastructure](https://ibb.co/ScJfxHF)

## Description
	This web infrastructure is a scaled-up version of the infrastructure described here. In this version, all Single Points of Failure (SPOFs) have been removed, and each major component (web server, application server, and database servers) has been moved to separate GNU/Linux servers. SSL protection isn't terminated at the load balancer, and each server's network is protected with a firewall. Additionally, the infrastructure is monitored for improved reliability and security.

## Specifics About This Infrastructure

### Firewall for Each Server
	The addition of a firewall between each server provides individual protection for each server, safeguarding them from unwanted and unauthorized users. This enhances security by isolating each component.

## Issues With This Infrastructure

### High Maintenance Costs
	The move to separate servers for each major component increases maintenance costs. The need for additional servers results in higher hardware expenses and elevated electricity bills. This requires allocation of company funds for server procurement and ongoing operational expenses, including electricity consumption to keep both new and existing servers operational.

