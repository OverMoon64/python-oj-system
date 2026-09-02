from typing import Any

from fastapi import FastAPI

app = FastAPI(
    title="Python OJ System",
    description="程序设计训练实验二：在线评测系统",
    version="0.1.0",
)


@app.get("/health")
async def health_check() -> dict[str, Any]:
    """检查后端服务是否正常运行。"""

    return {
        "code": 200,
        "msg": "success",
        "data": {
            "status": "ok",
        },
    }
