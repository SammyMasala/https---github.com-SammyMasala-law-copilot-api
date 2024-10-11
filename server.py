from app import app
import dotenv

dotenv.load_dotenv()

if __name__ == "__main__":
    app.run(host="localhost", port=30000, debug=True)