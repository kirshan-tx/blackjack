from blackjack import * 

def main() -> None:
    """
    Opens a window showing the application 

    :return: None
    """

    app = QApplication([])
    window = Blackjack()
    window.show()
    app.exec()

if __name__== "__main__":
    main()