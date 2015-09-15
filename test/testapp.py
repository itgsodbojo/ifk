
import sys
import seed


sys.path.append("../")

from app import app

if __name__ == '__main__':
    app.run(debug=True)