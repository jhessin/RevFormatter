"""
This returns a simple formatter that when asked for a chapter of the bible
generates the appropriate html to render to a web page.
"""
import mariadb
import sys

DEBUG = True

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
nd Judah,\nIssachar, Zebulun, and Benjamin,\nDan and Naphtali, Gad and Asher.\nAll the souls who came out of Jacob&rsquo;s thigh were 70 souls; and Joseph was in Egypt already.\nJoseph died, as did all his brothers and all that generation.\nThe children of Israel were fruitful and increased abundantly; and multiplied and grew exceedingly strong, and the land was filled with them.\nNow there arose a new king over Egypt who did not know Joseph.\nAnd he said to his people, &ldquo;Behold, the people of the children of Israel are more numerous and stronger than we are.\nCome, let&rsquo;s deal wisely with them, lest they multiply and it happens that when any war breaks out that they join with our enemies and fight against us and escape from the land.&rdquo;\nTherefore they set taskmasters over them to afflict them with forced labor. They built for Pharaoh storage cities, Pithom and Raamses.\nBut the more they afflicted them, the more they multiplied and the more they spread out. The <em>Egyptians</em> were grieved because of the children of Israel.\nThe Egyptians ruthlessly made the children of Israel serve,\nand they made their lives bitter with hard service in mortar and in brick and in all kinds of service in the field. In all of their service they ruthlessly made them serve as slaves.\nThe king of Egypt spoke to the Hebrew midwives, of whom the name of the one was Shiphrah and the name of the other Puah,\nand he said, &ldquo;When you perform the duty of a midwife to the Hebrew women andsee them on the birth stool, if it is a son, then you must kill him, but if it is a daughter, then she may live.&rdquo;\nBut the midwives feared God and did not do what the king of Egypt commanded them, but saved the baby boys alive.\nThe king of Egypt called for the midwives and said to them, &ldquo;Why have you done this, and let the male children live?&rdquo;\nThe midwives said to Pharaoh, &ldquo;Because the Hebrew women are not like the Egyptian women, for they are vigorous and give birth before the midwife comes to them.&rdquo;\nSo God dealt well with the midwives. And the people multiplied and grew very mighty.\nAnd because the midwives feared God, he gave them families.\nThen Pharaoh commanded all his people, saying, &ldquo;You must castevery son who is born into the river, but you are to let every daughter live.&rdquo;\n-\n-\n-\n'
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
