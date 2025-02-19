"""Module for handling Neo4j database connections and queries"""

import json
from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DB


class Neo4jConnection:
    """Class for handling Neo4j database connections and queries"""

    def __init__(self, uri, user, password):
        """Initialize Neo4j connection with credentials

        Args:
            uri (str): Neo4j database URI
            user (str): Username for authentication
            password (str): Password for authentication
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        """Close the Neo4j driver connection if it exists"""
        if self.driver is not None:
            self.driver.close()

    # Метод, который передает запрос в БД
    def query(self, query, db=None):
        """Execute a Cypher query against the Neo4j database

        Args:
            query (str): Cypher query to execute
            db (str, optional): Database name to query. Defaults to None.

        Returns:
            list: Results of the query execution
        """
        assert self.driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = (
                self.driver.session(database=db)
                if db is not None
                else self.driver.session()
            )
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response


connection = Neo4jConnection(uri=NEO4J_URI, user=NEO4J_USER, password=NEO4J_PASSWORD)

try:
    print(f"Trying to connect to Neo4j ({NEO4J_URI})")
    connection.driver.verify_connectivity()
    print("Connected to Neo4j")
except:
    print("Cannot connect to Neo4J")


def dict_to_str(d):
    """Convert a dictionary to a Neo4j-compatible string representation

    Args:
        d (dict): Dictionary to convert

    Returns:
        str: Neo4j-compatible string representation of the dictionary
    """
    # Формируем строку, где ключи не будут в кавычках, а значения останутся как есть
    items = [f"{key}: {json.dumps(value)}" for key, value in d.items()]
    return "{%s}" % ", ".join(items)


def create_node(category: str, properties: dict) -> str:
    """Create a new node in the Neo4j database

    Args:
        category (str): Label/category for the node
        properties (dict): Properties to set on the node

    Returns:
        str: Element ID of the created node
    """
    properties = dict_to_str(properties)

    query_string = f"CREATE (a:{category} {properties}) RETURN a"
    response = connection.query(query_string, db=NEO4J_DB)
    return response[0]["a"].element_id


def create_OneDirectionalEdge(
    sourceNode_elementID: str, destNode_elementID: str, RelationType: str
):
    """Create a directed edge between two nodes

    Args:
        sourceNode_elementID (str): Element ID of the source node
        destNode_elementID (str): Element ID of the destination node
        RelationType (str): Type of relationship to create

    Returns:
        str: Element ID of the created relationship

    Warning:
        RelationType cannot contain spaces
    """
    query_string = f"""
    MATCH(a)
    WHERE elementId(a)=	"{sourceNode_elementID}"
    MATCH(b)
    WHERE elementId(b)=	"{destNode_elementID}"
    CREATE (a)-[r:{RelationType}]->(b)
    RETURN r
    """
    response = connection.query(query_string, db=NEO4J_DB)
    return response[0]["r"].element_id


def get_Node(elementId: str):
    """Get a node by its element ID

    Args:
        elementId (str): Element ID of the node to retrieve

    Returns:
        dict: Node data containing properties and labels
    """
    query_string = f"""
    MATCH(a)
    WHERE elementId(a)=	"{elementId}"
    RETURN a
    """
    response = connection.query(query_string, db=NEO4J_DB)
    return response[0]["a"]


def get_path_between_nodes(sourceNode_elementID: str, destNode_elementID: str):
    """Find the shortest path between two nodes

    Args:
        sourceNode_elementID (str): Element ID of the source node
        destNode_elementID (str): Element ID of the destination node

    Returns:
        list: List of nodes on the shortest path from source to destination
    """
    query_string = f"""
    MATCH (source:landmark),(target:landmark)
    WHERE elementId(source) = '{sourceNode_elementID}' AND elementId(target) = '{destNode_elementID}'
    MATCH p = shortestPath((source)-[*]-(target))
    return p;
    """
    response = connection.query(query_string, db=NEO4J_DB)
    return response[0]["p"].nodes


def get_all_nodes():
    """Get all nodes from the database

    Returns:
        list: List of all nodes in the database
    """
    query_string = f"""
    MATCH(N)
    RETURN N
    """
    response = connection.query(query_string, db=NEO4J_DB)
    l = []
    for record in response:
        l.append(record["N"])

    return l


def delete_Node(elementID: str) -> bool:
    """Delete a node by its element ID

    Args:
        elementID (str): Element ID of the node to delete

    Returns:
        bool: False if deletion fails, None if successful
    """
    query_string = f"""
    MATCH (a)
    WHERE elementID(a) = "{elementID}"
    DELETE a
    """
    try:
        response = connection.query(query_string, db=NEO4J_DB)
    except:
        return False


def delete_edge(
    sourceNode_elementID: str, destNode_elementID: str, RelationType: str
): ...


def add_properties_to_node(elementID: str, properties: dict) -> bool:
    """Add or update properties of a node

    Args:
        elementID (str): Element ID of the node to modify
        properties (dict): Properties to add or update

    Returns:
        bool: False if operation fails, None if successful
    """
    for key in properties.keys():

        query_string = f"""

        MATCH (n:landmark)
        WHERE elementID(n) = "{elementID}"
        SET n.{key} = '{properties[key]}'
        RETURN n

        """
        try:
            response = connection.query(query_string, db=NEO4J_DB)
        except:
            return False
