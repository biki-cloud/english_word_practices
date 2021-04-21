from flask import Flask, render_template, request
import glob

from HandleDetailedFile import *

app = Flask(__name__)


@app.route('/<word_name>', methods=['GET', 'POST'])
def main(word_name):
    config_file_path = './configs.json'
    # df = DetailFile('./memorable_word/ielts3500.txt')
    df = DetailFile(f'./memorable_word/{word_name}')
    if request.method == 'POST':
        result = read_json(config_file_path)["result"]
        user_choice = request.form.get('choice')
        print(f'previous_question: {result}')
        print(f'user_choice: {user_choice}')
        if result == user_choice:
            df.add_collect_number(user_choice)

    random_element = df.get_random_element(3)
    question = random.sample(random_element, 1)[0]
    data = {"result": question['en']}
    write_json(config_file_path, data)
    req = request.form
    return render_template('main.html', question=question, choice_element=random_element, req=req, word_file=word_name)


@app.route('/rest')
def rest():
    word_files = glob.glob('./memorable_word/*')
    word_files_basename = [os.path.basename(f) for f in word_files]
    return render_template('rest.html', word_files=word_files_basename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
