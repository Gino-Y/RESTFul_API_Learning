from flask import Flask
from app.app import create_app

app = create_app()


@app.route('/v1/user/get')
def get_user():
    return 'I am Gino!'


if __name__ == '__main__':
    app.run()
