from azure.storage.blob import BlobClient, BlobBlock

# Configuration
connection_string = "DefaultEndpointsProtocol=https;AccountName=YOURSTORAGEACCTNAME;AccountKey=YOURSTORAGEKEY;EndpointSuffix=core.windows.net"
container_name = "blobtest"
blob_name = "10GB_file.mp4"
file_path = "10GB_file.mp4"

# Create Blob client
blob_client = BlobClient.from_connection_string(connection_string, container_name, blob_name)

# Define block size
block_size = 100 * 1024 * 1024  # 100 MB per block -  this can be upto 4000 but more memory is needed on the VM

# Read file and divide into blocks
with open(file_path, "rb") as file:
    file_data = file.read()
    blocks = [file_data[i : i + block_size] for i in range(0, len(file_data), block_size)]

# Upload blocks
block_ids = []
for i, block in enumerate(blocks):
    block_id = format(i, "05")
    blob_client.stage_block(block_id, block)
    block_ids.append(block_id)

# Commit blocks
blob_client.commit_block_list(block_ids)
