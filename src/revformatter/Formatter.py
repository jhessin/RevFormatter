"""
This returns a simple formatter that when asked for a chapter of the bible
generates the appropriate html to render to a web page.
"""
import mariadb
import sys

class Formatter:
    def __init__(self) -> None:
        try:
            self.__conn = mariadb.connect()
            self.__cur = self.__conn.cursor()
        except mariadb.Error as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)

    def getChapter(self, book: str, chapter: int) -> str:
        self.cursor.execute(f"""SELECT book from REV.book WHERE title like "{book}" """)
        bookNum = 1
        for book in self.cursor:
            bookNum = book[0]
        print(f'Book Number: {(bookNum)}, chapter: {chapter}')
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
