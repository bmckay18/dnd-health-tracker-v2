SELECT COALESCE(
    (SELECT colGoldAmount 
     FROM tblGold 
     WHERE colGoldID = (SELECT MAX(colGoldID) FROM tblGold)
    ), 0
) AS colGoldAmount;