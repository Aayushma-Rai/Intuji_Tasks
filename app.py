from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "The server is working!"

blogs = [
    {"id": 1, "title": "My First Blog", "description": "Hello World!", "category": "Tech"},
    {"id": 2, "title": "Cooking Pasta", "description": "How to boil water.", "category": "Food"}
]


@app.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs), 200



@app.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blog = next((b for b in blogs if b['id'] == blog_id), None)
    if blog:
        return jsonify(blog), 200
    return jsonify({"message": "Blog not found"}), 404


@app.route('/blogs', methods=['POST'])
def create_blog():
    data = request.json
    new_blog = {
        "id": len(blogs) + 1,
        "title": data['title'],
        "description": data['description'],
        "category": data['category']
    }
    blogs.append(new_blog)
    return jsonify(new_blog), 201


@app.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    blog = next((b for b in blogs if b['id'] == blog_id), None)
    if not blog:
        return jsonify({"message": "Blog not found"}), 404
    
    data = request.json
    blog.update({
        "title": data.get('title', blog['title']),
        "description": data.get('description', blog['description']),
        "category": data.get('category', blog['category'])
    })
    return jsonify(blog), 200

if __name__ == '__main__':
    app.run(debug=True)