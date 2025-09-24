CREATE TABLE IF NOT EXISTS "tblNPC" (
	"colNPCID"	INTEGER NOT NULL,
	"colNPCName"	TEXT,
	"colNPCMaxHP"	NUMERIC,
	"colNPCHP"	NUMERIC,
	PRIMARY KEY("colNPCID")
);
CREATE TABLE IF NOT EXISTS "tblInventory" (
	"colInventoryID"	INTEGER NOT NULL,
	"colInventoryName"	TEXT NOT NULL,
	"colInventoryQuantity"	INTEGER,
	"colInventoryDescription"	TEXT,
	PRIMARY KEY("colInventoryID")
);
CREATE TABLE IF NOT EXISTS "tblGold" (
	"colGoldID" INTEGER NOT NULL, 
	"colGoldAmount" INTEGER,
	"colGoldDifference" INTEGER, 
	PRIMARY KEY ("colGoldID")
);