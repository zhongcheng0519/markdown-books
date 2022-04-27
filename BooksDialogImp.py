from BooksDialog import *
import toml


CONFIG_FILE = "config.toml"


class BooksDialogImp(QDialog):

    def __init__(self):
        super(BooksDialogImp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.config = dict()
        self.ui.tableWidgetEnvironments.setColumnWidth(0, 150)
        self.ui.tableWidgetEnvironments.setColumnWidth(1, 500)
        self.ui.tableWidgetBooks.setColumnWidth(0, 150)
        self.ui.tableWidgetBooks.setColumnWidth(1, 500)
        self.ui.pushButtonAddEnv.clicked.connect(self.onPushButtonAddEnvClicked)
        self.ui.pushButtonDelEnv.clicked.connect(self.onPushButtonDelEnvClicked)
        self.ui.pushButtonAddBook.clicked.connect(self.onPushButtonAddBookClicked)
        self.ui.pushButtonDelBook.clicked.connect(self.onPushButtonDelBookClicked)
        self.ui.buttonBox.accepted.connect(self.onButtonBoxAccepted)

        self.load(CONFIG_FILE)
        self.updateTable()

    def load(self, path):
        try:
            conf = toml.load(path)
        except Exception:
            QMessageBox.warning(self, 'Warning', 'Load failed, create new config file')
            return
        self.config = conf

    def updateTable(self):
        if not self.config:
            return
        env = self.config["env"]
        books = self.config["books"]
        self.ui.tableWidgetEnvironments.setRowCount(0)
        r = 0
        for k, v in env.items():
            self.ui.tableWidgetEnvironments.insertRow(r)
            self.ui.tableWidgetEnvironments.setItem(r, 0, QTableWidgetItem(k))
            self.ui.tableWidgetEnvironments.setItem(r, 1, QTableWidgetItem(v))
            r += 1
        self.ui.tableWidgetBooks.setRowCount(0)
        r = 0
        for k, v in books.items():
            self.ui.tableWidgetBooks.insertRow(r)
            self.ui.tableWidgetBooks.setItem(r, 0, QTableWidgetItem(k))
            self.ui.tableWidgetBooks.setItem(r, 1, QTableWidgetItem(v))
            r += 1

    def onPushButtonAddEnvClicked(self):
        print("onPushButtonAddEnvClicked")
        rc = self.ui.tableWidgetEnvironments.rowCount()
        self.ui.tableWidgetEnvironments.insertRow(rc)

    def onPushButtonDelEnvClicked(self):
        print("onPushButtonDelEnvClicked")
        r = self.ui.tableWidgetEnvironments.currentRow()
        self.ui.tableWidgetEnvironments.removeRow(r)

    def onPushButtonAddBookClicked(self):
        print("onPushButtonAddBookClicked")
        rc = self.ui.tableWidgetBooks.rowCount()
        self.ui.tableWidgetBooks.insertRow(rc)

    def onPushButtonDelBookClicked(self):
        print("onPushButtonDelBookClicked")
        r = self.ui.tableWidgetBooks.currentRow()
        self.ui.tableWidgetBooks.removeRow(r)

    def readTable(self):
        for r in range(self.ui.tableWidgetEnvironments.rowCount()):
            k = self.ui.tableWidgetEnvironments.item(r, 0).text()
            v = self.ui.tableWidgetEnvironments.item(r, 1).text()
            if "env" not in self.config:
                self.config["env"] = dict()
            self.config['env'][k] = v
        for r in range(self.ui.tableWidgetBooks.rowCount()):
            k = self.ui.tableWidgetBooks.item(r, 0).text()
            v = self.ui.tableWidgetBooks.item(r, 1).text()
            if "books" not in self.config:
                self.config["books"] = dict()
            self.config["books"][k] = v

    def onButtonBoxAccepted(self):
        print("onButtonBoxAccepted")
        self.readTable()
        with open(CONFIG_FILE, "wt", encoding='utf-8') as f:
            toml.dump(self.config, f)
