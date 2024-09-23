import chromadb
import uuid
from langchain_community.document_loaders import CSVLoader

class Portfolio:
    def query_skill_link(self, skill_name):
        loader = CSVLoader(file_path="my_portfolio.csv")
        data = loader.load()

        chroma_client = chromadb.PersistentClient("vectorspace")

        try:
            collection = chroma_client.get_collection(name="portfolio")
            print("Retrieved existing collection.")
        except ValueError:  # Handle ValueError instead of CollectionNotFoundError
            collection = chroma_client.create_collection(name="portfolio")
            print("Created a new collection.")

        if collection.count() == 0:
            for doc in data:
                page_content = doc.page_content.split('\n')
                
                techstack = page_content[0]  # Modify this according to your CSV structure
                links = page_content[1]      # Modify this if links are on a different line
                collection.add(
                    documents=[techstack],
                    metadatas={"links": links},
                    ids=[str(uuid.uuid4())]
                )

        print("Documents added to the collection.")

        # Join the list of skills into a single string
        query_text = " ".join(skill_name)

        results = collection.query(
            query_texts=[query_text],  # Pass the joined string instead of a list
            n_results=1  # Fetch the top result
        )
        metadatas = results.get('metadatas', [])

        if metadatas and isinstance(metadatas[0], list) and isinstance(metadatas[0][0], dict):
            return metadatas[0][0].get('links', 'Link not found')
        else:
            return 'Skill not found'
