from app.storage import MemoryStorage


def test_storage_create_and_read():
    storage = MemoryStorage()
    test_email = "test@mail.com"
    test_data = {"status": "valid", "score": 100}

    storage.create(test_email, test_data)
    result = storage.read(test_email)

    assert result == test_data


def test_storage_update():
    storage = MemoryStorage()
    storage.create("dev@mail.com", {"status": "unknown"})

    is_updated = storage.update("dev@mail.com", {"status": "valid"})

    assert is_updated is True
    assert storage.read("dev@mail.com") == {"status": "valid"}


def test_storage_update_non_existent():
    storage = MemoryStorage()

    is_updated = storage.update("ghost@mail.com", {"status": "valid"})

    assert is_updated is False