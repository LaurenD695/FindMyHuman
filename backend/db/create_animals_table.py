import psycopg2

# Replace these with your actual PostgreSQL credentials
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Create table
cur.execute("""
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS animals (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    isAdoptionPending BOOLEAN,
    ageGroup VARCHAR(50),
    isBirthDateExact BOOLEAN,
    breedString TEXT,
    breedPrimary VARCHAR(100),
    breedPrimaryId INTEGER,
    isBreedMixed BOOLEAN,
    isCatsOk BOOLEAN,
    isCourtesyListing BOOLEAN,
    isCurrentVaccinations BOOLEAN,
    isDeclawed BOOLEAN,
    descriptionHtml TEXT,
    descriptionText TEXT,
    isNeedingFoster BOOLEAN,
    isFound BOOLEAN,
    priority INTEGER,
    isHousetrained BOOLEAN,
    name VARCHAR(100),
    pictureCount INTEGER,
    pictureThumbnailUrl TEXT,
    qualities TEXT[],  -- Assuming it's always a list of strings
    rescueId VARCHAR(50),
    sex VARCHAR(10),
    slug TEXT,
    isSpecialNeeds BOOLEAN,
    isSponsorable BOOLEAN,
    videoCount INTEGER,
    videoUrlCount INTEGER,
    createdDate TIMESTAMPTZ,
    updatedDate TIMESTAMPTZ,
    ageString VARCHAR(50),        -- Optional
    birthDate TIMESTAMPTZ         -- Optional
);
""")

conn.commit()
cur.close()
conn.close()
