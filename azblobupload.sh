#!/bin/bash

# Replace the following variables with your own values
storageAccountName="YOURSTORAGEACCTNAME"
storageContainerName="YOURCONTAINERNAME"
localFilePath="YOURLOCALFILENAME"
blobName="YOURFILENAMEINBLOB"

# Upload the local file to the blob
az storage blob upload \
    --file $blobName \
    --account-name "$storageAccountName" \
    --account-key "$(az storage account keys list --account-name "$storageAccountName" --query '[0].value' -o tsv)" \
    --type block \
    --container-name "$storageContainerName" \
    --name "$blobName" \
    --type block \
