from Block import Block

blockchain = []

genesis_block = Block("Genesis block", ["John Doe sent 1 BTC to Jane Doe",
                                        "Tracy sent 4 BTC to Mark",
                                        "Mary sent 2 BTC to Jane"])

second_block = Block(genesis_block.block_hash, ["Barbara sent 3 BTC to Jane",
                                                "Sam sent 67 BTC to Jim"])

third_block = Block(second_block.block_hash, ["Liz sent 4 BTC to Sonya"])                                                

print("Block hash: genesis block -> " + genesis_block.block_hash)
print("Block hash: second block -> " + second_block.block_hash)
print("Block hash: third block -> " + third_block.block_hash)  