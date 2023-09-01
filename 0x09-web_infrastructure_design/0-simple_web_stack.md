# Simple Web Stack

![Image of a simple web stack](https://ibb.co/vqkQRKx)

## Description
	This is a simple web infrastructure that hosts a website reachable via www.foobar.com. The infrastructure lacks firewalls and SSL certificates for network protection. Each component (database, application server) shares the resources (CPU, RAM, and SSD) provided by the server.

## Specifics About This Infrastructure

### What a Server Is
	A server is computer hardware or software that provides services to other computers, usually referred to as clients.

### The Role of the Domain Name
	A domain name provides a human-friendly alias for an IP Address, making it easier to recognize and remember. The IP address and domain name alias are mapped in the Domain Name System (DNS).

### DNS Record for www.foobar.com
	www.foobar.com uses an A record, which can be checked by running `dig www.foobar.com`. An A record stores a hostname and its corresponding IPv4 address.

### The Role of the Web Server
	The web server is software/hardware that accepts requests via HTTP or secure HTTP (HTTPS) and responds with the content of the requested resource or an error message.

### The Role of the Application Server
	The application server installs, operates, and hosts applications and associated services for end users, IT services, and organizations. It facilitates the hosting and delivery of high-end consumer or business applications.

### The Role of the Database
	The database maintains a collection of organized information that can be easily accessed, managed, and updated.

### Communication with the Client
	Communication between the client (user's computer) and the server occurs over the internet network through the TCP/IP protocol suite.

## Issues With This Infrastructure

### Single Points of Failure (SPOF)
	There are multiple SPOFs in this infrastructure. For example, if the MySQL database server is down, the entire site would be inaccessible.

### Downtime During Maintenance
	When maintenance checks are required on any component, they must be taken offline, or the server needs to be turned off. Since there is only one server, the website experiences downtime during maintenance.

### Scalability Challenges
	Scaling this infrastructure can be difficult because all required components are on a single server. As a result, the server can quickly run out of resources or slow down when faced with a high volume of incoming requests.

