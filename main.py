from portfolio_In_chromadb import Portfolio
from clean_data import Clean_data
from Email_generator import Chain

class Main_generator():
    @staticmethod
    def main_gen(url):  # Removed the dot after @staticmethod
        # Define the URL for cleaning
        url_to_clean = url
        print(url_to_clean)
        # Clean the data from the URL
        cleaned_text = Clean_data.cleaned(url_to_clean)
        print(f"Cleaned text from URL: {cleaned_text}")

        # Create an instance of Chain
        chain = Chain()

        # Extract jobs using the instance
        jobs = chain.extract_jobs(cleaned_text)
        print(jobs)
        
        # Initialize skills
        skills = []
        
        for job in jobs:
            # Extract skills from the job, if available
            skills = job.get('skills', [])
            print(skills)
            if skills:
                break  # Break the loop if we find skills in any job

        # Check if skills were found
        if not skills:
            raise ValueError("No skills found in the extracted jobs.")

        # Query skill links from the portfolio
        portfolio = Portfolio()
        link = portfolio.query_skill_link(skills)

        # Generate the email using the instance
        email_content = chain.write_mail(job, link)
        return email_content
