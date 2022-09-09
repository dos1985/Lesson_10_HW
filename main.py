from flask import Flask, request, render_template
import utils
import visualizer

app = Flask(__name__)


@app.route("/")
def page_all_candidates():
    candidates = utils.candidates_get_all()
    html_code = visualizer.build_html_for_some_candidates(candidates)
    return html_code


@app.route("/skills/")
def page_candidates_by_skill(skill):
    candidates = utils.candidates_get_by_skill(skill)
    html_code = visualizer.build_html_for_some_candidates(candidates)
    return html_code


@app.route("/candidates/<int:pk>")
def page_candidate_by_pk(pk):
    candidate = utils.candidates_get_by_pk(pk)
    html_code = visualizer.build_html_for_one_candidate(candidate)
    return html_code


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7000, debug=True)
