from flask import Flask, render_template, request
from src.convert_text_to_query import ConvertTextToQuery 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['sentence']
        
        query_obj = ConvertTextToQuery()
        result = query_obj.main(query)

        return render_template('index.html', sentence=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)