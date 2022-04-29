CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Categories ('label') VALUES ('Sports');
INSERT INTO Categories ('label') VALUES ('Travel');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content') VALUES (2, 1, 'Shrek Tech Makes Me Sweat', 'April, 25,2022', 'Shrek is coming in hot with the new Shrek tv and go phone.  You will be oogling and orgring over every ounce of it.  These new devices are going to be so farquading tite.')
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content') VALUES (1, 3, 'Shrek Tech Makes Me Sweat', 'April, 25,2022', 'Pokem ipsum dolor sit amet Gothitelle Rotom Yellow Gothita Minccino Zephyr Badge. Water Teleport Rapidash Trubbish Regirock Quilava Mudkip. Ghost Spinda Elekid Zebstrika Lilligant Buneary Nincada. Sunt in culpa Mothim Relicanth Pidove Golduck Shedinja Fuchsia City. Red Pichu Electabuzz Lumineon Mienfoo Razor Leaf Vermilion City.')
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content') VALUES (3, 1, 'Shrek Tech Makes Me Sweat', 'April, 25,2022', 'Sonic Boom Ice Rapidash theyre comfy and easy to wear Tynamo Shellos Jigglypuff. Sonic Boom Hitmonlee Regirock Machamp Chingling Raichu Rayquaza. Viridian City Sceptile Panpour Mr. Mime Caterpie Darmanitan Meowth. Glitch City Vermilion City Gorebyss Garchomp Sand-Attack Happiny Magmortar. Viridian City Johto Whimsicott Mienshao Ditto Hippopotas Solrock.')
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content') VALUES (2, 2, 'Shrek Tech Makes Me Sweat', 'April, 25,2022', 'Splash Gastly Leech Life Tail Whip ex ea commodo consequat Mineral Badge Dewott. Rage searching far and wide Stunfisk Venusaur Kricketot Palpitoad Togetic. Fighting Dusknoir Ciccino Ashs mother Escavalier Stunky Leaf Green. Squirtle Bibarel Snover Stoutland Gabite Mewtwo Rotom. Vine Whip Houndour Whirlipede Cacnea Gothitelle the enemy Pokemon fainted Azelf.')
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content') VALUES (2, 2, 'Shrek Tech Makes Me Sweat', 'April, 25,2022', 'Splash Gastly Leech Life Tail Whip ex ea commodo consequat Mineral Badge Dewott. Rage searching far and wide Stunfisk Venusaur Kricketot Palpitoad Togetic. Fighting Dusknoir Ciccino Ashs mother Escavalier Stunky Leaf Green. Squirtle Bibarel Snover Stoutland Gabite Mewtwo Rotom. Vine Whip Houndour Whirlipede Cacnea Gothitelle the enemy Pokemon fainted Azelf.')
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content') VALUES (2, 2, 'Shrek Tech Makes Me Sweat', 'April, 25,2022', 'Splash Gastly Leech Life Tail Whip ex ea commodo consequat Mineral Badge Dewott. Rage searching far and wide Stunfisk Venusaur Kricketot Palpitoad Togetic. Fighting Dusknoir Ciccino Ashs mother Escavalier Stunky Leaf Green. Squirtle Bibarel Snover Stoutland Gabite Mewtwo Rotom. Vine Whip Houndour Whirlipede Cacnea Gothitelle the enemy Pokemon fainted Azelf.')
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content') VALUES (1, 2, 'Are Ogres the Hot New Thing: Everything you Need to Know About SHREXulization', 'April, 25,2022', 'Splash Gastly Leech Life Tail Whip ex ea commodo consequat Mineral Badge Dewott. Rage searching far and wide Stunfisk Venusaur Kricketot Palpitoad Togetic. Fighting Dusknoir Ciccino Ashs mother Escavalier Stunky Leaf Green. Squirtle Bibarel Snover Stoutland Gabite Mewtwo Rotom. Vine Whip Houndour Whirlipede Cacnea Gothitelle the enemy Pokemon fainted Azelf.')
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'content') VALUES (1, 2, 'Pokemon: Satan"s Smile', 'April, 25,2022', 'Splash Gastly Leech Life Tail Whip ex ea commodo consequat Mineral Badge Dewott. Rage searching far and wide Stunfisk Venusaur Kricketot Palpitoad Togetic. Fighting Dusknoir Ciccino Ashs mother Escavalier Stunky Leaf Green. Squirtle Bibarel Snover Stoutland Gabite Mewtwo Rotom. Vine Whip Houndour Whirlipede Cacnea Gothitelle the enemy Pokemon fainted Azelf.')

INSERT INTO Users ('first_name', 'last_name', 'email', 'bio', 'username', 'password') VALUES ('Derek', 'Chills', 'drchills420@notmail.com', 'Pokem ipsum dolor sit amet Parasect Exeggcute our courage will pull us through Petilil Numel Trapinch. Scratch Clefairy Smoochum Stoutland Ursaring Abomasnow Mirror Move. Squirtle Zoroark Zebstrika The Power Of One Quilava Pidgeot Marsh Badge. Pokemon Phione Ambipom Milotic Scyther Bronzor Shroomish. Dragon Wobbuffet Walrein Groudon Grumpig Crawdaunt Ninjask.', 'dchills69', '66669420')
INSERT INTO Users ('first_name', 'last_name', 'email', 'bio', 'username', 'password') VALUES ('Tony', 'Cheese', 'tortuga69@notmail.com', 'Red Poison Sting Zigzagoon Luvdisc Skorupi Machoke Durant. Viridian City Nidoqueen Sawk Venomoth Gigalith Tirtouga Surskit. Viridian City Mirror Move to catch them is my real test Archeops Hoppip Hidden Machine Burnt Berry. Sunt in culpa Bubble Hoppip anim id est laborum Super Potion Seismitoad Crustle. Blue Chatot Yellow Wingull Trubbish Simisear Samurott.', 'cheese420', '66669420')

INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 2);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 3);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (8, 2);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (8, 3);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (9, 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (9, 3);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (10, 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (10, 2);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (10, 3);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (11, 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (12, 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (12, 3);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (13, 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (14, 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (14, 2);
