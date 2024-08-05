from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (replace with your database logic)
profiles = [
    {"cnic": "12345", "name": "John Doe", "age": 30},
    # Add more profiles
]

@app.route('/api/profile/search/<cnic>', methods=['GET'])
def search_profile(cnic):
    # Find the profile with the specified CNIC (replace with your database logic)
    profile = next((p for p in profiles if p['cnic'] == cnic), None)

    if profile:
        return jsonify(profile)
    else:
        return jsonify({"message": "Profile not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
