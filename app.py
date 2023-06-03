from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('/scrape')
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    base_url = request.form.get('url')
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for link in soup.find_all('a'):
        try:
            link_text = link.get_text()
            link_url = link.get('href')
            
            absolute_url = urljoin(base_url, link_url)
            
            link_data = {
                'text': link_text,
                'url': absolute_url
            }
            
            links.append(link_data)
        except AttributeError:
            continue


    return render_template('results.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)







# from flask import Flask, render_template, request
# from bs4 import BeautifulSoup
# import requests
# from urllib.parse import urljoin

# app = Flask(__name__)

# @app.route('/scrape', methods=['POST'])
# def scrape():
#     base_url = request.form.get('url')
#     response = requests.get(base_url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     links = []
#     for link in soup.find_all('a'):
#         try:
#             link_text = link.get_text()
#             link_url = link.get('href')
            
#             absolute_url = urljoin(base_url, link_url)
            
#             link_data = {
#                 'text': link_text,
#                 'url': absolute_url
#             }
            
#             links.append(link_data)
#         except AttributeError:
#             continue

#     return render_template('results.html', links=links)

# if __name__ == '__main__':
#     app.run(debug=True)
