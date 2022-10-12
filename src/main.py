from microdot import Microdot, send_file

app = Microdot()

htmldoc = """<!DOCTYPE html>
<html>
    <head>
        <title>Microdot Example Page</title>
    </head>
    <body>
        <div>
            <h1>Microdot Example Page</h1>
            <p>Hello from Microdot!</p>
            <p><a href="/shutdown">Click to shutdown the server</a></p>
        </div>
    </body>
</html>
"""


@app.route("/dummy-16.file")
def index1(request):
    return send_file("dummy-16.file")


@app.route("/dummy-32.file")
def index2(request):
    return send_file("dummy-32.file")


@app.route("/dummy-128.file")
def index3(request):
    return send_file("dummy-128.file")


@app.route("/dummy.bin")
def index4(request):
    return send_file("dummy.bin")


@app.route("/")
def hello(request):
    return htmldoc, 200, {"Content-Type": "text/html"}


@app.route("/shutdown")
def shutdown(request):
    request.app.shutdown()
    return "The server is shutting down..."


app.run(debug=True, port=80)
