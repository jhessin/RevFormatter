"""
This returns a simple formatter that when asked for a chapter of the bible
generates the appropriate html to render to a web page.
"""
import mariadb
import sys

DEBUG = False

class Formatter:
    def __init__(self) -> None:
        try:
            self.__conn = mariadb.connect()
            self.__cur = self.__conn.cursor()
        except mariadb.Error as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)

    def getChapter(self, book: str, chapter: int) -> str:
        """
        A basic fetcher for a bible chapter. Give it a book name or
        abbreviation and it will find it and return that chapter text
        formatted.

        >>> from Formatter import Formatter

        >>> f = Formatter()

        >>> f.getChapter('ex', 1)
        """
        self.cursor.execute(f"""SELECT book from REV.book WHERE aliases like
                            "%{book}%" """)
        bookNum = None
        for book in self.cursor:
            bookNum = book[0]
        if not bookNum:
            return 'Book not found!'
        if DEBUG:
            print(f'Book: {book}, chapter: {chapter}')
        self.cursor.execute(f"""SELECT heading, microheading, paragraph, style,
                            versetext FROM REV.verse WHERE book="{bookNum}" AND
                            chapter="{chapter}" """)
        result = ''
        for heading, microheading, paragraph, style, text in self.cursor:
            # Just dump the text for testing purposes.
            result += f"{text}\n"
        return result

    @property
    def cursor(self):
        return self.__cur

def main():
    f = Formatter()
    result = f.getChapter('ex', 1)
    print(result)


if __name__ == "__main__":
    main()
