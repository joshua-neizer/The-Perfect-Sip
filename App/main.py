from website import create_app

app =  create_app()

# Executes when main is ran
if __name__ == '__main__':
    # Run flask application and start up web server
    app.run(debug=True, host="0.0.0.0")

