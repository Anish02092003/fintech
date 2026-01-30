from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_compare_upload_invalid_file():
    response = client.post(
        "/company/compare-upload",
        files={
            "file_a": ("a.txt", b"invalid"),
            "file_b": ("b.txt", b"invalid"),
        },
        data={
            "company_a_name": "A",
            "company_b_name": "B",
        },
    )

    assert response.status_code == 400