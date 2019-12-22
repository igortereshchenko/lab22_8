insert into "Group"(
                    group_id,
                    group_name)
values (10, 'km-62');

insert into "Group"(
                    group_id,
                    group_name)
values (11, 'km-61');

insert into "Group"(
                    group_id,
                    group_name)
values (12, 'test');
----------------------------------------------------------------------
insert into "Student"(
                    student_id,
                    student_university,
                    student_faculty,
                    student_group,
                    student_name)
values (10, 'kpi', 'FPM', 'km-62', 'yehor sedinin');

insert into "Student"(
                    student_id,
                    student_university,
                    student_faculty,
                    student_group,
                    student_name)
values (11, 'kpi', 'FPM', 'km-61', 'test test');

insert into "Student"(
                    student_id,
                    student_university,
                    student_faculty,
                    student_group,
                    student_name)
values (12, 'nekpi', 'rtf', 'test', '12345');

----------------------------------------------------------------------

insert into "Discipline"(
                    discipline_id,
                    discipline_name,
                    discipline_group)
values (10, 'math', 'km-62');

insert into "Discipline"(
                    discipline_id,
                    discipline_name,
                    discipline_group)
values (11, 'bd', 'km-61');

insert into "Discipline"(
                    discipline_id,
                    discipline_name,
                    discipline_group)
values (12, 'ai', 'test');
