from unittest.mock import MagicMock
from app.storage import MemoryStorage
from app.service import EmailVerifierService


def test_process_and_save_email_success():
    mock_client = MagicMock()
    mock_client.email_verify.return_value = {
        "data": {"status": "valid", "score": 95}
    }

    storage = MemoryStorage()
    service = EmailVerifierService(api_client=mock_client, storage=storage)

    result = service.process_and_save("ceo@startup.com")

    assert result is True

    mock_client.email_verify.assert_called_once_with("ceo@startup.com")

    saved_data = storage.read("ceo@startup.com")
    assert saved_data == {"status": "valid", "score": 95}


def test_process_and_save_email_api_error():
    mock_client = MagicMock()
    mock_client.email_verify.side_effect = Exception("HTTP 401 Unauthorized")

    storage = MemoryStorage()
    service = EmailVerifierService(api_client=mock_client, storage=storage)

    result = service.process_and_save("fail@startup.com")

    assert result is False

    assert storage.read("fail@startup.com") is None