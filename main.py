from blackjack import * 

def main():
    app = QApplication([])
    window = Blackjack()
    window.show()
    app.exec()

if __name__== "__main__":
    main()