import requests

# Usage pytest announcement_test.py


class AnnouncementAction():
    # base_url = 'https://blablabox-announcement.herokuapp.com'

    # For local testing
    base_url = 'http://127.0.0.1:8000'

    def create_announcement(self, announcement_info, required_status):
        r = requests.post(url=self.base_url + '/announcement/create', json=announcement_info)
        assert r.status_code == required_status

    def get_announcement(self, required_status):
        r = requests.get(url=self.base_url + '/announcement/get')
        assert r.status_code == required_status

    def send_end_test(self, status):
        resp = requests.get(self.base_url + "/endtest")
        assert resp.status_code == status


def test_announcement_actions():

    aAction = AnnouncementAction()

    announcement_info = {
        'title': 'test',
        'text': 'test',
        'image_link': 'google.com',
        'movie_link': 'youtube.com'
    }

    # Try to get announcement while there is no announcement
    aAction.get_announcement(204)

    # Create announcement
    aAction.create_announcement(announcement_info, 200)

    # Get all announcements
    aAction.get_announcement(200)

    # Try to send request with data that is not JSON
    aAction.create_announcement(None, 400)

    # Send incomplete JSON
    announcement_info_temp = {
        'title': 'test',
        'image_link': 'google.com'
    }
    aAction.create_announcement(announcement_info_temp, 500)

    # Send a request to complete coverage report
    aAction.send_end_test(200)
