from dotenv import load_dotenv
from src.runner import Runner

def main():
    load_dotenv()
    Runner().run()

if __name__ == "__main__":
    main()