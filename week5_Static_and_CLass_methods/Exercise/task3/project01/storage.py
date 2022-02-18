class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = Storage.find_item(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = Storage.find_item(topic_id, self.topics)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = Storage.find_item(document_id, self.documents)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = Storage.find_item(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = Storage.find_item(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = Storage.find_item(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        return Storage.find_item(document_id, self.documents)

    @staticmethod
    def find_item(given_id, given_list):
        return [item for item in given_list if item.id == given_id][0]

    def __repr__(self):
        result = []
        for doc in self.documents:
            result.append(repr(doc))

        return '\n'.join(result)