import sc2
from sc2 import run_game,maps,Race,Difficulty,position
from sc2.player import Bot,Computer
from sc2.constants import PROBE

class TestBot(sc2.BotAI):
    async def on_step(self,iteration):
        await self.moveWorker()

    async def moveWorker(self):
        print(self.enemy_start_locations[0])
        scout = self.units(PROBE)[0]
        await self.do(scout.move(position.Point2(position.Pointlike(self.enemy_start_locations[0]))))

run_game(maps.get("(2)CatalystLE"),[
    Bot(Race.Protoss,TestBot()),
    Computer(Race.Terran,Difficulty.Easy)
    ],realtime=True)
