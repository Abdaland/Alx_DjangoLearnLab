\# delete.md



from bookshelf.models import Book



\# Command:

book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()

Book.objects.all()



\# Expected output:

\# <QuerySet \[]>

