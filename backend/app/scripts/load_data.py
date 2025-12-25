import csv
import os
from neo4j import GraphDatabase
#Load CSV files & handle Neo4j connection.

# --- Database Connection Details ---
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "@Simran1234" # Your Neo4j password

class DataLoader: #Handles loading operations.
    def __init__(self, driver):
        self.driver = driver

    def clean_database(self): #Removes old data to start fresh.
        """Wipes all nodes, relationships, and constraints from the database."""
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            # Drop constraints to ensure a completely fresh start
            try:
                session.run("DROP CONSTRAINT FOR (u:User) REQUIRE u.customerID IS UNIQUE")
            except Exception: pass # Ignore error if constraint doesn't exist
            try:
                session.run("DROP CONSTRAINT FOR (p:Product) REQUIRE p.id IS UNIQUE")
            except Exception: pass
        print("🧹 Database has been wiped clean.")

    def load_users(self, file_path):
        with self.driver.session() as session:
            session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.customerID IS UNIQUE")
            # Use 'utf-8-sig' to handle potential invisible characters at the start of the file
            with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row.get('id'): # Skips empty lines
                        session.run("""
                            MERGE (u:User {customerID: toInteger($id)})
                            SET u.name = $name
                        """, id=row['id'], name=row['name'])
            print(f"✅ Successfully loaded users from {os.path.basename(file_path)}")

    def load_products(self, file_path):
        with self.driver.session() as session:
            session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (p:Product) REQUIRE p.id IS UNIQUE")
            with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row.get('id'): # Skips empty lines
                        session.run("""
                            MERGE (p:Product {id: $id})
                            SET p.name = $name, p.category = $category
                        """, id=row['id'], name=row['name'], category=row['category'])
            print(f"✅ Successfully loaded products from {os.path.basename(file_path)}")

    def create_purchase_relationships(self, file_path):
        with self.driver.session() as session:
            with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # FINAL FIX: Uses the correct 'user' and 'product' keys from your CSV
                    if row.get('user') and row.get('product'):
                        session.run("""
                            MATCH (u:User {customerID: toInteger($user)}) #Creates User nodes.
                            MATCH (p:Product {id: $product}) #Creates Product nodes.
                            MERGE (u)-[:PURCHASED]->(p) #Creates edges between users and products.
                        """, user=row['user'], product=row['product'])
            print(f"✅ Successfully created PURCHASED relationships from {os.path.basename(file_path)}")


if __name__ == "__main__":
    dataset_path = 'Dataset'

    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    loader = DataLoader(driver)

    print("--- Starting final data loading process ---")
    loader.clean_database()
    loader.load_users(os.path.join(dataset_path, 'users.csv'))
    loader.load_products(os.path.join(dataset_path, 'products.csv'))
    loader.create_purchase_relationships(os.path.join(dataset_path, 'purchased.csv'))
    #Loads ALL data and builds graph.
    
    driver.close()
    print("\n--- Data loading complete! Your project is ready. ---")