@pytest.fixture
async def server(event_loop):
    from server import Server
    the_server = Server()
    await the_server.start()
    yield the_server
    await the_server.stop()