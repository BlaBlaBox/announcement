from flask import jsonify, request, abort                                                   # pragma: no cover
from announcement_config import app                                                         # pragma: no cover
from announcement_db import add_announcement, get_announcements                             # pragma: no cover
from coverage import Coverage, CoverageException                                            # pragma: no cover


@app.errorhandler(400)
def bad_request(err):
    return jsonify({'error': 'Your request doesn\'t contain JSON'}), 400


@app.errorhandler(401)  # pragma: no cover
def unauthorized(err):
    return jsonify({'error': 'Unauthorized access'}), 403


@app.errorhandler(404)  # pragma: no cover
def not_found(err):
    return jsonify({'error': 'Not found'}), 404


cov = Coverage()        # pragma: no cover
cov.start()             # pragma: no cover


@app.route('/announcement/create', methods=['POST'])
def create_announcement():
    if not request.json:
        abort(400)

    title = request.json['title']
    text = request.json['text']
    image_link = request.json['image_link']
    movie_link = request.json['movie_link']
    new_announcement = add_announcement(title=title, text=text, image_link=image_link, movie_link=movie_link)
    if new_announcement is None:
        return jsonify({'error': 'Announcement could not added.'}), 500     # pragma: no cover

    return jsonify({'result': 'Success', 'announcement_id': new_announcement.announcement_id}), 200


@app.route('/announcement/get', methods=['GET'])
def get():
    announcements = get_announcements()
    if announcements is None:
        return jsonify({'error': 'There is no announcement.'}), 204
    announcement_list = []
    for i in announcements:
        announcement_list.append({"announcement_id": i.announcement_id, "title": i.title, "text": i.text, "image_link": i.image_link, "movie_link": i.movie_link})
    return jsonify({'result': 'Success', 'announcement_list': announcement_list}), 200


@app.route('/endtest')          # pragma: no cover
def end_test():
    cov.stop()
    cov.save()
    try:
        cov.html_report()
        return jsonify({'result': 'Coverage report has been saved'}), 200
    except CoverageException as err:
        print("Error ", err)
        return jsonify({'result': 'Error on coverage'}), 400


if __name__ == '__main__':      # pragma: no cover
    app.run(debug=True, port=8000)
