# ------- local imports -------
from app.app import app

if __name__ == '__main__':
    # hey this is a new change
    app.run(host='0.0.0.0', port=5555)
