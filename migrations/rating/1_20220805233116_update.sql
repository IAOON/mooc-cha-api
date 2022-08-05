-- upgrade --
CREATE TABLE IF NOT EXISTS "rating" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "target_id" INT NOT NULL REFERENCES "ratable" ("id") ON DELETE CASCADE
);
-- downgrade --
DROP TABLE IF EXISTS "rating";
