from website import create_app

app =  create_app()

#if main is run, the line will be executed
if __name__ == '__main__':
    #run flask application and start up web server
    app.run(debug=True)

