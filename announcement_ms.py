from flask import jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from announcement_config import app
from announcement_db import add_announcement, get_announcements


auth = HTTPBasicAuth()

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Your request doesn\'t contain JSON'}), 400

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 403

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404




@app.route('/announcement/create', methods=['POST'])
#@auth.login_required
def create_announcement():
    if not request.json:
        abort(400)

    title = request.json['title']
    text = request.json['text']
    image_link = request.json['image_link']
    movie_link = request.json['movie_link']
    new_announcement = add_announcement(title=title, text=text, image_link=image_link, movie_link=movie_link)
    if new_announcement is None:
        return jsonify({'error': 'Announcement could not added.'}), 400

    return jsonify({'result': 'Success', 'announcement_id':new_announcement.announcement_id}), 200

@app.route('/announcement/get', methods=['GET'])
#@auth.login_required
def get():
    announcements = get_announcements()
    if announcements is None:
        return jsonify({'error': 'There is no announcement.'}), 400
    announcement_list = []
    for i in announcements:
        announcement_list.append({"announcement_id":i.announcement_id, "title":i.title, "text":i.text, "image_link":i.image_link, "movie_link":i.movie_link})
    return jsonify({'result': 'Success', 'announcement_list':announcement_list}), 200



# Validate the admin signin#######TODO###############
@auth.verify_password
def verify_password(username, password):
    # TODO: Change check if is admin in the database or not.
    return username == 'admin' and password == 'asdqwe123'


if __name__ == '__main__':
    app.run(debug=True, port=8000)
