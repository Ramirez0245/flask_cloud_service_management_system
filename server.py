from app import cloud_management_app


app = cloud_management_app()

if __name__ == "__main__":
    print("Start")
    app.run(debug=True)