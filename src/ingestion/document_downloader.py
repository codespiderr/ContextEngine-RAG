import os
import wikipediaapi
import time
from bs4 import BeautifulSoup as soup

def download_data(topics_list,dir="data/cleaned"):
    os.makedirs(dir, exist_ok=True)
    print("started dowload of ",len(topics_list), "pages")

    wiki = wikipediaapi.Wikipedia(user_agent='CONTEXTENGINE-RAG', language='en',extract_format=wikipediaapi.ExtractFormat.HTML)

    for page_title in topics_list:
        time.sleep(1.0)
        
        page = wiki.page(page_title)
        if not page.exists():
            print(f"Doesn't exist: {page_title}")
            continue
            
        safe_filename = page_title.replace(" ", "_").replace("/", "-") + ".txt"
        file_path = os.path.join(dir, safe_filename)

        t = soup(page.text,'html.parser')
        #clean_text = t.get_text(separator=" ", strip=True)

        truncated_content = page.text
        if "see also" in page.text or "See also" in page.text:
        # Keeps only the text strictly before the phrase
            truncated_content = page.text.split("See also", 1)[0]
        # Keeps only the text strictly before the phrase
            truncated_content = truncated_content.split("Further reading", 1)[0]


        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Title: {page.title}\n")
            f.write(f"Category_Context: RAG Dataset\n\n")
            f.write(t.get_text())
            
        print(f"Saved: {page_title}")

if __name__ == "__main__":

    data = [
    "Alan Turing", "Ada Lovelace", "Charles Babbage", "Analytical Engine",
    "Von Neumann architecture", "John von Neumann", "ENIAC", "Claude Shannon",
    "Information theory", "Difference engine", "Gottfried Wilhelm Leibniz",
    "George Boole", "Boolean algebra", "Turing machine", "Entscheidungsproblem",
    "Colossus computer", "Harvard Mark I", "Grace Hopper", "Compiler",
    "Von Neumann cellular automaton",

    "History of programming languages", "Fortran", "Lisp (programming language)",
    "John Backus", "ALGOL 60", "COBOL", "BASIC", "C (programming language)",
    "Dennis Ritchie", "C++", "Bjarne Stroustrup", "Object-oriented programming",
    "Functional programming", "Procedural programming", "Python (programming language)",
    "Guido van Rossum", "Java (programming language)", "JavaScript", "SQL", "Assembly language",

    "Operating system", "Unix", "Ken Thompson", "Linux", "Linus Torvalds", "GNU",
    "Richard Stallman", "Microsoft Windows", "History of the Internet", "ARPANET",
    "Internet protocol suite", "Transmission Control Protocol", "IP address",
    "World Wide Web", "Tim Berners-Lee", "Hypertext Transfer Protocol", "Domain Name System",
    "Ethernet", "Cloud computing", "Central processing unit",

    "History of artificial intelligence", "Dartmouth workshop", "John McCarthy (computer scientist)",
    "Marvin Minsky", "AI winter", "Expert system", "Symbolic artificial intelligence",
    "Machine learning", "Arthur Samuel (computer scientist)", "Perceptron", "Frank Rosenblatt",
    "Artificial neural network", "Backpropagation", "Geoffrey Hinton", "Yann LeCun",
    "Support vector machine", "Random forest", "Decision tree learning", "Deep learning",
    "Convolutional neural network",

    "Transformer (deep learning architecture)", "Attention (machine learning)",
    "Large language model", "Generative pre-trained transformer", "OpenAI",
    "Ilya Sutskever", "Sam Altman", "BERT (language model)", "Prompt engineering",
    "Retrieval-augmented generation", "Reinforcement learning from human feedback",
    "Recurrent neural network", "Long short-term memory", "Natural language processing",
    "Artificial general intelligence", "Computing power", "Graphics processing unit",
    "Nvidia", "AI safety", "Hallucination (artificial intelligence)"
    ]
    
    download_data(data)