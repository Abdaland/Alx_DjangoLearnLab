from relationship_app.models import Author, Book, Library, Librarian

def run():
    # Create an Author
    author = Author.objects.create(name="Abdallah El Yamlahi")

    # Create a Book linked to that Author
    book = Book.objects.create(title="My First Book", author=author)

    # Create a Library and add the Book to it
    library = Library.objects.create(name="Central Library")
    library.books.add(book)

    # Create a Librarian linked to the Library
    librarian = Librarian.objects.create(name="Sara", library=library)

    # Print everything
    print("Author:", author.name)
    print("Book:", book.title, "| Author:", book.author.name)
    print("Library:", library.name, "| Books:", [b.title for b in library.books.all()])
    print("Librarian:", librarian.name, "| Library:", librarian.library.name)

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # ✅ required
    return library.books.all()

def list_books_by_author(author_name):
    author = Author.objects.get(name=author_name)      # ✅ exact line
    return Book.objects.filter(author=author)          # ✅ exact line

def get_librarian(library_name):
    library = Library.objects.get(name=library_name)  # ✅ exact line
    return library.librarian
