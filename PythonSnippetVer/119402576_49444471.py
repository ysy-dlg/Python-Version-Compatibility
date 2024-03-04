async def stop(self):
    self.server.close()
    await self.server.wait_closed()