/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     05/11/2019 04:00:34                          */
/*==============================================================*/


drop index block_style_FK;

drop index block_PK;

drop table block;

drop index countries_PK;

drop table countries;

drop index occupation_PK;

drop table occupation;

drop index pages_PK;

drop table pages;

drop index popularity2_FK;

drop index popularity_FK;

drop index popularity_PK;

drop table popularity;

drop index block_has_position_FK;

drop index pages_contains_positions_FK;

drop index positions_PK;

drop table positions;

drop index user_has_access_FK;

drop index "premium access_PK";

drop table "premium access";

drop index sites_PK;

drop table sites;

drop index styles_PK;

drop table styles;

drop index topic_analitycs_PK;

drop table topic_analitycs;

drop index topic_style2_FK;

drop index topic_style_FK;

drop index topic_style_PK;

drop table topic_style;

drop index topics2_FK;

drop index topics_FK;

drop index topics_PK;

drop table topics;

drop index user_countries2_FK;

drop index user_countries_FK;

drop index user_countries_PK;

drop table user_countries;

drop index user_positions2_FK;

drop index user_positions_FK;

drop index user_positions_PK;

drop table user_positions;

drop index user_sites2_FK;

drop index user_sites_FK;

drop index user_sites_PK;

drop table user_sites;

drop index user_styles2_FK;

drop index user_styles_FK;

drop index user_styles_PK;

drop table user_styles;

drop index users_PK;

drop table users;

/*==============================================================*/
/* Table: block                                                 */
/*==============================================================*/
create table block (
   style_name           TEXT                 not null,
   block_name           TEXT                 not null,
   block_type           TEXT                 not null,
   code                 TEXT                 null,
   source               TEXT                 null,
   constraint PK_BLOCK primary key (style_name, block_name, block_type)
);

/*==============================================================*/
/* Index: block_PK                                              */
/*==============================================================*/
create unique index block_PK on block (
style_name,
block_name,
block_type
);

/*==============================================================*/
/* Index: block_style_FK                                        */
/*==============================================================*/
create  index block_style_FK on block (
style_name
);

/*==============================================================*/
/* Table: countries                                             */
/*==============================================================*/
create table countries (
   country_name         TEXT                 not null,
   constraint PK_COUNTRIES primary key (country_name)
);

/*==============================================================*/
/* Index: countries_PK                                          */
/*==============================================================*/
create unique index countries_PK on countries (
country_name
);

/*==============================================================*/
/* Table: occupation                                            */
/*==============================================================*/
create table occupation (
   occupation           TEXT                 not null,
   constraint PK_OCCUPATION primary key (occupation)
);

/*==============================================================*/
/* Index: occupation_PK                                         */
/*==============================================================*/
create unique index occupation_PK on occupation (
occupation
);

/*==============================================================*/
/* Table: pages                                                 */
/*==============================================================*/
create table pages (
   element_id           TEXT                 not null,
   index                TEXT                 null,
   path                 TEXT                 null,
   constraint PK_PAGES primary key (element_id)
);

/*==============================================================*/
/* Index: pages_PK                                              */
/*==============================================================*/
create unique index pages_PK on pages (
element_id
);

/*==============================================================*/
/* Table: popularity                                            */
/*==============================================================*/
create table popularity (
   style_topic_name     TEXT                 not null,
   popularity           INT4                 null,
   constraint PK_POPULARITY primary key (style_topic_name)
);

/*==============================================================*/
/* Index: popularity_PK                                         */
/*==============================================================*/
create unique index popularity_PK on popularity (
style_topic_name
);

/*==============================================================*/
/* Index: popularity_FK                                         */
/*==============================================================*/
create  index popularity_FK on popularity (
style_topic_name
);

/*==============================================================*/
/* Index: popularity2_FK                                        */
/*==============================================================*/
create  index popularity2_FK on popularity (
style_topic_name
);

/*==============================================================*/
/* Table: positions                                             */
/*==============================================================*/
create table positions (
   element_id           TEXT                 not null,
   style_name           TEXT                 not null,
   block_name           TEXT                 not null,
   block_type           TEXT                 not null,
   "position"           TEXT                 not null,
   constraint PK_POSITIONS primary key (style_name, element_id, block_name, block_type, "position")
);

/*==============================================================*/
/* Index: positions_PK                                          */
/*==============================================================*/
create unique index positions_PK on positions (
style_name,
element_id,
block_name,
block_type,
"position"
);

/*==============================================================*/
/* Index: pages_contains_positions_FK                           */
/*==============================================================*/
create  index pages_contains_positions_FK on positions (
element_id
);

/*==============================================================*/
/* Index: block_has_position_FK                                 */
/*==============================================================*/
create  index block_has_position_FK on positions (
style_name,
block_name,
block_type
);

/*==============================================================*/
/* Table: "premium access"                                      */
/*==============================================================*/
create table "premium access" (
   nickname             TEXT                 not null,
   plan                 TEXT                 not null,
   expires              DATE                 null,
   constraint "PK_PREMIUM ACCESS" primary key (nickname, plan)
);

/*==============================================================*/
/* Index: "premium access_PK"                                   */
/*==============================================================*/
create unique index "premium access_PK" on "premium access" (
nickname,
plan
);

/*==============================================================*/
/* Index: user_has_access_FK                                    */
/*==============================================================*/
create  index user_has_access_FK on "premium access" (
nickname
);

/*==============================================================*/
/* Table: sites                                                 */
/*==============================================================*/
create table sites (
   site_adress          TEXT                 not null,
   site_name            TEXT                 null,
   constraint PK_SITES primary key (site_adress)
);

/*==============================================================*/
/* Index: sites_PK                                              */
/*==============================================================*/
create unique index sites_PK on sites (
site_adress
);

/*==============================================================*/
/* Table: styles                                                */
/*==============================================================*/
create table styles (
   style_name           TEXT                 not null,
   code                 TEXT                 null,
   premium              BOOL                 null,
   constraint PK_STYLES primary key (style_name)
);

/*==============================================================*/
/* Index: styles_PK                                             */
/*==============================================================*/
create unique index styles_PK on styles (
style_name
);

/*==============================================================*/
/* Table: topic_analitycs                                       */
/*==============================================================*/
create table topic_analitycs (
   topic_name           TEXT                 not null,
   words                INT4                 null,
   paragraphs           INT4                 null,
   focus_time           TIME                 null,
   sentences            INT4                 null,
   images               FLOAT8               null,
   constraint PK_TOPIC_ANALITYCS primary key (topic_name),
   constraint sentences_more_then_paragraphs check (sentences >= paragraphs),
   constraint words_more_then_sentences check (words >= sentences)
);

/*==============================================================*/
/* Index: topic_analitycs_PK                                    */
/*==============================================================*/
create unique index topic_analitycs_PK on topic_analitycs (
topic_name
);

/*==============================================================*/
/* Table: topic_style                                           */
/*==============================================================*/
create table topic_style (
   style_name           TEXT                 not null,
   topic_name           TEXT                 not null,
   priority             INT4                 null,
   constraint PK_TOPIC_STYLE primary key (style_name, topic_name)
);

/*==============================================================*/
/* Index: topic_style_PK                                        */
/*==============================================================*/
create unique index topic_style_PK on topic_style (
style_name,
topic_name
);

/*==============================================================*/
/* Index: topic_style_FK                                        */
/*==============================================================*/
create  index topic_style_FK on topic_style (
style_name
);

/*==============================================================*/
/* Index: topic_style2_FK                                       */
/*==============================================================*/
create  index topic_style2_FK on topic_style (
topic_name
);

/*==============================================================*/
/* Table: topics                                                */
/*==============================================================*/
create table topics (
   style_name           TEXT                 not null,
   block_name           TEXT                 not null,
   block_type           TEXT                 not null,
   topic_name           TEXT                 not null,
   constraint PK_TOPICS primary key (style_name, block_name, block_type, topic_name)
);

/*==============================================================*/
/* Index: topics_PK                                             */
/*==============================================================*/
create unique index topics_PK on topics (
style_name,
block_name,
block_type,
topic_name
);

/*==============================================================*/
/* Index: topics_FK                                             */
/*==============================================================*/
create  index topics_FK on topics (
style_name,
block_name,
block_type
);

/*==============================================================*/
/* Index: topics2_FK                                            */
/*==============================================================*/
create  index topics2_FK on topics (
topic_name
);

/*==============================================================*/
/* Table: user_countries                                        */
/*==============================================================*/
create table user_countries (
   nickname             TEXT                 not null,
   country_name         TEXT                 not null,
   constraint PK_USER_COUNTRIES primary key (nickname, country_name)
);

/*==============================================================*/
/* Index: user_countries_PK                                     */
/*==============================================================*/
create unique index user_countries_PK on user_countries (
nickname,
country_name
);

/*==============================================================*/
/* Index: user_countries_FK                                     */
/*==============================================================*/
create  index user_countries_FK on user_countries (
nickname
);

/*==============================================================*/
/* Index: user_countries2_FK                                    */
/*==============================================================*/
create  index user_countries2_FK on user_countries (
country_name
);

/*==============================================================*/
/* Table: user_positions                                        */
/*==============================================================*/
create table user_positions (
   occupation           TEXT                 not null,
   nickname             TEXT                 not null,
   constraint PK_USER_POSITIONS primary key (occupation, nickname)
);

/*==============================================================*/
/* Index: user_positions_PK                                     */
/*==============================================================*/
create unique index user_positions_PK on user_positions (
occupation,
nickname
);

/*==============================================================*/
/* Index: user_positions_FK                                     */
/*==============================================================*/
create  index user_positions_FK on user_positions (
occupation
);

/*==============================================================*/
/* Index: user_positions2_FK                                    */
/*==============================================================*/
create  index user_positions2_FK on user_positions (
nickname
);

/*==============================================================*/
/* Table: user_sites                                            */
/*==============================================================*/
create table user_sites (
   site_adress          TEXT                 not null,
   nickname             TEXT                 not null,
   create_date          DATE                 null,
   constraint PK_USER_SITES primary key (site_adress, nickname)
);

/*==============================================================*/
/* Index: user_sites_PK                                         */
/*==============================================================*/
create unique index user_sites_PK on user_sites (
site_adress,
nickname
);

/*==============================================================*/
/* Index: user_sites_FK                                         */
/*==============================================================*/
create  index user_sites_FK on user_sites (
site_adress
);

/*==============================================================*/
/* Index: user_sites2_FK                                        */
/*==============================================================*/
create  index user_sites2_FK on user_sites (
nickname
);

/*==============================================================*/
/* Table: user_styles                                           */
/*==============================================================*/
create table user_styles (
   nickname             TEXT                 not null,
   style_name           TEXT                 not null,
   constraint PK_USER_STYLES primary key (nickname, style_name)
);

/*==============================================================*/
/* Index: user_styles_PK                                        */
/*==============================================================*/
create unique index user_styles_PK on user_styles (
nickname,
style_name
);

/*==============================================================*/
/* Index: user_styles_FK                                        */
/*==============================================================*/
create  index user_styles_FK on user_styles (
nickname
);

/*==============================================================*/
/* Index: user_styles2_FK                                       */
/*==============================================================*/
create  index user_styles2_FK on user_styles (
style_name
);

/*==============================================================*/
/* Table: users                                                 */
/*==============================================================*/
create table users (
   nickname             TEXT                 not null,
   login                TEXT                 null,
   password             TEXT                 null,
   constraint PK_USERS primary key (nickname)
);

/*==============================================================*/
/* Index: users_PK                                              */
/*==============================================================*/
create unique index users_PK on users (
nickname
);

alter table block
   add constraint FK_BLOCK_BLOCK_STY_STYLES foreign key (style_name)
      references styles (style_name)
      on delete restrict on update restrict;

alter table popularity
   add constraint FK_POPULARI_POPULARIT_STYLES foreign key (style_topic_name)
      references styles (style_name)
      on delete restrict on update restrict;

alter table popularity
   add constraint FK_POPULARI_POPULARIT_TOPIC_AN foreign key (style_topic_name)
      references topic_analitycs (topic_name)
      on delete restrict on update restrict;

alter table positions
   add constraint FK_POSITION_BLOCK_HAS_BLOCK foreign key (style_name, block_name, block_type)
      references block (style_name, block_name, block_type)
      on delete restrict on update restrict;

alter table positions
   add constraint FK_POSITION_PAGES_CON_PAGES foreign key (element_id)
      references pages (element_id)
      on delete restrict on update restrict;

alter table "premium access"
   add constraint "FK_PREMIUM _USER_HAS__USERS" foreign key (nickname)
      references users (nickname)
      on delete restrict on update restrict;

alter table topic_style
   add constraint FK_TOPIC_ST_TOPIC_STY_STYLES foreign key (style_name)
      references styles (style_name)
      on delete restrict on update restrict;

alter table topic_style
   add constraint FK_TOPIC_ST_TOPIC_STY_TOPIC_AN foreign key (topic_name)
      references topic_analitycs (topic_name)
      on delete restrict on update restrict;

alter table topics
   add constraint FK_TOPICS_TOPICS_BLOCK foreign key (style_name, block_name, block_type)
      references block (style_name, block_name, block_type)
      on delete restrict on update restrict;

alter table topics
   add constraint FK_TOPICS_TOPICS2_TOPIC_AN foreign key (topic_name)
      references topic_analitycs (topic_name)
      on delete restrict on update restrict;

alter table user_countries
   add constraint FK_USER_COU_USER_COUN_USERS foreign key (nickname)
      references users (nickname)
      on delete restrict on update restrict;

alter table user_countries
   add constraint FK_USER_COU_USER_COUN_COUNTRIE foreign key (country_name)
      references countries (country_name)
      on delete restrict on update restrict;

alter table user_positions
   add constraint FK_USER_POS_USER_POSI_OCCUPATI foreign key (occupation)
      references occupation (occupation)
      on delete restrict on update restrict;

alter table user_positions
   add constraint FK_USER_POS_USER_POSI_USERS foreign key (nickname)
      references users (nickname)
      on delete restrict on update restrict;

alter table user_sites
   add constraint FK_USER_SIT_USER_SITE_SITES foreign key (site_adress)
      references sites (site_adress)
      on delete restrict on update restrict;

alter table user_sites
   add constraint FK_USER_SIT_USER_SITE_USERS foreign key (nickname)
      references users (nickname)
      on delete restrict on update restrict;

alter table user_styles
   add constraint FK_USER_STY_USER_STYL_USERS foreign key (nickname)
      references users (nickname)
      on delete restrict on update restrict;

alter table user_styles
   add constraint FK_USER_STY_USER_STYL_STYLES foreign key (style_name)
      references styles (style_name)
      on delete restrict on update restrict;

