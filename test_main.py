from main import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello from your CI/CD pipeline deployed on Render!" in response.data

