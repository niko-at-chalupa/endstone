import pytest
from endstone import Player
from endstone.command import Command, CommandSender
from endstone.event import PacketSendEvent, event_handler
from endstone.plugin import Plugin

from .tests.conftest import clear_runtime_context, set_runtime_context

# Frequent packet IDs to filter out from logging
FILTERED_PACKET_IDS = {
    0x10,  # ServerPlayerPostMovePosition
    0x12,  # MoveAbsoluteActor
    0x13,  # MovePlayer
    0x15,  # UpdateBlock
    0x19,  # LevelEvent
    0x27,  # SetActorData
    0x28,  # SetActorMotion
    0x3A,  # FullChunkData
    0x6F,  # MoveDeltaActor
    0x73,  # Ping
    0x79,  # NetworkChunkPublisherUpdate
    0x7B,  # LevelSoundEvent
    0x87,  # ClientCacheBlobStatusPacket
    0x88,  # ClientCacheMissResponsePacket
    0x90,  # PlayerAuthInputPacket
    0xA1,  # CorrectPlayerMovePredictionPacket
    0xAE,  # SubChunkPacket
    0xAF,  # SubChunkRequestPacket
}


class PacketListener:
    def __init__(self, plugin: Plugin):
        self.plugin = plugin

    @event_handler
    def on_packet_send(self, event: PacketSendEvent) -> None:
        if event.packet_id in FILTERED_PACKET_IDS:
            return
        player_name = event.player.name if event.player else "N/A"
        self.plugin.logger.info(
            f"[PacketSend] id=0x{event.packet_id:02X} player={player_name} "
            f"payload={event.payload.hex()}"
        )


class EndstoneTest(Plugin):
    prefix = "Test"
    api_version = "0.11"
    commands = {
        "test": {
            "description": "Run the tests",
            "usages": ["/test"],
            "permissions": ["endstone_test.command.test"],
        }
    }

    permissions = {
        "endstone_test.command.test": {
            "description": "Allow users to use the /test command.",
            "default": "op",
        }
    }

    def on_load(self) -> None:
        self.logger.info("on_load is called!")

    def on_enable(self) -> None:
        self.logger.info("on_enable is called!")
        self.register_events(PacketListener(self))
        self.run_tests()

    def on_command(
        self, sender: CommandSender, command: Command, args: list[str]
    ) -> bool:
        if command.name == "test" and isinstance(sender, Player):
            self.run_tests(player=sender)
            return True
        return False

    def on_disable(self) -> None:
        self.logger.info("on_disable is called!")

    def run_tests(self, **kwargs):
        marker = "player" if "player" in kwargs else "not player"
        set_runtime_context(server=self.server, plugin=self, **kwargs)
        try:
            return pytest.main(
                [
                    "-s",
                    "-m",
                    marker,
                    "--pyargs",
                    "endstone_test.tests",
                ]
            )
        finally:
            clear_runtime_context()
