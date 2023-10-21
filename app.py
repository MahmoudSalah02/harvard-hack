from albumy import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # This runs the Flask development server when the script is run directly
