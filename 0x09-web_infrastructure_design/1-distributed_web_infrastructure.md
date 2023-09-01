# Distributed Web Infrastructure
![Image ofDistributed Web Infra](https://ibb.co/GVwtjL8)

## Description
This is a distributed web infrastructure that attempts to reduce the traffic to the primary server by distributing some of the load to a replica server with the aid of a server responsible for balancing the load between the two servers (primary and replica).

## Specifics About This Infrastructure
### Distribution Algorithm and Load Balancer
The distribution algorithm the load balancer is configured with and how it works.

The HAProxy load balancer is configured with the Round Robin distribution algorithm. This algorithm works by using each server behind the load balancer in turns, according to their weights. It’s also probably the smoothest and most fair algorithm as the servers’ processing time stays equally distributed. As a dynamic algorithm, Round Robin allows server weights to be adjusted on the go.

### Setup Enabled by the Load-Balancer
The HAProxy load-balancer is enabling an Active-Passive setup rather than an Active-Active setup. In an Active-Active setup, the load balancer distributes workloads across all nodes to prevent any single node from getting overloaded. In an Active-Passive setup, not all nodes are active at all times. The next passive node becomes active only if the preceding node is inactive.

### Database Primary-Replica (Master-Slave) Cluster
How a database Primary-Replica (Master-Slave) cluster works.

A Primary-Replica setup configures one server as the Primary server and the other server as a Replica of the Primary server. The Primary server handles read/write requests, while the Replica server handles read requests. Data synchronization occurs whenever the Primary server executes a write operation.

### Difference Between Primary and Replica Nodes
The difference between the Primary node and the Replica node in regard to the application.

The Primary node handles write operations, while the Replica node processes read operations. This decreases the read traffic to the Primary node.

## Issues With This Infrastructure
### Single Points of Failure (SPOF)
There are multiple SPOF in the infrastructure. For example, if the Primary MySQL database server is down, the entire site would be unable to make changes (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.

### Security Issues
Security issues include the lack of encrypted data transmission over the network using an SSL certificate, making it vulnerable to eavesdropping by hackers. There is also no firewall installed on any server, which means there's no way to block unauthorized IPs.

### Lack of Monitoring
There is no monitoring in place to track the status of each server. Without monitoring, it's challenging to identify and address issues promptly.

