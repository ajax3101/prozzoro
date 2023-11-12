create table region(
	id			bigint not null primary key,
	name		character varying(128) not null,
	crt_date	TIMESTAMP with time zone NOT NULL DEFAULT NOW());
	
create table agency(
	id			bigint not null primary key,
	region_id	bigint not null REFERENCES region (id),
	name		character varying(200) not null,
	edrpou		character varying(10)	not null,
	crt_date	TIMESTAMP with time zone NOT NULL DEFAULT NOW());
	
insert into region(id, name) values (0, 'Обласна ланка');
insert into region(id, name) values (1, 'Бердянський район');
insert into region(id, name) values (2, 'Василівський район');
insert into region(id, name) values (3, 'Запорізький район');
insert into region(id, name) values (4, 'Мелітопольський район');
insert into region(id, name) values (5, 'Пологівський район');

insert into agency(id, region_id, name, edrpou) values (0, 0, 'Запорізька обласна державна адміністрація (апарат)', '00022504');
insert into agency(id, region_id, name, edrpou) values (1, 0, 'Департамент економічного розвитку і торгівлі Запорізької обласної державної адміністрації', '02741456');
insert into agency(id, region_id, name, edrpou) values (2, 0, 'Департамент житлово-комунального господарства та будівництва Запорізької обласної державної адміністрації', '33836176');
insert into agency(id, region_id, name, edrpou) values (3, 0, 'Департамент агропромислового розвитку Запорізької обласної державної адміністрації', '00731270');
insert into agency(id, region_id, name, edrpou) values (4, 0, 'Департамент з питань цивільного захисту населення Запорізької обласної державної адміністрації', '14373165');
insert into agency(id, region_id, name, edrpou) values (5, 0, 'Департамент соціального захисту населення Запорізької обласної державної адміністрації', '03193005');
insert into agency(id, region_id, name, edrpou) values (6, 0, 'Департамент освіти і науки Запорізької обласної державної адміністрації', '02143429');
insert into agency(id, region_id, name, edrpou) values (7, 0, 'Департамент охорони здоров''я Запорізької обласної державної адміністрації', '02012869');
insert into agency(id, region_id, name, edrpou) values (8, 0, 'Департамент культури, туризму, національностей та релігій Запорізької обласної державної адміністрації', '02228109');
insert into agency(id, region_id, name, edrpou) values (9, 0, 'Управління зовнішніх зносин та зовнішньоекономічної діяльності Запорізької обласної державної адміністрації', '25971041');
insert into agency(id, region_id, name, edrpou) values (10, 0, 'Управління містобудування та архітектури Запорізької обласної державної адміністрації', '35258283');
insert into agency(id, region_id, name, edrpou) values (11, 0, 'Департамент захисту довкілля Запорізької обласної державної адміністрації', '43847544');
insert into agency(id, region_id, name, edrpou) values (12, 0, 'Департамент внутрішньої політики та інформаційної діяльності Запорізької обласної державної адміністрації', '34718647');
insert into agency(id, region_id, name, edrpou) values (13, 0, 'Відділ внутрішнього аудиту Запорізької обласної державної адміністрації', '38732555');
insert into agency(id, region_id, name, edrpou) values (14, 0, 'Державний архів Запорізької області', '03494617');
insert into agency(id, region_id, name, edrpou) values (15, 0, 'Служба у справах дітей Запорізької обласної державної адміністрації', '25765784');
insert into agency(id, region_id, name, edrpou) values (16, 0, 'Управління молоді, фізичної культури та спорту Запорізької обласної державної адміністрації', '38922191');
insert into agency(id, region_id, name, edrpou) values (17, 0, 'Департамент фінансів Запорізької обласної державної адміністрації', '02313714');
insert into agency(id, region_id, name, edrpou) values (18, 0, 'Управління оборонної роботи та взаємодії з правоохоронними органами Запорізької обласної державної адміністрації', '45021701');
insert into agency(id, region_id, name, edrpou) values (19, 0, 'Управління транспорту та зв’язку Запорізької обласної державної адміністрації (реорганізовується в Департамент інфраструктури та промисловості з 01.11.2023)', '44638516');
insert into agency(id, region_id, name, edrpou) values (20, 0, 'Управління стратегічних галузей виробництва Запорізької обласної державної адміністрації (ліквідується з 01.11.2023)', '44574751');
insert into agency(id, region_id, name, edrpou) values (21, 1, 'Бердянська районна державна адміністрація', '02140840');
insert into agency(id, region_id, name, edrpou) values (22, 1, 'Відділ фінансів Бердянської районної державної адміністрації', '02313803');
insert into agency(id, region_id, name, edrpou) values (23, 1, 'Управління соціального захисту населення Бердянської районної державної адміністрації', '03193181');
insert into agency(id, region_id, name, edrpou) values (24, 2, 'Василівська районна державна адміністрація Запорізької області', '02140857');
insert into agency(id, region_id, name, edrpou) values (25, 2, 'Відділ фінансів Василівської районної державної адміністрації Запорізької області', '02313861');
insert into agency(id, region_id, name, edrpou) values (26, 2, 'Управління соціального захисту населення  Василівської районної державної адміністрації Запорізької області', '03193117');
insert into agency(id, region_id, name, edrpou) values (27, 3, 'Запорізька районна державна адміністрація Запорізької області', '20488417');
insert into agency(id, region_id, name, edrpou) values (28, 3, 'Відділ фінансів Запорізької районної державної адміністрації Запорізької області', '20488432');
insert into agency(id, region_id, name, edrpou) values (29, 3, 'Управління соціального захисту населення Запорізької районної державної адміністрації Запорізької області', '03193241');
insert into agency(id, region_id, name, edrpou) values (30, 3, 'Служба у справах дітей Запорізької районної державної адміністрації Запорізької області', '34157121');
insert into agency(id, region_id, name, edrpou) values (31, 3, 'Відділ освіти, охорони здоров''я, культури і спорту Запорізької районної державної адміністрації Запорізької області', '25218792');
insert into agency(id, region_id, name, edrpou) values (32, 4, 'Мелітопольська районна державна адміністрація Запорізької області', '02126314');
insert into agency(id, region_id, name, edrpou) values (33, 4, 'Управління соціального захисту населення  Мелітопольської районної державної адміністрації Запорізької області', '03193057');
insert into agency(id, region_id, name, edrpou) values (34, 4, 'Служба у справах дітей  Мелітопольської районної державної адміністрації    Запорізької області', '35432646');
insert into agency(id, region_id, name, edrpou) values (35, 4, 'Відділ фінансів Мелітопольської районної державної адміністрації Запорізької області', '02313648');
insert into agency(id, region_id, name, edrpou) values (36, 4, 'Відділ, освіти, охорони здоров''я, культури та спорту  Мелітопольської районної державної адміністрації Запорізької області', '02136100');
insert into agency(id, region_id, name, edrpou) values (37, 5, 'Пологівська районна державна адміністрація Запорізької області', '02126354');
insert into agency(id, region_id, name, edrpou) values (38, 5, 'Архівний відділ Пологівської районної державної адміністрації Запорізької області', '44251875');
insert into agency(id, region_id, name, edrpou) values (39, 5, 'Фінансовий відділ Пологівської районної державної адміністрації Запорізької області', '02313708');
insert into agency(id, region_id, name, edrpou) values (40, 5, 'Служба у справах дітей Пологівської районної державної адміністрації Запорізької області', '25219811');
insert into agency(id, region_id, name, edrpou) values (41, 5, 'Управління соціального захисту населення Пологівської районної державної адміністрації Запорізької області', '03193123');