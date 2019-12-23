INSERT INTO styles (style_name, code, premium) VALUES
	('ancient', '----', FALSE),
	('modern', '----', FALSE),
	('futuristic', '----', TRUE),
	('news', '----', FALSE),
	('comedy', '----', FALSE),
	('history', '----', TRUE);


INSERT INTO sites (site_adress, site_name) VALUES
	('newsmy.com', 'Good news'),
	('newstest.com', 'Bad news'),
	('coolnews.com', 'Cool news');


INSERT INTO pages (element_id, index, path) VALUES
	('news_1', 'main', 'main.html'),
	('info_1', 'main', 'main.html'),
	('copyright_1', 'main', 'main.html');


INSERT INTO users (nickname, login, password) VALUES
	('ASIMER', 'ASIMER', 'ASIMER'),
	('Kelioris', 'Kelioris', 'Kelioris'),
	('Tereshchenko', 'Tereshchenko', 'Tereshchenko');


INSERT INTO countries (country_name) VALUES
    ('Ukraine'),
    ('Russia'),
    ('Belarus');


INSERT INTO occupation (occupation) VALUES
    ('student'),
    ('teacher'),
    ('work');


INSERT INTO block (style_name, block_name, block_type, code) VALUES
    ('modern', 'news', 'div', '<h1>Today news</h1>'),
    ('futuristic', 'info', 'div', '----'),
    ('futuristic', 'copyright', 'footer', '----'),
    ('ancient', 'copyright', 'div', '----'),
    ('ancient', 'info', 'div', '----'),
    ('ancient', 'copyright', 'footer', '----');


INSERT INTO "premium access" (nickname, plan, expires) VALUES
	('ASIMER', 'without premium', NULL),
	('Kelioris', 'econom', '2020-09-1'),
	('Tereshchenko', 'pro', '2020-10-1');


INSERT INTO topic_analitycs (topic_name, words, paragraphs, focus_time, sentences, images) VALUES
	('news', 1245, 12, '0:1:13.878746', 14, 0.4),
	('modern', 452, 2, '0:0:23.369432', 6, 0.8),
	('futuristic', 452, 2, '0:0:23.369432', 6, 0.8),
	('ancient', 452, 2, '0:0:23.369432', 6, 0.8),
	('comedy', 452, 2, '0:0:23.369432', 6, 0.8),
	('history', 2245, 16, '0:2:1.647847', 18, 0.4);


INSERT INTO topic_style (style_name, topic_name, priority) VALUES
	('modern', 'news', 1),
	('futuristic', 'comedy', 2),
	('ancient', 'history', 3);


INSERT INTO user_countries (nickname, country_name) VALUES
	('ASIMER', 'Ukraine'),
	('Kelioris', 'Russia'),
	('Tereshchenko', 'Belarus');


INSERT INTO user_positions (occupation, nickname) VALUES
	('student', 'ASIMER'),
	('work', 'Kelioris'),
	('teacher', 'Tereshchenko');


INSERT INTO user_sites (site_adress, nickname, create_date) VALUES
	('newsmy.com', 'ASIMER', '2018-02-10'),
	('newstest.com', 'Kelioris', '2019-03-10'),
	('coolnews.com', 'Tereshchenko', '2019-04-10');


INSERT INTO user_styles (nickname, style_name) VALUES
	('ASIMER', 'ancient'),
	('Kelioris', 'futuristic'),
	('Tereshchenko', 'modern');


INSERT INTO popularity (style_topic_name, popularity) VALUES
	('modern', 123),
	('futuristic', 914),
	('news', 332),
	('comedy', 154),
	('history', 441),
	('ancient', 929);


INSERT INTO positions (style_name, element_id, block_name, block_type, "position") VALUES
	('modern', 'news_1', 'news', 'div', 'center'),
	('ancient', 'info_1', 'info', 'div', 'left'),
	('futuristic', 'copyright_1', 'copyright', 'footer', 'bottom');


INSERT INTO topics (style_name, block_name, block_type, topic_name) VALUES
	('modern', 'news', 'div', 'comedy'),
	('futuristic', 'info', 'div', 'news'),
	('ancient', 'copyright', 'div', 'history');