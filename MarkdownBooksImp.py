from MarkdownBooks import *
from BooksDialogImp import *
import toml
import re
import subprocess


CONFIG_FILE = "config.toml"


class MarkdownBooksImp(QMainWindow):

    def __init__(self):
        super(MarkdownBooksImp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionBooks_B.triggered.connect(self.onActionBooksToggled)
        self.config = toml.load(CONFIG_FILE)
        self.updateBooks()

        self.ui.listWidget.itemDoubleClicked.connect(self.onListWidgetItemDoubleClicked)

    def onActionBooksToggled(self):
        print("onActionBooksToggled")
        books_dialog = BooksDialogImp()
        if books_dialog.exec_():
            self.config = books_dialog.config
            print(self.config)
        else:
            print("Canceled")

    def updateBooks(self):
        print("updateBooks")
        books = self.config["books"]
        for key in books:
            self.ui.listWidget.addItem(QListWidgetItem(QIcon(":/res/icon"), key))

    def onListWidgetItemDoubleClicked(self, item):
        print("onListWidgetItemDoubleClicked")
        book_title = item.text()
        book_path = self.config["books"][book_title]
        pattern = re.compile(r'@{\w+}')
        rep_vars = pattern.findall(book_path)
        for rep_var in rep_vars:
            var = rep_var[2:-1]
            if var in self.config["env"]:
                book_path = book_path.replace(rep_var, self.config['env'][var])
            else:
                print('%s not in var_map' % rep_var)
        print(book_path)
        subprocess.run(["typora", book_path])


if __name__ == "__main__":
    app = QApplication()
    main_window = MarkdownBooksImp()
    main_window.show()
    app.exec_()