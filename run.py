# ------- local imports -------
from app.app import app

if __name__ == '__main__':
    # This is a change
    app.run(host='0.0.0.0', port=5555)
