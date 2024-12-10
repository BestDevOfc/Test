from Flask import*


app = Flask("app")

@app.route('/')
def home():
    return "HI"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
