from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # or your preferred DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<Book {self.book_name} by {self.author}>"

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []
    for b in books:
        output.append({
            'id': b.id,
            'book_name': b.book_name,
            'author': b.author,
            'publisher': b.publisher
        })
    return jsonify(output)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    b = Book.query.get_or_404(id)
    return jsonify({
        'id': b.id,
        'book_name': b.book_name,
        'author': b.author,
        'publisher': b.publisher
    })

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new = Book(
        book_name=data.get('book_name'),
        author=data.get('author'),
        publisher=data.get('publisher')
    )
    db.session.add(new)
    db.session.commit()
    return jsonify({'id': new.id}), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    b = Book.query.get_or_404(id)
    data = request.json
    b.book_name = data.get('book_name', b.book_name)
    b.author = data.get('author', b.author)
    b.publisher = data.get('publisher', b.publisher)
    db.session.commit()
    return jsonify({'message': 'Book updated'})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    b = Book.query.get(id)
    if b is None:
        return jsonify({'error': 'not found'}), 404
    db.session.delete(b)
    db.session.commit()
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
