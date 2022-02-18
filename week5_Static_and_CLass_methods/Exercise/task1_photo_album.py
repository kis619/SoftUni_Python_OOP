import math

from week5_Static_and_CLass_methods.Exercise.constants import photos_per_page


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] * photos_per_page for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / photos_per_page))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if not self.photos[page] or len(self.photos[page]) < photos_per_page:
                for slot in range(photos_per_page):
                    self.photos[page].append(label)
                    return f"{label} photo added successfully on page {page + 1} " \
                           f"slot {slot + 1}"

        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in range(self.pages):
            if len(self.photos[page]):
                for photo in self.photos[page]:
                    result += "[] "
                result = result[:-1]
            result += "\n-----------\n"

        return result[:-1]


album = PhotoAlbum(2)
print(len(album.photos))
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
