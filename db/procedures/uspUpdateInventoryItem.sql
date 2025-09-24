UPDATE tblInventory
SET colInventoryQuantity = @quantity, colInventoryDescription = '@note'
WHERE colInventoryID = @primarykey