-- Table: public."Discipline"

-- DROP TABLE public."Discipline";

CREATE TABLE public."Discipline"
(
    discipline_id integer NOT NULL,
    discipline_name text COLLATE pg_catalog."default" NOT NULL,
    discipline_group text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Discipline_pkey" PRIMARY KEY (discipline_id),
    CONSTRAINT discipline_group FOREIGN KEY (discipline_group)
        REFERENCES public."Group" (group_name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public."Discipline"
    OWNER to postgres;

-- Table: public."Group"

-- DROP TABLE public."Group";

CREATE TABLE public."Group"
(
    group_id integer NOT NULL,
    group_name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Group1_pkey" PRIMARY KEY (group_id),
    CONSTRAINT "Group1_group_name_key" UNIQUE (group_name)

)

TABLESPACE pg_default;

ALTER TABLE public."Group"
    OWNER to postgres;

-- Table: public."Student"

-- DROP TABLE public."Student";

CREATE TABLE public."Student"
(
    student_id integer NOT NULL,
    student_university text COLLATE pg_catalog."default" NOT NULL,
    student_faculty text COLLATE pg_catalog."default" NOT NULL,
    student_group text COLLATE pg_catalog."default" NOT NULL,
    student_name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Student_pkey" PRIMARY KEY (student_id),
    CONSTRAINT student_group FOREIGN KEY (student_group)
        REFERENCES public."Group" (group_name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public."Student"
    OWNER to postgres;