from flask import Flask, render_template, request, url_for

from HandleDetailedFile import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    config_file_path = './configs.json'
    if request.method == 'POST':
        print(f'previous_question: {read_json(config_file_path)["previous_question"]}')
        print(f'choice: {request.form.get("choice")}')
    df = DetailFile('./memorable_word/ielts3500.txt')
    random_element = df.get_random_element(3)
    question = random.sample(random_element, 1)[0]
    j = {"previous_question": question['en']}
    write_json(config_file_path, j)
    req = request.form
    return render_template('main.html', question=question, choice_element=random_element, req=req)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
