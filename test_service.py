from nameko.testing.services import worker_factory
from temp_messenger.service import MessageService, WebServer


def test_konnichiwa():
    service = worker_factory(MessageService)
    result = service.konnichiwa()
    assert result == 'Konnichiwa!'

