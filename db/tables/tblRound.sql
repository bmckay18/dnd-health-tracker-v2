CREATE TABLE IF NOT EXISTS "tblRound" (
    "colRound" INTEGER NOT NULL
);

INSERT INTO tblRound (colRound) 
SELECT 1
WHERE NOT EXISTS (
    SELECT 1 FROM tblRound
);