DELETE FROM tblNPC;
DELETE FROM tblInventory;
DELETE FROM tblGold;

INSERT INTO tblNPC (colNPCName, colNPCMaxHP, colNPCHP)
VALUES 
('goblin', 12, 12),
('boar 1', 5, 2),
('boar 2', 5, 5),
('Sir James', 56, 56),
('Cleric', 41, 41);

INSERT INTO tblInventory (colInventoryName, colInventoryQuantity, colInventoryDescription)
VALUES
('+1 Longsword', 1, NULL),
('Potion of Healing', 15, NULL),
('Mysterious Scroll', 1, 'The scroll has markings that you do not recognise'),
('Scroll of Fireball', 1, NULL),
('Potion of Invisibility', 15, NULL),
('Sword of the Ancients', 1, 'This blade was forged by those of old'),
('Flute', 1, NULL),
('Trombone', 12, NULL),
('Tear of the Gods', 1, NULL),
('Bag of Holding', 1, NULL),
('Potion of Hill Giant Strength', 2, NULL),
('Elixir of Vitality', 1, NULL);

INSERT INTO tblGold (colGoldAmount, colGoldDifference)
VALUES 
(1832, 1832),
(1932, 100),
(1000, -932),
(-500, -1500),
(150, 650);