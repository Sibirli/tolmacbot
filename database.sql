CREATE TABLE "profile" (
	"id" serial NOT NULL,
	"chat_id" int NOT NULL UNIQUE,
	"first_name" TEXT NOT NULL,
	"last_name" TEXT,
	"username" TEXT UNIQUE,
	"date" int NOT NULL,
	CONSTRAINT "profile_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

