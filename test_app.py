import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    # Test for the dashboard page
    def test_dashboard(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    # Test for submitting data
    def test_submit(self):
        tester = app.test_client(self)
        response = tester.post('/submit', data=dict(email="test@example.com", summary="Test summary"))
        self.assertEqual(response.status_code, 200)

    # Test for getting all summaries
    def test_get_summaries(self):
        tester = app.test_client(self)
        response = tester.get('/summaries')
        self.assertEqual(response.status_code, 200)

    # Test for updating a summary
    def test_update_summary(self):
        tester = app.test_client(self)
        response = tester.patch('/summaries/1', json=dict(summary="Updated summary"))
        self.assertEqual(response.status_code, 200)

    # Test for deleting a summary
    def test_delete_summary(self):
        tester = app.test_client(self)
        response = tester.delete('/summaries/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
