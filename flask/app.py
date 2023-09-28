from pathlib import Path
from flask import Flask, redirect, render_template, request
import streamlit_logic


app = Flask(__name__)
current_url = None
STREAMLIT_BASE_FOLDER = Path('streamlit_apps')

@app.route('/delete/<session_id>', methods=['POST'])
def delete(session_id):
    print(f"Stopping session {session_id}")
    # Add your code here to handle the deletion of the session
    streamlit_logic.stop_streamlit_process(int(session_id))
    return redirect('/')

@app.route('/show/<session_id>', methods=['POST'])
def show(session_id):
    global current_url
    current_url = streamlit_logic.port_to_streamlit_url(int(session_id))
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def home():
    global current_url
    if request.method == 'POST':
        if request.form.get('Spawn app 1') == '1':
            # call start_streamlit_process with file1.py
            current_url = streamlit_logic.start_streamlit_process(STREAMLIT_BASE_FOLDER / 'file1.py')
        elif request.form.get('Spawn app 2') == '2':
            # call start_streamlit_process with file2.py
            current_url = streamlit_logic.start_streamlit_process(STREAMLIT_BASE_FOLDER / 'file2.py')
        else:
            pass # unknown
        return redirect('/')

    return render_template('template.html', url=current_url, session_ids=list(streamlit_logic.sessions.keys()))

if __name__ == '__main__':
    app.run(debug=True)