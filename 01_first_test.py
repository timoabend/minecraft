import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()
mc.postToChat("Hello Minecraft")
time.sleep(5)

playerPos = mc.player.getPos()
mc.player.setPos(playerPos.x, playerPos.y + 50, playerPos.z)
mc.postToChat("Don't look down")
time.sleep(5)

playerTilePos = mc.player.getTilePos()
blockBelowPlayerType = mc.getBlock(playerTilePos.x, playerTilePos.y -1, playerTilePos.z)
mc.setBlock(playerTilePos.x + 1, playerTilePos.y + 1, playerTilePos.z, blockBelowPlayerType)
mc.setBlock(playerTilePos.x, playerTilePos.y + 1, playerTilePos.z + 1, blockBelowPlayerType)
mc.setBlock(playerTilePos.x - 1, playerTilePos.y + 1, playerTilePos.z, blockBelowPlayerType)
mc.setBlock(playerTilePos.x, playerTilePos.y + 1, playerTilePos.z -1, blockBelowPlayerType)
mc.postToChat("Trapped")

mc.setBlock(playerTilePos.x + 1, playerTilePos.y + 1, playerTilePos.y, block.AIR)
mc.postToChat("Be free!")
time.sleep(5)

mc.setBlocks(playerTilePos.x - 25, playerTilePos.y - 1, playerTilePos.z -25, playerTilePos.x + 25, playerTilePos.y - 1, playerTilePos.z + 25, block.DIAMOND_BLOCK)
mc.postToChat("Diamond")
