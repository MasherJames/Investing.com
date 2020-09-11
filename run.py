from app import create_app

# Initialize the flask app
app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
