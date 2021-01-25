from pymongo import MongoClient

client = MongoClient("mongodb://localhost:2717/")
# o banco de dados catalogue será criado se não existir
db = client.catalogue
# a coleção books será criada se não existir
students = db.books.find({})
book = {
    "title": "A Light in the Attic, newest! :)",
}
db.books.insert_one(book)
client.close()  # fecha a conexão com o banco de dados
