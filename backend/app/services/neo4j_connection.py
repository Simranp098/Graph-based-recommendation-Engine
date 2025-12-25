from neo4j import GraphDatabase #Imports Neo4j driver.

class Neo4jConnection: #Defines a class to manage DB connections.
    """
    A class to manage the connection and queries to a Neo4j database.
    """
    def __init__(self, uri, user, password):
        # Establish a connection to the database
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        # Connects to Neo4j database.

    def close(self):
        # Close the database connection
        if self._driver is not None:
            self._driver.close()
            #👉 Closes DB connection after request.

    def query(self, query, parameters=None):
        """
        Execute a Cypher query and return the results.
        """
        with self._driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]


def get_neo4j_connection():
    #Creates & supplies new database connection to services.
    """
    Dependency injector for the Neo4j connection.
    It creates a connection instance and ensures it's closed after the request.
    """
    conn = Neo4jConnection(
        uri="bolt://localhost:7687",
        user="neo4j",
        password="@Simran1234"  # Your password
    )
    try:
        yield conn #Sends connection temporarily.
    finally:
        conn.close()