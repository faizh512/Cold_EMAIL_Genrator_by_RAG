from langchain_community.document_loaders import WebBaseLoader

import re
class Clean_data():
    def clean_text(text):
        # Remove HTML tags
        text = re.sub(r'<[^>]*?>', '', text)
        # Remove URLs
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
        # Remove special characters
        text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
        # Replace multiple spaces with a single space
        text = re.sub(r'\s{2,}', ' ', text)
        # Trim leading and trailing whitespace
        text = text.strip()
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text


    def cleaned(url):
        url=url
        loader=WebBaseLoader([url])
        data=loader.load()
        for doc in data:
            # Assuming each document's content is in `doc.page_content`
            cleaned_content =Clean_data.clean_text(doc.page_content)
            return cleaned_content