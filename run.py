from app import app
import os
from dotenv import load_dotenv

load_dotenv() 

if __name__ == "__main__":
    # app.run(debug=os.getenv('DEBUG', True), host=os.getenv('HOST', '127.0.0.1'), port=os.getenv('PORT', 5000))
    app.run()