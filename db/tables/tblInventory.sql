CREATE TABLE IF NOT EXISTS "tblInventory" (
	"colInventoryID"	INTEGER NOT NULL,
	"colInventoryName"	TEXT NOT NULL,
	"colInventoryQuantity"	INTEGER,
	"colInventoryDescription"	TEXT,
	PRIMARY KEY("colInventoryID")
);