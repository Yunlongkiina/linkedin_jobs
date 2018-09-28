"""
example how to write scrape simple JS web
"""
import bs4 as bs
import sys
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl


class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self.on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def on_load_finished(self):
        self.html = self.toHtml(self.callable)
        print('Load finished')

    def callable(self, html_str):
        self.html = html_str
        self.app.quit()


def main():
    job_title = []
    post_date = []
    company_name = []
    job_location = []
    job_description = []


    page = Page('https://www.linkedin.com/jobs/search?keywords=&location=Helsinki%2C+Southern+Finland%2C+Finland&locationId=PLACES.fi.1-1')
    print(type(page))
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    job_titile = soup.find_all('h2')
    for job in job_titile:
        print(job.text)

if __name__ == '__main__': main()