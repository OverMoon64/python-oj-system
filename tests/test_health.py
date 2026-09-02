from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check() -> None:
    """健康检查接口应返回标准成功响应。"""

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "code": 200,
        "msg": "success",
        "data": {
            "status": "ok",
        },
    }
