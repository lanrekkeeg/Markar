from app.controller.server import api

if __name__ == "__main__":
    api.run(host='0.0.0.0', port=8082)