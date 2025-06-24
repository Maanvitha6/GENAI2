                              June 03 2025
                            
1. Network :
   A collection of things (called nodes) connected by links (called edges).

2. Social network :
   A network where people are the nodes and relationships (like friendship or follows) are the edges.

3. Graph Theory :
   A branch of math that studies networks made of nodes and edges.

4. Node : (vertex)
   A point in the network.

5. Edge : (Link)
   A connection between two nodes.

   * TYPES OF EDGES :
    1. Directed Edge :
       . A one-way connection.

    2. Undirected Edge :
       . A two-way connection.

6. Centrality :
   . A measure of how important or central a node is in a network.
   . There are different types : degree, betweenness, closeness, etc.

7. Degree : 
   . The number of edges (connections) a node has.
   . There are two types of degrees : In-Degree , Out-Degree.

   * In-Degree:
     . Number of edges coming into a node (only for directed).
    
   * Out- Degree:
     . Number of edges going out of a node.
    
8. Shortest path :
   . The smallest number of steps needed to go from one node to another.

9. Betweeness :
   . How often a node lies on the shortest path between other nodes.

10. Closeness :
   . How near a node is to all other nodes.

11. Eigen vector centrality :
    . A node is important if it is connected to other important nodes. Not just how many connections you have, but who you are  connected to.

12. Connected graph : 
    . A graph where all nodes are connected by paths.

13. Component :
    . A group of connected nodes.

14. Path :
    . A route from one node to other through edges.

15. Cycle :
    . A path that starts and ends at the same node.

Example :
. here are 5 people:
  ->Aisha, Ben, Chloe, Dev, Ella.
  ->And these are the follows (just like Instagram “follows”):
  ->Aisha follows Ben.
  ->Ben follows Chloe.
  ->Chloe follows Dev.
  ->Dev follows Ella.
  ->Aisha also follows Ella directly.

    -> Node          - 	        Each person (Aisha, Ben, etc.) is a node.
    -> Edge	         -          A follow is a connection — an arrow from one person to another.
    -> In-Degree     -	        How many people follow you. Ella has 2 followers (Dev and Aisha).
    -> ShortestPath  -          Aisha → Ella directly (1 step) is shorter than going through all others.
    -> Betweenness   -  	    Chloe is in the middle between Ben and Dev → important bridge.
    -> Closeness     - 	        Ben can reach everyone quickly in few steps → he is close to all.
    -> EigenvectorCentrality - 	Ella is followed by important people (Dev, Aisha) → she’s influential.
    
* Graph Database:
  A graph database is a non-relational database designed to store data in nodes (entities) and edges (relationships) — like a network.

Types of Data:

1. Structured Data:
    . organized in rows and columns like in tables.	
    . Relational databases (e.g., SQL).

2. Semi-structured: 
    . Doesn’t fit strict tables, but has tags or markers.	
    . JSON, XML, CSV.

3. Unstructured:
    . No predefined format.	
    . Text files, emails, images, videos.

Graph Database:(Fraud Detection)

*  It works well with:
Data Type	- How Graph Databases Handle it.
Structured	- Can import data from SQL databases into graphs.
Semi-structured -	Naturally maps to nodes and edges (e.g., JSON → nodes/links).
Unstructured	 - Can store metadata or tags as graph properties.