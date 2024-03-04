class UserFile(Document):
    filename = StringField()
    file_data = BinaryField()