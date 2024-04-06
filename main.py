from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get-user/<int:user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Carlos",
        "email": "carlos@exemple.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


@app.route("/update-user", methods=["PUT"])
def update_user():
    data = request.get_json()

    return jsonify(data), 202


@app.route("/delete-user", methods=["DELETE"])
def delete_user():
    data = request.get_json()

    return jsonify(data), 203


if __name__ == "__main__":
    app.run(debug=True)
